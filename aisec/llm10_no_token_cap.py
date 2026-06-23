"""Unbounded Consumption (OWASP LLM10) — no token cap on a user-driven completion. The
caller controls prompt size and there is no max_tokens, so a large input drives unbounded
output cost. TP-2.
"""
from openai import OpenAI

client = OpenAI()


def summarize(user_text: str):
    # SINK (LLM10): unbounded input, no max_tokens / no length guard
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": user_text}])
