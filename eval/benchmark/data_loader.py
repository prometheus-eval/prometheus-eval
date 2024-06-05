import json
import os
import random

from src.evaluation.prompts import ABSOLUTE_PROMPT, AUTOJ_COARSE_SCORE_RUBRIC
from src.evaluation.utils import extract_sections


class EvalDataLoader:
    # List of allowed filenames
    ALLOWED_FILES = [
        "feedback_collection_ood_test.json",
        "feedback_collection_test.json",
        "preference_collection_ood_test.json",
        "flask_eval.json",
        "hhh_alignment_eval.json",
        "mt_bench_eval.json",
        "mt_bench_human_judgement_eval.json",
        "vicuna_eval.json",
        "autoj_pairwise.json",
        "alpaca_eval.json",
    ]

    def __init__(self, data_name):
        """
        Initializes the EvalDataLoader with the name of the data file (without extension).

        :param data_name: The name of the data file to load (without '.json').
        """
        # Construct the filename by appending '.json' extension
        filename = f"{data_name}.json"

        # Check if the constructed filename is in the list of allowed files
        if filename not in self.ALLOWED_FILES:
            raise ValueError(
                f"Filename '{filename}' is not allowed. Please choose from the allowed list."
            )

        # Use __file__ to determine the directory of the current script and construct the absolute path
        self.data_name = data_name
        script_dir = os.path.dirname(__file__)
        self.data_path = os.path.join(script_dir, "data")
        self.file_path = os.path.join(
            script_dir, "data", filename
        )  # Assuming the files are in a 'data' subdirectory
        self.records = []

    def _read_records(self):
        """
        Reads and parses JSON objects from the file. Supports both a single JSON object/array
        for the entire file and one JSON object per line.
        """
        try:
            with open(self.file_path, "r") as file:
                # Attempt to load the entire file content as a single JSON object/array
                try:
                    self.records = json.load(file)
                except json.JSONDecodeError:
                    # If the above fails, revert to reading the file line by line
                    file.seek(0)  # Reset file pointer to the beginning
                    self.records = [json.loads(line) for line in file if line.strip()]
            print(
                f"Successfully loaded {len(self.records)} records from {self.file_path}."
            )
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from the file '{self.file_path}': {e}")

    def _parse_records(self):
        """
        Augments each record with additional key-values extracted from the 'instruction' field using the extract_sections function.
        """
        if self.data_name in [
            "flask_eval",
            "mt_bench_eval",
            "vicuna_eval",
            "feedback_collection_ood_test",
        ]:
            for record in self.records:
                if (
                    isinstance(record, dict) and "instruction" in record
                ):  # Check if the record is the expected format
                    record["instruction"] = record["instruction"].strip().rstrip('",')
                    extracted_sections = extract_sections(record["instruction"])
                    record.update(extracted_sections)

        elif self.data_name in [
            "hhh_alignment_eval",
            "mt_bench_human_judgement_eval",
            "alpaca_eval",
            "preference_collection_ood_test",
        ]:
            for record in self.records:
                # Clean up the instruction field
                record["chosen_instruction"] = (
                    record["chosen_instruction"].strip().rstrip('",')
                )
                record["rejected_instruction"] = (
                    record["rejected_instruction"].strip().rstrip('",')
                )

                chosen_sections = extract_sections(record["chosen_instruction"])
                rejected_sections = extract_sections(record["rejected_instruction"])

                # Assert that all extracted sections except 'orig_response' are equal
                for key in chosen_sections:
                    if key != "orig_response":
                        assert (
                            chosen_sections[key] == rejected_sections[key]
                        ), f"Mismatch found in section '{key}' between chosen and rejected instructions."

                # Randomly assign the chosen and rejected instructions to A and B
                chosen_label = random.choice(["A", "B"])
                rejected_label = "B" if chosen_label == "A" else "A"
                record["chosen"] = chosen_label

                if "tie" in record.keys():
                    if record["tie"] == 1:
                        record["chosen"] = "tie"
                else:
                    record["tie"] = 0

                record[f"orig_response_{chosen_label}"] = chosen_sections.get(
                    "orig_response", ""
                )
                record[f"orig_response_{rejected_label}"] = rejected_sections.get(
                    "orig_response", ""
                )

                for key, value in chosen_sections.items():
                    if key != "orig_response":
                        record[key] = value

        elif self.data_name in ["autoj_pairwise"]:
            for record in self.records:
                record["orig_instruction"] = record.pop("prompt")
                record[
                    "score_rubric"
                ] = AUTOJ_COARSE_SCORE_RUBRIC  # Use the predefined score rubric

                if record["label"] == 0:
                    record["chosen_instruction"] = ABSOLUTE_PROMPT.format(
                        orig_instruction=record["orig_instruction"],
                        orig_response=record["response 1"],
                        score_rubric=record["score_rubric"],
                    )
                    record["rejected_instruction"] = ABSOLUTE_PROMPT.format(
                        orig_instruction=record["orig_instruction"],
                        orig_response=record["response 2"],
                        score_rubric=record["score_rubric"],
                    )
                else:
                    record["chosen_instruction"] = ABSOLUTE_PROMPT.format(
                        orig_instruction=record["orig_instruction"],
                        orig_response=record["response 2"],
                        score_rubric=record["score_rubric"],
                    )
                    record["rejected_instruction"] = ABSOLUTE_PROMPT.format(
                        orig_instruction=record["orig_instruction"],
                        orig_response=record["response 1"],
                        score_rubric=record["score_rubric"],
                    )

                # Avoid positional bias by randomly switching the order of the responses
                is_switch = random.choice([1, 0])
                record["is_switch"] = is_switch

                if is_switch:
                    record["orig_response_A"] = record["response 2"].strip()
                    record["orig_response_B"] = record["response 1"].strip()
                else:
                    record["orig_response_A"] = record["response 1"].strip()
                    record["orig_response_B"] = record["response 2"].strip()

                if record["label"] == 2:
                    record["chosen"] = "tie"
                    record["tie"] = 1
                else:
                    record["tie"] = 0
                    assert record["label"] in [
                        0,
                        1,
                    ], f"Invalid label: {record['label']} for record: {record}"

                # If switch and label = 0. Correct answer is B
                # If switch and label = 1. Correct answer is A
                # If not switch and label = 0. Correct answer is A
                # If not switch and label = 1. Correct answer is B
                if is_switch == 1 and record["label"] == 0:
                    record["chosen"] = "B"
                elif is_switch == 1 and record["label"] == 1:
                    record["chosen"] = "A"
                elif is_switch == 0 and record["label"] == 0:
                    record["chosen"] = "A"
                elif is_switch == 0 and record["label"] == 1:
                    record["chosen"] = "B"

        else:
            raise NotImplementedError(
                "Parsing records for this data is not implemented yet."
            )

    def get_records(self):
        """
        Returns the list of parsed JSON records.

        :return: A list of dictionaries, each representing a JSON object.
        """
        self._read_records()
        self._parse_records()
        return self.records


if __name__ == "__main__":
    file_names = [
        "feedback_collection_ood_test",
        "preference_collection_ood_test",
        "flask_eval",
        "mt_bench_eval",
        "hhh_alignment_eval",
        "mt_bench_human_judgement_eval",
        "vicuna_eval",
        "alpaca_eval",
        "autoj_pairwise",
    ]

    for file_name in file_names:
        print(f"Loading records from {file_name}")
        loader = EvalDataLoader(file_name)
        records = loader.get_records()

        record = records[0]

        if records:
            print(f"Keys of the first record in {file_name}: {records[0].keys()}\n")
        else:
            print(f"No records found in {file_name}\n")

        # import pdb; pdb.set_trace()
