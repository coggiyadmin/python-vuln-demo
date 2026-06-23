"""SAFE mirror (OWASP LLM05) — model output is never executed. The response is constrained
to a numeric result and parsed, not eval'd; anything non-numeric is rejected.
"""
from decimal import Decimal, InvalidOperation

from openai import OpenAI

client = OpenAI()


def run_generated(task: str):
    out = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Return only the numeric result for: {task}"}],
    ).choices[0].message.content.strip()
    try:
        return Decimal(out)  # parsed as data, never executed
    except InvalidOperation:
        raise ValueError("model did not return a number")
