"""Unbounded Consumption (OWASP LLM10) — agent loop with no iteration cap. A model that
never emits the stop token (or an injected "keep going") spins forever, burning tokens/cost. TP-1.
"""
from openai import OpenAI

client = OpenAI()


def agent(goal: str):
    history = [{"role": "user", "content": goal}]
    while True:  # SINK (LLM10): no max-steps / no budget guard
        step = client.chat.completions.create(model="gpt-4", messages=history)
        msg = step.choices[0].message.content
        history.append({"role": "assistant", "content": msg})
        if "DONE" in msg:
            return history
