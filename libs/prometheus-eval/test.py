from prometheus_eval import PrometheusEval

judge = PrometheusEval(dtype="float16")

import pdb

pdb.set_trace()

data = [
    {
        "instruction": "What are the key components of a neural network?",
        "response_A": "Neurons, weights, and activation functions are the key components.",
        "response_B": "Layers, nodes, and input data are the main components.",
    }
]
rubric = "Are the components accurately identified?"
reference_answers = [
    "Neurons, weights, and activation functions are fundamental to neural networks.",
    "Layers, nodes, and input data are essential parts of neural network architecture.",
]

feedbacks, scores = judge.relative_grade(
    data=data, rubric=rubric, reference_answers=reference_answers, params={}
)
