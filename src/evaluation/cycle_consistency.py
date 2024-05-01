import json
import os
import random
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from src.evaluation.benchmark import EvalDataLoader
from src.evaluation.utils import parse_filename

loader = EvalDataLoader("feedback_collection_ood_test")
records = loader.get_records()


def read_data_from_file(output_file_path):
    with open(output_file_path, "r") as file:
        return [json.loads(line) for line in file]


def search_dict(orig_response):
    matching_dicts = [d for d in records if d["orig_response"] == orig_response]
    assert len(matching_dicts) == 1
    return matching_dicts[0]["gpt4_score"]


def add_response_score_A(row):
    return search_dict(row["orig_response_A"])


def add_response_score_B(row):
    return search_dict(row["orig_response_B"])


def add_prometheus_score(row):
    return row["prometheus_score"][0]


def add_prometheus_score_a2r(row):
    score_a = row["prometheus_score"][0][0]
    score_b = row["prometheus_score"][1][0]

    score_a = 0 if score_a is None else score_a
    score_b = 0 if score_b is None else score_b

    if score_a > score_b:
        return "A"
    elif score_a == score_b:
        return random.choice(["A", "B"])
    else:
        return "B"


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.path.join(os.path.dirname(__file__), "reports")
    print("Calculating cycle consistency...")

    base_path = Path(output_dir)
    subdirectories = sorted(
        [d for d in base_path.iterdir() if d.is_dir()], key=lambda x: str(x)
    )

    overall_results = {}

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

            if data_name != "preference_collection_ood_test":
                continue

            if temp == 0.0:
                continue

            if mode == "a2a":
                continue

            result_key = f"{model_id}_{mode}"

            data = read_data_from_file(str_file_path)
            df = pd.DataFrame(data)
            df["orig_score_A"] = df.apply(add_response_score_A, axis=1)
            df["orig_score_B"] = df.apply(add_response_score_B, axis=1)
            grouped = df.groupby("orig_instruction")
            # print("len(grouped): ", len(grouped))

            group_list = []

            total_nums = 0
            correct_nums = 0

            for _, group in tqdm(grouped, desc="Grouping"):
                assert len(group) == 10
                group_list.append(group)

                # print(group.head(10))

                for score in [1, 2, 3, 4, 5]:
                    # print("Calculating for score", score)
                    if mode == "r2r":
                        group["prometheus_score_final"] = group.apply(
                            add_prometheus_score, axis=1
                        )
                    elif mode == "a2r":
                        group["prometheus_score_final"] = group.apply(
                            add_prometheus_score_a2r, axis=1
                        )

                    score_A_win = group[
                        (group["orig_score_A"] == score) & (group["chosen"] == "A")
                    ]  # X < 1
                    score_A_lose = group[
                        (group["orig_score_A"] == score) & (group["chosen"] == "B")
                    ]  # 1 < X
                    score_B_win = group[
                        (group["orig_score_B"] == score) & (group["chosen"] == "B")
                    ]  # X < 1
                    score_B_lose = group[
                        (group["orig_score_B"] == score) & (group["chosen"] == "A")
                    ]  # 1 < X

                    # print(len(score_A_win))
                    # print(len(score_B_lose))
                    # print(len(score_B_win))
                    # print(len(score_B_lose))

                    left_group = list(
                        set(
                            list(score_A_win["orig_score_B"].unique())
                            + list(score_B_win["orig_score_A"].unique())
                        )
                    )
                    right_group = list(
                        set(
                            list(score_A_lose["orig_score_B"].unique())
                            + list(score_B_lose["orig_score_A"].unique())
                        )
                    )

                    # print("left_group: ", left_group)
                    # print("right_group: ", right_group)

                    search_group = []
                    for i in range(len(left_group)):
                        for j in range(len(right_group)):
                            search_group.append((left_group[i], right_group[j]))

                    # print(search_group)
                    total_nums += len(search_group)

                    for x, y in search_group:
                        # import pdb; pdb.set_trace()
                        # import pdb; pdb.set_trace()
                        if mode == "r2r":
                            temp_A = group[
                                (group["orig_score_A"] == x)
                                & (group["orig_score_B"] == y)
                                & (group["prometheus_score_final"] == "B")
                            ]
                            temp_B = group[
                                (group["orig_score_A"] == y)
                                & (group["orig_score_B"] == x)
                                & (group["prometheus_score_final"] == "A")
                            ]
                        elif mode == "a2r":
                            temp_A = group[
                                (group["orig_score_A"] == x)
                                & (group["orig_score_B"] == y)
                                & (group["prometheus_score_final"] == "B")
                            ]
                            temp_B = group[
                                (group["orig_score_A"] == y)
                                & (group["orig_score_B"] == x)
                                & (group["prometheus_score_final"] == "A")
                            ]

                        # import pdb; pdb.set_trace()
                        count = len(temp_A) + len(temp_B)
                        # assert count == 1
                        if count == 1:
                            correct_nums += 1

            print(f"{model_id} Accuracy: ", correct_nums / total_nums)
            overall_results[result_key] = correct_nums / total_nums

    print(overall_results)


if __name__ == "__main__":
    main()
