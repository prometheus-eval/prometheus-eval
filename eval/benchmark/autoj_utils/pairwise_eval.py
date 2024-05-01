import argparse
import os
import random

from src.evaluation.benchmark.autoj_utils.utils_constants import *


def exchange_to_ori_label(exchanged_pred_label):
    assert exchanged_pred_label in [0, 1, 2]
    if exchanged_pred_label == 0:
        return 1
    elif exchanged_pred_label == 1:
        return 0
    else:
        return exchanged_pred_label


def check_res(
    gt_label,
    pred_label,
    pred_label_exchange,
):
    # assert pred_label in [0, 1, 2] and pred_label_exchange in [0, 1, 2, None]
    correct = [0, 0]
    agree = 0
    both_correct = 0
    if gt_label == pred_label:
        correct[0] = 1
    if gt_label == pred_label_exchange:
        correct[1] = 1
    if pred_label_exchange == pred_label:
        agree = 1
        if pred_label == gt_label:
            both_correct = 1
    return correct, agree, both_correct


def register_scenario_wise_results(
    scenario_wise_results,
    scenario,
    gt_label,
    pred_label,
    pred_label_exchange,
):
    if scenario not in scenario_wise_results:
        scenario_wise_results[scenario] = {
            "correct": 0,
            "correct_exchange": 0,
            "correct_both": 0,
            "total": 0,
            "exchange_dont_agree": 0,
        }
    scenario_wise_results[scenario]["total"] += 1
    if gt_label == pred_label:
        scenario_wise_results[scenario]["correct"] += 1
    if pred_label_exchange is not None:
        if gt_label == pred_label_exchange:
            scenario_wise_results[scenario]["correct_exchange"] += 1
        if pred_label_exchange == pred_label == gt_label:
            scenario_wise_results[scenario]["correct_both"] += 1
        if pred_label_exchange != pred_label:
            scenario_wise_results[scenario]["exchange_dont_agree"] += 1


def update_stat(stat, correct, agree, both_correct):
    stat["correct"][0] += correct[0]
    stat["correct"][1] += correct[1]
    stat["correct_both"] += both_correct
    stat["exchange_dont_agree"] += 1 - agree


def group_wise_collect(scenario_wise_results, type="single"):
    group_wise_results = {
        "Overall": {
            "correct": 0,
            "correct_exchange": 0,
            "correct_both": 0,
            "total": 0,
            "exchange_dont_agree": 0,
        },
    }
    for k, v in scenario_wise_results.items():
        group = reversed_scenario_group[k]
        if group not in group_wise_results:
            group_wise_results[group] = {
                "correct": 0,
                "correct_exchange": 0,
                "correct_both": 0,
                "total": 0,
                "exchange_dont_agree": 0,
            }
        # Ignore results other than "Overall" for single mode
        # for kk in group_wise_results[group]:
        #   group_wise_results[group][kk] += v[kk]
        for kk in group_wise_results["Overall"]:
            group_wise_results["Overall"][kk] += v[kk]

    # order = list(scenario_group.keys()) + ["Overall"]
    order = ["Overall"]

    results = {}

    for group_name in order:
        agreement = round(
            100
            * group_wise_results[group_name]["correct"]
            / float(group_wise_results[group_name]["total"]),
            2,
        )
        agreement_both = round(
            100
            * group_wise_results[group_name]["correct_both"]
            / float(group_wise_results[group_name]["total"]),
            2,
        )
        consistency = round(
            100
            * (
                1
                - group_wise_results[group_name]["exchange_dont_agree"]
                / float(group_wise_results[group_name]["total"])
            ),
            2,
        )
        real_agreement = agreement if type == "single" else agreement_both
        real_consistency = "-" if type == "single" else consistency
        results[group_name] = {
            "agreement": real_agreement,
            # "consistency": real_consistency,
        }
    return results


def do_one_abs(data):
    accepted_scores, rejected_scores = (
        data["prometheus_score"][0],
        data["prometheus_score"][1],
    )
    assert len(accepted_scores) == len(rejected_scores)
    # assert len(accepted_scores) == 5
    # mean_accepted_scores = statistics.mean(accepted_scores)
    # mean_rejected_scores = statistics.mean(rejected_scores)

    runs = min(len(accepted_scores), 3)

    if data["label"] != 2:
        for i in range(runs):
            if accepted_scores[i] is None or rejected_scores[i] is None:
                pass
            elif accepted_scores[i] > rejected_scores[i]:
                return data["label"]
                break
            elif accepted_scores[i] < rejected_scores[i]:
                return 1 - data["label"]
                break

            if i == (len(accepted_scores) - 1):
                return 1 - data["label"]
                break

    elif data["label"] == 2:
        if (
            accepted_scores[0] is not None
            and rejected_scores[0] is not None
            and accepted_scores[0] == rejected_scores[0]
        ):
            return data["label"]
        else:
            return random.choice([0, 1])
    return


def do_one_rel(data):
    alphabet_list = data["prometheus_score"]
    alphabet_list = [item.upper() for item in alphabet_list if item is not None]

    if True:
        for alphabet in alphabet_list:
            if alphabet not in ["A", "B", "TIE", None]:
                print(alphabet)
                import pdb

                pdb.set_trace()

    assert all(
        alphabet in {"A", "B", "TIE", None} for alphabet in alphabet_list
    ), "alphabet_list contains values other than 'A', 'B', or 'TIE'"

    counts = {
        alphabet: alphabet_list.count(alphabet) for alphabet in set(alphabet_list)
    }

    # max_alphabet = max(counts, key=counts.get)
    try:
        max_alphabet = alphabet_list[0]
    except:
        max_alphabet = None

    if data["label"] != 2:
        # If switch and label = 0. Correct answer is B
        # If switch and label = 1. Correct answer is A
        # If not switch and label = 0. Correct answer is A
        # If not switch and label = 1. Correct answer is B
        if data["is_switch"] == 1 and data["label"] == 0:
            if max_alphabet == "B":
                return data["label"]
            else:
                return 1 - data["label"]
        elif data["is_switch"] == 1 and data["label"] == 1:
            if max_alphabet == "A":
                return data["label"]
            else:
                return 1 - data["label"]
        elif data["is_switch"] == 0 and data["label"] == 0:
            if max_alphabet == "A":
                return data["label"]
            else:
                return 1 - data["label"]
        elif data["is_switch"] == 0 and data["label"] == 1:
            if max_alphabet == "B":
                return data["label"]
            else:
                return 1 - data["label"]
        else:
            assert 0
            return 1 - data["label"]
    elif data["label"] == 2:
        if max_alphabet == "TIE":
            return data["label"]
        # elif alphabet_list[0] != alphabet_list[1] and "TIE" not in alphabet_list[:2]:
        #     return data["label"]
        else:
            return random.choice([0, 1])
    return


def evaluate_autoj_performance(data: list, mode: str, skip_tie: bool = False):
    def preprocess_autoj_data(data: list, mode: str):
        labels = []
        preds = []
        do_one_func = do_one_abs if mode == "a2r" else do_one_rel
        for d in data:
            if skip_tie and d["label"] == 2:
                continue
            labels.append(d)
            preds.append(do_one_func(d))
        return labels, preds

    source, pred = preprocess_autoj_data(data, mode)

    # Assuming the existence of the required functions: read_jsonl, exchange_to_ori_label, check_res, update_stat, register_scenario_wise_results, group_wise_collect
    assert len(source) == len(pred)

    stat = {
        "not_resolve": [0, 0],  # for ori and exchange
        "correct": [0, 0],
        "correct_both": 0,
        "exchange_dont_agree": 0,
    }

    scenario_wise_results = {}

    for idx, (sourcedata, preddata) in enumerate(zip(source, pred)):
        gt_label = sourcedata["label"]  # 0,1,2
        pred_label = preddata  # 0,1,2
        pred_label_exchange = None
        correct, agree, both_correct = check_res(
            gt_label, pred_label, pred_label_exchange
        )
        update_stat(stat, correct, agree, both_correct)
        register_scenario_wise_results(
            scenario_wise_results,
            sourcedata["scenario"],
            gt_label,
            pred_label,
            pred_label_exchange,
        )

    results = group_wise_collect(scenario_wise_results, "single")

    # print("Group Name\tAgreement\tConsistency")
    # print("----------------------------")
    # for k, v in results.items():
    #     if k == "Overall":
    #         print("----------------------------")
    #     print(f"{k}\t{v['agreement']}\t-")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        type=str,
        default="pairwise",
        choices=["single", "pairwise"],
        help="single or pairwise",
    )
    parser.add_argument(
        "--pred_file_path",
        type=str,
        default="../../data/outputs/pairwise_example_output.jsonl",
        help="path to the prediction file",
    )
    parser.add_argument(
        "--exchange_pred_file_path",
        type=str,
        default="../../data/outputs/pairwise_exchange_example_output.jsonl",
        help="path to the prediction file on the `exchange-response-order` data",
    )
    parser.add_argument(
        "--source_file_path",
        type=str,
        default="../../data/test/testdata_pairwise.jsonl",
        help="path to the source file",
    )
    args = parser.parse_args()

    source = read_jsonl(args.source_file_path)
    pred = read_jsonl(args.pred_file_path)
    assert len(source) == len(pred)

    if args.type == "pairwise":
        assert args.exchange_pred_file_path is not None
        assert os.path.exists(args.exchange_pred_file_path)
        pred_exchange = read_jsonl(args.exchange_pred_file_path)
        assert len(source) == len(pred_exchange)
    else:
        pred_exchange = None

    stat = {
        "not_resolve": [0, 0],  # for ori and exchange
        "correct": [0, 0],
        "correct_both": 0,
        "exchange_dont_agree": 0,
    }

    scenario_wise_results = {}

    for idx, (sourcedata, preddata) in enumerate(zip(source, pred)):
        gt_label = sourcedata["label"]  # 0,1,2

        pred_label = preddata["output"]  # 0,1,2

        pred_label_exchange = (
            exchange_to_ori_label(pred_exchange[idx]["output"])
            if args.type == "pairwise"
            else None
        )

        correct, agree, both_correct = check_res(
            gt_label, pred_label, pred_label_exchange
        )

        update_stat(stat, correct, agree, both_correct)

        register_scenario_wise_results(
            scenario_wise_results,
            sourcedata["scenario"],
            gt_label,
            pred_label,
            pred_label_exchange,
        )

    results = group_wise_collect(scenario_wise_results, args.type)

    print("Group Name\tAgreement\tConsistency")
    print("----------------------------")
    for k, v in results.items():
        if k == "Overall":
            print("----------------------------")
        print(f"{k}\t{v['agreement']}\t-")
