"""TN — benign output rendering. Formats a fixed, app-authored result string; no model
output, no dynamic sink. The noise-floor baseline for the LLM05 family.
"""


def render_summary(count: int, total: float) -> str:
    return f"Processed {count} items totalling {total:.2f}."
