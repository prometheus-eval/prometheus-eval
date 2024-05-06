import argparse
import json
import logging
import os

from accelerate.state import PartialState
from huggingface_hub import HfApi

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def push_to_hub(target_model_path, repo_id, hf_token):
    if PartialState().process_index == 0:
        logger.info("Pushing model to hub...")
        if os.path.exists(f"{target_model_path}/training_params.json"):
            training_params = json.load(
                open(f"{target_model_path}/training_params.json")
            )
            # Optionally, remove sensitive info if needed
            # training_params.pop("token")
            json.dump(
                training_params, open(f"{target_model_path}/training_params.json", "w")
            )

        api = HfApi(token=hf_token)
        api.create_repo(repo_id=repo_id, repo_type="model", private=True, exist_ok=True)
        api.upload_folder(
            folder_path=target_model_path, repo_id=repo_id, repo_type="model"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Push model to Hugging Face Hub")
    parser.add_argument(
        "--target_model_path", required=True, help="Local path to the model directory"
    )
    parser.add_argument(
        "--repo_id", required=True, help="Hugging Face Hub repository ID"
    )
    parser.add_argument(
        "--hf_token", required=True, help="Hugging Face authentication token"
    )

    args = parser.parse_args()

    push_to_hub(
        target_model_path=args.target_model_path,
        repo_id=args.repo_id,
        hf_token=args.hf_token,
    )
