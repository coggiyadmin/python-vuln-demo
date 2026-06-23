"""TN — benign single bounded model call; capped tokens, one shot, no loop.
"""
from openai import OpenAI

client = OpenAI()


def answer(question: str):
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": question}], max_tokens=256)
