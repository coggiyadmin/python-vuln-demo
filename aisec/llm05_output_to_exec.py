"""Improper Output Handling (OWASP LLM05) — model output executed as code. The LLM's
response is passed to eval(), so a prompt-injected or hallucinated payload runs with full
process authority. TP-1.
"""
from openai import OpenAI

client = OpenAI()


def run_generated(task: str):
    code = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a python expression for: {task}"}],
    ).choices[0].message.content
    # SINK (LLM05): unvalidated model output executed as code
    return eval(code)
