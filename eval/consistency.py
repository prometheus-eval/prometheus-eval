import json
import os
from collections import defaultdict
from pathlib import Path

import krippendorff
import numpy as np
import pandas as pd
from tqdm import tqdm

from eval.utils import parse_filename


def read_data_from_file(output_file_path):
    with open(output_file_path, "r") as file:
        return [json.loads(line) for line in file]


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    print("Calculating consistency...")

    overall_results = defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        )
    )

    base_path = Path(output_dir)
    subdirectories = sorted(
        [d for d in base_path.iterdir() if d.is_dir()], key=lambda x: str(x)
    )
    for subdir in tqdm(subdirectories):
        # Ignore hermes, zephyr outputs
        if (
            "hermes" in subdir.name
            or "zephyr" in subdir.name
            or "gemma" in subdir.name
            or "slerp" in subdir.name
            or "ties" in subdir.name
        ):
            continue
        # import pdb; pdb.set_trace()
        json_file_paths = list(subdir.rglob("*.json"))
        for file_path in json_file_paths:
            filename = file_path.name
            str_file_path = str(file_path)
            experiment_meta = parse_filename(filename)
            # Assuming parse_filename returns None for files that don't match expected pattern
            if not experiment_meta or isinstance(experiment_meta, str):
                print(experiment_meta, ":", filename)
                continue
            try:
                data_name = experiment_meta["data_name"]
                temp = experiment_meta["temperature"]
                mode = experiment_meta["mode"]
                model_id = subdir.name.replace("-outputs", "")
                filename.replace("_output.json", "")
                mode = experiment_meta["mode"]
            except:
                raise Exception

            if mode != "a2a":
                continue

            data = read_data_from_file(str_file_path)

            rate_A = []
            rate_B = []
            rate_C = []

            error_flag = False

            for record in data:
                scores = record["prometheus_score"]
                if len(scores) != 3:
                    print("Error: ", data_name, model_id, mode, temp)
                    error_flag = True
                    break
                rate_A.append(scores[0])
                rate_B.append(scores[1])
                rate_C.append(scores[2])

            if error_flag:
                result_val = -100
            else:
                rate_data = np.array([rate_A, rate_B, rate_C])

                alpha_ordinal = krippendorff.alpha(
                    reliability_data=rate_data, level_of_measurement="ordinal"
                )
                result_val = alpha_ordinal

            overall_results[data_name][model_id][mode][temp] = result_val

    rows_list = []
    for data_name, models in overall_results.items():
        for model_id, modes in models.items():
            for mode, temps in modes.items():
                for temp, result_val in temps.items():
                    row = {
                        "Data Name": data_name,
                        "Model ID": model_id,
                        "Mode": mode,
                        "Temperature": temp,
                        "Consistency": result_val,
                    }
                    rows_list.append(row)

    df = pd.DataFrame(rows_list)

    models_list = [
        "Llama-2-7b-chat-hf",
        "Llama-2-13b-chat-hf",
        "Llama-2-70b-chat-hf",
        "Mistral-7B-Instruct-v0.2",
        "Mixtral-8x7B-Instruct-v0.1",
        "prometheus-7b-v1.0",
        "prometheus-13b-v1.0",
        "autoj-13b",
        "prometheus-7b-v1.5-beta-merged",
        "prometheus-mixtral-v0.2-dare",
        "gpt-3.5-turbo-0613",
        "gpt-4-0613",
        "gpt-4-1106-preview",
        "gpt-4-0126-preview",
    ]

    # df['Model ID'] = pd.Categorical(df['Model ID'], categories=models_list, ordered=True)
    # df_sorted = df.sort_values('Model ID')

    # report_path = os.path.join(report_dir, f"ABS_CONSISTENCY.md")
    report_path = os.path.join(report_dir, f"abs_consistency.csv")
    df.to_csv(report_path, index=False)

    # with open(report_path, "w") as md_file:
    #     md_file.write(df.to_markdown(index=False))

    # if "mt_bench_human_judgement" in experiment_id or "autoj" in experiment_id:
    #     no_tie_sub_results = calculate_results(
    #         str_file_path, mode=mode, skip_tie=True
    #     )
    #     overall_results[data_name][model_id][mode][temp][
    #         "skip_tie_True"
    #     ] = no_tie_sub_results


if __name__ == "__main__":
    main()
