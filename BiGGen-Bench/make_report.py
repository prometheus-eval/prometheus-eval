import argparse
import json

from rich import box
from rich.console import Console
from rich.table import Table


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def main(args):
    console = Console()

    feedback_file_path = args.feedback_file_path
    feedback_data = read_json(feedback_file_path)
    feedback_data_list = list(feedback_data.values())

    scores = {
        "grounding": [],
        "instruction_following": [],
        "planning": [],
        "reasoning": [],
        "refinement": [],
        "safety": [],
        "theory_of_mind": [],
        "tool_usage": [],
        "multilingual": [],
    }

    response_model = feedback_data_list[0]["response_model_name"]
    eval_model = feedback_data_list[0]["eval_model_name"]

    for _, instance in feedback_data.items():
        capability = instance["capability"]
        scores[capability].append(instance["score"])

    # Initialize table for output
    table = Table(
        title=f"Performance Report for {response_model} graded by {eval_model}",
        box=box.ROUNDED,
    )
    table.add_column("Capability", justify="left", style="cyan", no_wrap=True)
    table.add_column("Average Score", justify="right", style="green")

    for capability, score_list in scores.items():
        average_score = sum(score_list) / len(score_list) if score_list else None
        if average_score is not None:
            table.add_row(capability, f"{average_score:.3f}")
        else:
            table.add_row(capability, "N/A")

    all_scores = [
        sum(score_list) / len(score_list)
        for score_list in scores.values()
        if score_list
    ]
    overall_average = sum(all_scores) / len(all_scores) if all_scores else 0
    table.add_row("Overall", f"{overall_average:.3f}", style="bold red")

    console.print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score the model")
    parser.add_argument(
        "--feedback_file_path",
        type=str,
        required=True,
        help="Path to the feedback file",
    )

    args = parser.parse_args()
    main(args)
