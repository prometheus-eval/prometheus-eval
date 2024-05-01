# prometheus_eval/__init__.py

from .judge import PrometheusEval
from .prompts import (
    ABSOLUTE_PROMPT,
    ABSOLUTE_PROMPT_WO_REF,
    RELATIVE_PROMPT,
    RELATIVE_PROMPT_WO_REF,
    get_prompt_template,
    load_rubric,
)
