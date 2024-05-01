
## Prerequisites

- Python 3.11 or newer
- Poetry for Python dependency management

## Installation

To set up the project environment and install the required dependencies, follow these steps:

1. **Install Poetry:**
   Ensure that Poetry is installed on your system. If not, you can install it with the following command:

   ```bash
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

2. **Clone the repository:**
   Clone the source code from the repository.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install dependencies:**
   Use Poetry to install the project dependencies.

   ```bash
   poetry install
   ```

## Usage

To run the model evaluation, use the following command:

```bash
poetry run python -m src.evluation.run_evaluate --model_name <model-name> --eval_data_names <data-names> [OPTIONS]
```

### Command Line Arguments

- `--model_name` (required): The name of the model to evaluate. Example: `"kaist-ai/prometheus-7b-v1.5-beta-3"`.
- `--eval_data_names` (required): Space-separated list of evaluation data names. Example: `"hhh_alignment_eval vicuna_eval"`.
- `--rerun` (optional): Flag to force rerun of evaluations even if output files exist.

### Examples

1. **Run a basic evaluation:**

   ```bash
   poetry run python -m src.evluation.run_evaluate --model_name "prometheus-eval/prometheus-7b-v2.0" --eval_data_names "eval_data1 eval_data2"
   ```

2. **Force rerun of evaluation:**

   ```bash
   poetry run python -m src.evluation.run_evaluate --model_name "prometheus-eval/prometheus-7b-v2.0" --eval_data_names "eval_data1 eval_data2" --rerun
   ```

## Development

- Set the `DEBUG` flag in the script to `True` for a verbose output during development.
- Adjust `num_gpus` based on the model size and the available GPU resources.
