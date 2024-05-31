# import huggingface_hub
# import os

# # load all files with .txt extension in `urial_prompts` folder.
# files = [file for file in os.listdir("urial_prompts") if file.endswith(".txt")]
# prompts_dict = {}
# for file in files:
#     file = file.split("/")[-1]
#     split_name = file.split(".")[0]
#     with open(f"urial_prompts/{file}") as f:
#         prompts_dict = {split_name: f.read()}


from datasets import load_dataset

split_name = "inst_help"
url = f"https://raw.githubusercontent.com/Re-Align/URIAL/main/urial_prompts/{split_name}.txt"
dataset = load_dataset(
    "text",
    data_files=url,
    split="train",
    sample_by="document",
)
print(dataset["text"][0])
