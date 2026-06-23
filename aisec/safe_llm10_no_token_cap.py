"""SAFE mirror (OWASP LLM10) — input length is capped and max_tokens is bounded.
"""
from openai import OpenAI

client = OpenAI()
MAX_INPUT = 8000


def summarize(user_text: str):
    if len(user_text) > MAX_INPUT:
        raise ValueError("input too large")
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": user_text}], max_tokens=512)
