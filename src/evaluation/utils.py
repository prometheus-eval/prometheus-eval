import json
import pdb
import re
import statistics

from scipy.stats import kendalltau, pearsonr, spearmanr

from src.evaluation.benchmark.autoj_utils.pairwise_eval import (
    evaluate_autoj_performance,
)

DEBUG = False

model_type_2_mode = {
    "v1.0": "absolute",
    "v2.0": "both",
}

dataset_2_mode = {
    "alpaca_eval": "relative",
    "hhh_alignment_eval": "relative",
    "mt_bench_human_judgement_eval": "relative",
    "autoj_pairwise": "relative",
    "vicuna_eval": "absolute",
    "flask_eval": "absolute",
    "mt_bench_eval": "absolute",
    "feedback_collection_ood_test": "absolute",
    "preference_collection_ood_test": "relative",
}


def get_mode(model_name: str, eval_data_name: str) -> str:
    org_name = model_name.split("/")[0]

    if org_name == "kaist-ai":
        model_type = model_name.split("-")[-1]
        model_mode = model_type_2_mode[model_type]
    else:
        model_mode = "both"

    data_mode = dataset_2_mode[eval_data_name]

    return model_mode, data_mode


def calculate_results(output_file_path, mode="a2a", skip_tie=False):
    # print(f"Calculating results for {output_file_path}...")

    def read_data_from_file():
        with open(output_file_path, "r") as file:
            return [json.loads(line) for line in file]

    def calculate_mean_scores(score_key):
        return [statistics.mean(d[score_key]) for d in data if d[score_key]]

    def calculate_correlations(scores1, scores2):
        pr, _ = pearsonr(scores1, scores2)
        sr, _ = spearmanr(scores1, scores2)
        kt, _ = kendalltau(scores1, scores2)
        return {
            "Pearson": pr,
            "Kendall": kt,
            "Spearman": sr,
        }

    data = read_data_from_file()
    data_name = output_file_path.split("/")[-1].replace("_output.json", "")

    if mode == "a2a":
        prometheus_scores = calculate_mean_scores("prometheus_score")
        results = {}

        if "feedback_collection_ood_test" in data_name:
            gpt4_scores = [d["gpt4_score"] for d in data]
            prometheus_scores = [d["prometheus_score"][0] for d in data]
            correct_predictions = sum(
                1 for x, y in zip(prometheus_scores, gpt4_scores) if x == y
            )

            total_predictions = len(prometheus_scores)
            accuracy = correct_predictions / total_predictions

            results["Accuracy"] = accuracy * 100
            prometheus_scores = calculate_mean_scores("prometheus_score")

            results["with GPT4"] = calculate_correlations(
                prometheus_scores, gpt4_scores
            )
            return results

        if "flask" in output_file_path:
            human_scores = calculate_mean_scores("human_score")
            results["with Human"] = calculate_correlations(
                prometheus_scores, human_scores
            )

        gpt4_scores = calculate_mean_scores("gpt4_score")
        results["with GPT4"] = calculate_correlations(prometheus_scores, gpt4_scores)
        return results

    def calculate_one_abs_acc(data, acc_list: list):
        accepted_scores, rejected_scores = (
            data["prometheus_score"][0],
            data["prometheus_score"][1],
        )
        assert len(accepted_scores) == len(rejected_scores)
        # assert len(accepted_scores) == 5
        # mean_accepted_scores = statistics.mean(accepted_scores)
        # mean_rejected_scores = statistics.mean(rejected_scores)

        runs = min(len(accepted_scores), 3)

        if "tie" not in data.keys():
            # if mean_accepted_scores > mean_rejected_scores:
            #     acc_list.append(1)
            # else:
            #     acc_list.append(0)
            for i in range(runs):
                if accepted_scores[i] is None or rejected_scores[i] is None:
                    pass
                elif accepted_scores[i] > rejected_scores[i]:
                    acc_list.append(1)
                    break
                elif accepted_scores[i] < rejected_scores[i]:
                    acc_list.append(0)
                    break

                if i == (runs - 1):
                    acc_list.append(0)
                    break
        else:
            if data["tie"] == 0:
                # if mean_accepted_scores > mean_rejected_scores:
                #     acc_list.append(1)
                # else:
                #     acc_list.append(0)
                for i in range(runs):
                    if accepted_scores[i] is None or rejected_scores[i] is None:
                        pass
                    elif accepted_scores[i] > rejected_scores[i]:
                        acc_list.append(1)
                        break
                    elif accepted_scores[i] < rejected_scores[i]:
                        acc_list.append(0)
                        break

                    if i == (runs - 1):
                        acc_list.append(0)
                        break
            elif data["tie"] == 1:
                if skip_tie:
                    return

                if (
                    accepted_scores[0] is not None
                    and rejected_scores[0] is not None
                    and accepted_scores[0] == rejected_scores[0]
                ):
                    acc_list.append(1)
                else:
                    acc_list.append(0)
        return

    def calculate_one_rel_acc(data, acc_list: list):
        alphabet_list = data["prometheus_score"]
        alphabet_list = [item.upper() for item in alphabet_list if item is not None]

        if DEBUG:
            for alphabet in alphabet_list:
                if alphabet not in ["A", "B", "TIE", None]:
                    print("Invalid alphabet extracted: ", alphabet)
                    pdb.set_trace()

        assert all(
            alphabet in {"A", "B", "TIE", None} for alphabet in alphabet_list
        ), "alphabet_list contains values other than 'A', 'B', or "

        counts = {
            alphabet: alphabet_list.count(alphabet) for alphabet in set(alphabet_list)
        }

        # max_alphabet = max(counts, key=counts.get)
        try:
            max_alphabet = alphabet_list[0]
        except:
            max_alphabet = None

        if "chosen" not in data.keys():
            data["chosen"] = "A"
            print("Warning: Key 'Chosen' should be in the data.")

        if "tie" not in data.keys():
            if max_alphabet == data["chosen"]:
                acc_list.append(1)
            else:
                acc_list.append(0)
        else:
            if data["tie"] == 0:
                if max_alphabet == data["chosen"]:
                    acc_list.append(1)
                else:
                    acc_list.append(0)
            elif data["tie"] == 1:
                if skip_tie:
                    return

                if max_alphabet == "TIE":
                    acc_list.append(1)
                # elif (
                #     alphabet_list[0] != alphabet_list[1] and "TIE" not in alphabet_list
                # ):
                #     acc_list.append(1)
                else:
                    acc_list.append(0)
        return

    assert mode in ["a2r", "r2r"]

    data_name = output_file_path.split("/")[-1]
    output_file_path.split("/")[-2].replace("-outputs", "")

    if "autoj" in data_name:
        return evaluate_autoj_performance(data, mode, skip_tie=skip_tie)

    if mode == "r2r":
        calculate_acc_func = calculate_one_rel_acc
    else:
        calculate_acc_func = calculate_one_abs_acc

    acc_dict = {"helpful": [], "harmless": [], "honest": [], "other": []}
    accs = []

    for d in data:
        if "hhh" in data_name:
            acc_list = acc_dict[d["source"]]
            calculate_acc_func(d, acc_list)
        elif "mt_bench" in data_name:
            acc_list = accs
            calculate_acc_func(d, acc_list)
        elif "alpaca" in data_name:
            acc_list = accs
            calculate_acc_func(d, acc_list)
        elif "preference_collection_ood_test" in data_name:
            acc_list = accs
            calculate_acc_func(d, acc_list)

    results = {}
    for key, value in acc_dict.items():
        acc = statistics.mean(value) if value else None
        if acc is not None:
            accs.extend(value)
            results[key] = acc

    if accs:
        results["Average"] = statistics.mean(accs)

    return results


def extract_sections(prompt):
    sections = prompt.split("###")
    extracted = {}

    # Iterate over sections to identify and extract relevant parts
    for section in sections:
        if "Task Description:" in section:
            extracted["task_description"] = section.split("Task Description:\n")[
                1
            ].strip()
        elif "The instruction to evaluate:" in section:
            extracted["orig_instruction"] = section.split(
                "The instruction to evaluate:\n"
            )[1].strip()
        elif "Response to evaluate:" in section:
            extracted["orig_response"] = section.split("Response to evaluate:\n")[
                1
            ].strip()
        elif "Score Rubrics:" in section:
            extracted["score_rubric"] = section.split("Score Rubrics:\n")[1].strip()
        elif "Feedback:" in section:
            extracted["feedback"] = section.split("Feedback:")[1].strip()
        elif "Reference Answer (Score 5):" in section:
            extracted["reference_answer"] = section.split("Reference Answer (Score 5):")[1].strip()
    
    return extracted


def parse_filename(filename):
    pattern = re.compile(
        r"(?P<data_name>.+?)_(?P<mode>r2r|a2r|a2a)_temp(?P<temperature>\d+\.\d+)(?:_sys_(?P<system>.+))?"
    )
    match = pattern.match(filename)

    if match:
        data = match.groupdict()
        data["temperature"] = float(data["temperature"])
        data["system"] = data["system"] == "output"

        return data
    else:
        return "The filename does not match the expected pattern."


if __name__ == "__main__":
    # prompt = """###Task Description:\nAn instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.\n1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.\n2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.\n3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"\n4. Please do not generate any other opening, closing, and explanations.\n\n###The instruction to evaluate:\nHere is a previous dialogue between an assistant and an user. Generate a human preferable response by the assistant.\nUser: Rewrite your previous response. Start every sentence with the letter A.\n\n\n\n###Response to evaluate:\nAbsolutely! A recent trip to the beautiful island of Hawaii was an adventure that I will never forget.\n\nAs a helpful assistant, I highly recommend a visit to the Polynesian Cultural Center as it immerses you in the cultures of the Pacific Islands.\n\nAlso, a trip to the North Shore is a must-see attraction, where you can witness surfers of all levels tackling the massive waves.\n\nAdditionally, paying respects to the brave men and women who lost their lives at Pearl Harbor was a deeply moving experience.\n\nAnd let's not forget about the delicious local cuisine, from poke bowls to shave ice, the flavors of Hawaii are truly unique and tasty.\n\nAll in all, Hawaii has it all - cultural immersion, natural beauty, and delicious food. As an assistant, I encourage you to put Hawaii at the top of your travel list. Aloha!\n\n###Score Rubrics:\n[Does the model's response offer direct, pertinent, and valuable information that actively assists the user's query or concern in a dialogue? The response should align with the user's needs and offer proactive suggestions or advice, if applicable.]\nScore 1: The model's response is completely off-topic and offers no helpful information or direction in relation to the user's query or concern.\nScore 2: The model's response vaguely addresses the user's query, but it lacks depth, clarity, or relevance, necessitating the user to seek further clarification.\nScore 3: The model's response addresses the user's query, but misses certain key aspects or does not provide additional helpful insights that might be relevant to the user.\nScore 4: The model's response effectively addresses the user's query, providing pertinent information. It might offer some proactive suggestions, but might not cover all potential insights or advice.\nScore 5: The model's response perfectly addresses the user's query, offering direct, comprehensive, and pertinent information. It anticipates further questions and provides proactive suggestions or advice, fully aligning with the user's needs.\n\n###Feedback: \","""
    # extracted_sections = extract_sections(prompt)
    # print(extracted_sections)

    filename = "autoj_pairwise_r2r_temp1.0_sys_output"
    parsed_info = parse_filename(filename)
    print(parsed_info)
