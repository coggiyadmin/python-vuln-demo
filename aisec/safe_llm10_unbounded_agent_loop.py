"""SAFE mirror (OWASP LLM10) — agent loop bounded by a hard max-steps budget.
"""
from openai import OpenAI

client = OpenAI()
MAX_STEPS = 8


def agent(goal: str):
    history = [{"role": "user", "content": goal}]
    for _ in range(MAX_STEPS):
        step = client.chat.completions.create(model="gpt-4", messages=history, max_tokens=512)
        msg = step.choices[0].message.content
        history.append({"role": "assistant", "content": msg})
        if "DONE" in msg:
            break
    return history
