"""Unbounded Consumption FN probe (OWASP LLM10) — recursive tool. A tool the model can call
itself re-invokes the model, so one request fans out into an unbounded call tree. No explicit
loop appears at the call site, so loop-shape scanners MISS it. Expected: trust layer MISS.
"""
from openai import OpenAI

client = OpenAI()


def expand_tool(topic: str) -> str:
    sub = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"List sub-topics of {topic}, then expand each."}],
    ).choices[0].message.content
    # SINK (LLM10 recursive): each sub-topic re-enters the model with no depth budget
    for line in sub.splitlines():
        if line.strip():
            expand_tool(line.strip())
    return sub
