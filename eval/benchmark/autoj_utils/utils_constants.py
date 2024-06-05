import json
import os
from typing import Union

from tqdm import tqdm

scenario_group = {
    "Summarization": ["post_summarization", "text_summarization", "note_summarization"],
    "Exam Questions": [
        "math_reasoning",
        "solving_exam_question_with_math",
        "solving_exam_question_without_math",
    ],
    "Code": [
        "code_simplification",
        "code_generation",
        "explaining_code",
        "code_correction_rewriting",
        "code_to_code_translation",
    ],
    "Rewriting": [
        "text_simplification",
        "language_polishing",
        "instructional_rewriting",
        "text_correction",
        "paraphrasing",
    ],
    "Creative Writing": [
        "writing_song_lyrics",
        "writing_social_media_post",
        "writing_blog_post",
        "writing_personal_essay",
        "creative_writing",
        "writing_advertisement",
        "writing_marketing_materials",
        "writing_presentation_script",
        "counterfactual",
    ],
    "Functional Writing": [
        "writing_product_description",
        "writing_job_application",
        "writing_news_article",
        "writing_biography",
        "writing_email",
        "writing_legal_document",
        "writing_technical_document",
        "writing_scientific_paper",
        "functional_writing",
        "writing_cooking_recipe",
    ],
    "General Communication": [
        "asking_how_to_question",
        "open_question",
        "analyzing_general",
        "explaining_general",
        "seeking_advice",
        "recommendation",
        "value_judgement",
        "verifying_fact",
        "chitchat",
        "roleplay",
        "planning",
        "brainstorming",
    ],
    "NLP Tasks": [
        "ranking",
        "text_to_text_translation",
        "data_analysis",
        "classification_identification",
        "title_generation",
        "question_generation",
        "reading_comprehension",
        "keywords_extraction",
        "information_extraction",
        "topic_modeling",
        "others",
    ],
}


critique_eval_prompt = """You are a helpful and precise assistant for checking the quality of the feedback.
Two pieces of feedback have been provided for the same response to a particular query. Which one is better with regard to their correctness, comprehensiveness, and specificity to the query?

[BEGIN DATA]
***
[Query]: {prompt}
***
[Response]: {response}
***
[Feedback 1]: {feedback1}
***
[Feedback 2]: {feedback2}
***
[END DATA]

Please choose from the following options, and give out your reason in the next line. 
A: Feedback 1 is significantly better.
B: Feedback 2 is significantly better.
C: Neither is significantly better."""

zh_critique_eval_prompt = """你是一个乐于助人且回答准确的助手，将要来评估反馈的质量。
我向你提供了两条针对特定用户问询的相同回答的反馈。就它们的正确性、全面性和与问询的相关性而言，哪一条更好？

[BEGIN DATA]
***
[用户问询]: {prompt}
***
[回应]: {response}
***
[反馈1]: {feedback1}
***
[反馈2]: {feedback2}
***
[END DATA]

请在以下选项中做出选择，并在这之后的一行给出你的理由
A:反馈1明显更好
B:反馈2明显更好
C:并没有哪条反馈明显更好"""


reversed_scenario_group = {vv: k for k, v in scenario_group.items() for vv in v}


def elegant_show(something, level=0, sid=0, full=False):
    # str,float,int
    # all print in this call should add level*4 spaces
    prefix = "\t" * level

    if isinstance(something, (str, float, int)) or something is None:
        if isinstance(something, str):
            # if '\n' in something:
            #     something = '\n'+something
            # add prefix whenever go to a new line in this string
            something = something.replace("\n", f"\n{prefix}")
        print(prefix, f"\033[1;35mElement: \033[0m", something)
    elif isinstance(something, list) or isinstance(something, tuple):
        # take a random example, and length
        # sid = 0
        if len(something) == 0:
            print(
                prefix,
                f"\033[1;33mLen: \033[0m{len(something)} \t\033[1;33m& No elements! \033[0m",
            )
        elif not full or len(something) == 1:
            print(
                prefix,
                f"\033[1;33mLen: \033[0m{len(something)} \t\033[1;33m& first element ...\033[0m",
            )
            elegant_show(something[sid], level + 1, sid, full)
        else:
            print(
                prefix,
                f"\033[1;33mLen: \033[0m{len(something)} \t\033[1;33m& Elements ...\033[0m",
            )
            for i in range(len(something) - 1):
                elegant_show(something[i], level + 1, sid, full)
                print(
                    prefix + "\t", f"\033[1;33m-------------------------------\033[0m"
                )
            elegant_show(something[-1], level + 1, sid, full)

    elif isinstance(something, dict):
        for k, v in something.items():
            print(prefix, f"\033[1;34mKey: \033[0m{k} \033[1;34m...\033[0m")
            elegant_show(v, level + 1, sid, full)
    else:
        print(prefix, f"\033[1;31mError @ Type: \033[0m{type(something)}")
        raise NotImplementedError


def read_jsonl(jsonl_file_path):
    s = []
    with open(jsonl_file_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        linex = line.strip()
        if linex == "":
            continue
        s.append(json.loads(linex))
    return s


def write_jsonl(data, jsonl_file_path, mode="w"):
    # data is a list, each of the item is json-serilizable
    assert isinstance(data, list)
    if not os.path.exists(os.path.dirname(jsonl_file_path)):
        os.makedirs(os.path.dirname(jsonl_file_path))
    with open(jsonl_file_path, mode) as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
