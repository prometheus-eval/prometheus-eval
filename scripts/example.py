from prometheus_eval import PrometheusEval

judge = PrometheusEval(model_id="prometheus-eval/prometheus-7b-v2.0", download_dir="/mnt/sda/juyoung/.cache")

instruction = "What are the key components of a neural network?"
response_A = "Neurons, weights, and activation functions are the key components."
response_B = "Layers, nodes, and input data are the main components."
rubric = "Are the components accurately identified?"
reference_answer = "Neurons, weights, and activation functions are fundamental to neural networks."

feedback, score = judge.single_relative_grade(
    instruction=instruction,
    response_A=response_A,
    response_B=response_B,
    rubric=rubric,
    reference_answer=reference_answer
)