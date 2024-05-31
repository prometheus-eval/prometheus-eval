import argparse
import json
import os
from pathlib import Path

import huggingface_hub
from datasets import load_dataset
from dotenv import dotenv_values
from transformers import AutoTokenizer

from src import CACHE_DIR
from src.fastchat_conversation import get_conv_template
from src.llms.vllm_utils import VLLM
from src.load_utils import (
    RESPONSE_BASE_PATH,
    get_biggenbench_uid2data,
    get_response_data_dict,
)
from src.model_list import get_model_num_gpus, get_model_type


def apply_template_hf(tokenizer, records: list, model_name: str):
    inputs = []

    for record in records:
        if tokenizer.chat_template is not None and "system" in tokenizer.chat_template:
            messages = [
                {"role": "system", "content": record["system_prompt"]},
                {"role": "user", "content": record["input"]},
            ]
        else:
            messages = [
                {
                    "role": "user",
                    "content": record["system_prompt"] + "\n\n" + record["input"],
                }
            ]

        input_str = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs.append(input_str)
    return inputs


def apply_template_batch(records: list, model_name: str, urial=None, urial_prompt=None):
    model_inputs = []

    if urial:
        assert urial_prompt is not None
        assert isinstance(urial_prompt, str)

    def map_to_conv(model_name: str, urial=None):
        if urial:
            if "inst_help_v5" in urial:
                conv = get_conv_template("urial_v5")
            elif "inst_help_v6" in urial:
                conv = get_conv_template("urial_v6")
            else:
                conv = get_conv_template("urial_backticks")
            conv.set_system_message(urial_prompt)
        elif "tulu" in model_name.lower():
            conv = get_conv_template("tulu")
        elif "openhermes" in model_name.lower() or "nous-hermes" in model_name.lower():
            conv = get_conv_template("OpenHermes-2.5-Mistral-7B")
        elif "zephyr" in model_name.lower():
            conv = get_conv_template("zephyr")
        elif "llama-2" in model_name.lower() or "codellama" in model_name.lower():
            conv = get_conv_template("llama-2")
        elif "mixtral" in model_name.lower() or "mistral" in model_name.lower():
            conv = get_conv_template("mistral")
        elif "yi" in model_name.lower() and "chat" in model_name.lower():
            conv = get_conv_template("Yi-34b-chat")
        elif "vicuna" in model_name.lower():
            conv = get_conv_template("vicuna_v1.1")
        elif "gemma" in model_name.lower():
            conv = get_conv_template("gemma")
        elif "qwen" in model_name.lower():
            conv = get_conv_template("qwen-7b-chat")
        elif "openchat" in model_name.lower():
            conv = get_conv_template("openchat_3.5")
        elif "orca-2" in model_name.lower():
            conv = get_conv_template("orca-2")
        else:
            raise ValueError(f"Model {model_name} not supported")
        return conv

    for record in records:
        conv = map_to_conv(model_name, urial)
        if urial:
            conv.append_message(
                conv.roles[0], record["system_prompt"] + "\n\n" + record["input"]
            )
            conv.append_message(conv.roles[1], None)
        else:
            conv.set_system_message(record["system_prompt"])
            conv.append_message(conv.roles[0], record["input"])
            conv.append_message(conv.roles[1], None)

        model_inputs.append(conv.get_prompt())
    return model_inputs


def dummy_completions(inputs, **kwargs):
    return ["dummy output"] * len(inputs)


def load_urial_prompt():
    urials = ["inst_1k_v4", "inst_1k_v4.help"]
    urial_prompts = []
    for urial in urials:
        url = f"urial_prompts/{urial}.txt"
        dataset = load_dataset(
            "text",
            data_files=url,
            split="train",
            sample_by="document",
            download_mode="force_redownload",
        )
        urial_prompts.append(dataset["text"][0])

    assert len(urial_prompts) == 2
    return urial_prompts


def prepare_inputs(
    tokenizer,
    records,
    model_name: str,
    safety: bool = False,
    urial_prompts: list = None,
):
    model_type = get_model_type(model_name)
    if model_type == "base":
        if safety:
            inputs = apply_template_batch(
                records, model_name, urial="inst_1k_v4", urial_prompt=urial_prompts[0]
            )
        else:
            inputs = apply_template_batch(
                records,
                model_name,
                urial="inst_1k_v4.help",
                urial_prompt=urial_prompts[1],
            )
    elif model_type == "instruct":
        try:
            if tokenizer.chat_template is not None and "gemma" not in model_name:
                inputs = apply_template_hf(tokenizer, records, model_name)
            elif "c4ai-command-r-plus-4bit" in model_name:
                inputs = apply_template_hf(tokenizer, records, model_name)
            else:
                inputs = apply_template_batch(records, model_name, urial=None)
            # if "OLMo" in model_name:
            #     inputs = apply_template_hf(records, model_name)
            # else:
            #     inputs = apply_template_batch(records, model_name, urial=None)
        except ValueError(f"Model {model_name} not supported"):
            inputs = apply_template_hf(records, model_name)
    else:
        raise ValueError(f"Model {model_name} not supported")

    return inputs


def main(model_id: str, num_gpus: int, force_rerun: bool):
    response_model_name = model_id.split("/")[-1]
    response_model_type = get_model_type(model_id)

    response_file_path = (
        Path(RESPONSE_BASE_PATH) / f"{response_model_name}_responses.json"
    )

    print(f"Model: {response_model_name}")
    if os.path.exists(response_file_path):
        print("\tResponse file exists")
        response_data_dict = get_response_data_dict(response_model_name)
        data_cnt = len(response_data_dict.keys())
        print("\t\tData count: ", data_cnt)
    else:
        response_data_dict = {}
        print("\tResponse file does not exist")
        print("\tFirst generate response for this model and then run evaluate\n")

    full_data_dict = get_biggenbench_uid2data()

    to_run_uids = set(full_data_dict.keys()) - set(response_data_dict.keys())
    filtered_uids = []

    # For inference, multilingual tasks are skipped for base models
    for uid in to_run_uids:
        if "multilingual" in uid:
            if response_model_type == "base":
                continue
        filtered_uids.append(uid)

    if len(filtered_uids) == 0:
        print("All responses are already generated.")
        return

    # When preparing inputs, safety tasks for base models should be marked
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

    inputs = []
    urial_prompts = load_urial_prompt()
    for uid in filtered_uids:
        record = full_data_dict[uid]

        if "safety" in uid and response_model_type == "base":
            inputs.append(
                prepare_inputs(
                    tokenizer,
                    [record],
                    model_id,
                    safety=True,
                    urial_prompts=urial_prompts,
                )[0]
            )
        else:
            inputs.append(
                prepare_inputs(
                    tokenizer, [record], model_id, urial_prompts=urial_prompts
                )[0]
            )

    params = {
        "max_tokens": 2048,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
    }

    if "awq" in model_id.lower():
        model = VLLM(
            model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR, quantization="AWQ"
        )
    elif "gptq" in model_id.lower():
        model = VLLM(
            model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR, quantization="GPTQ"
        )
    else:
        model = VLLM(model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR)

    outputs = model.completions(inputs, **params, use_tqdm=True)
    for idx, output in enumerate(outputs):
        if output == "":
            outputs[idx] = "Too long input."

    # Parsing the output for base models (because of urial prompts)
    if response_model_type == "base":
        for idx, output in enumerate(outputs):
            outputs[idx] = outputs[idx].split("```\n\n# Query:")[0].strip()

    for idx, uid in enumerate(filtered_uids):
        response_data_dict[uid] = {
            "capability": full_data_dict[uid]["capability"],
            "task": full_data_dict[uid]["task"],
            "response": outputs[idx].strip(),
        }

    response_output_dict = {}
    for key, val in response_data_dict.items():
        response_output_dict[key] = {
            "capability": val["capability"],
            "task": val["task"],
            "response": val["response"].strip(),
        }

    response_file_path.parent.mkdir(parents=True, exist_ok=True)
    response_output_dict = dict(sorted(response_output_dict.items()))

    with response_file_path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(response_output_dict, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="meta-llama/Llama-2-7b-chat-hf",
        help="Name of the model to evaluate",
    )
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Use system prompt during evaluation",
    )

    args = parser.parse_args()
    num_gpus = get_model_num_gpus(args.model_name)

    hf_token = dotenv_values(".env")["HF_TOKEN"]
    huggingface_hub.login(token=hf_token)

    main(args.model_name, num_gpus, False)
