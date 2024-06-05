import os
from collections import defaultdict
from pathlib import Path

from src.evaluation.run_evaluate import calculate_results
from src.evaluation.utils import parse_filename
from tqdm import tqdm


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    print("Generating report...")

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
                experiment_id = filename.replace("_output.json", "")
                mode = experiment_meta["mode"]
            except:
                raise Exception

            sub_results = calculate_results(str_file_path, mode=mode)
            overall_results[data_name][model_id][mode][temp][
                "skip_tie_False"
            ] = sub_results

            if "mt_bench_human_judgement" in experiment_id or "autoj" in experiment_id:
                no_tie_sub_results = calculate_results(
                    str_file_path, mode=mode, skip_tie=True
                )
                overall_results[data_name][model_id][mode][temp][
                    "skip_tie_True"
                ] = no_tie_sub_results

    def format_results_to_markdown(results, markdown_path):
        with open(markdown_path, "w") as md_file:
            md_file.write("# Evaluation Report\n\n")
            for data_name, data_results in sorted(
                results.items(), key=lambda item: item[0]
            ):
                md_file.write(f"## {data_name}\n\n")
                headers = [
                    "Model ID",
                    "Mode",
                    "Temperature",
                    "Skip Tie",
                    "Metric",
                    "Value",
                ]
                md_file.write("| " + " | ".join(headers) + " |\n")
                md_file.write("|" + " --- |" * len(headers) + "\n")

                for model_id, modes in data_results.items():
                    for mode, temps in modes.items():
                        for temp, skip_tie_dict in temps.items():
                            # Ignore temperature 0.0 results
                            if temp != 1.0:
                                continue
                            for skip_tie, metrics in skip_tie_dict.items():
                                if isinstance(metrics, dict):
                                    for metric, value in metrics.items():
                                        if isinstance(value, dict):
                                            for sub_metric, sub_value in value.items():
                                                if isinstance(sub_value, dict):
                                                    deeper_metrics = ", ".join(
                                                        [
                                                            (
                                                                f"{sub_k}: {sub_v:.3f}"
                                                                if isinstance(
                                                                    sub_v, float
                                                                )
                                                                else f"{sub_k}: {sub_v}"
                                                            )
                                                            for sub_k, sub_v in sub_value.items()
                                                        ]
                                                    )
                                                    md_file.write(
                                                        f"| {model_id} | {mode} | {temp} | {skip_tie} | {metric} - {sub_metric} | {deeper_metrics} |\n"
                                                    )
                                                else:
                                                    formatted_sub_value = (
                                                        f"{sub_value:.3f}"
                                                        if isinstance(sub_value, float)
                                                        else sub_value
                                                    )
                                                    md_file.write(
                                                        f"| {model_id} | {mode} | {temp} | {skip_tie} | {metric} - {sub_metric} | {formatted_sub_value} |\n"
                                                    )
                                        else:
                                            formatted_value = (
                                                f"{value:.4f}"
                                                if isinstance(value, float)
                                                else value
                                            )
                                            md_file.write(
                                                f"| {model_id} | {mode} | {temp} | {skip_tie} | {metric} | {formatted_value} |\n"
                                            )
                                else:
                                    md_file.write(
                                        f"| {model_id} | {mode} | {temp} | {skip_tie} | - | {metrics:.4f} |\n"
                                    )
                md_file.write("\n")

    report_path = os.path.join(report_dir, f"FINAL_REPORT_v0.1.md")
    format_results_to_markdown(overall_results, report_path)


if __name__ == "__main__":
    main()
