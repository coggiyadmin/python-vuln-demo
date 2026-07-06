"""Agent (LLM01 indirect prompt injection, part 2 of 2).

The page fetched by retriever.py is concatenated into the SYSTEM prompt with instruction
authority, so attacker text embedded in that page steers the model. The source (retriever.fetch)
and the sink (system-role injection) live in different files — the flow is only visible when the
directory is scanned as a tree.
"""
from openai import OpenAI

from retriever import fetch

client = OpenAI()


def summarize(url: str) -> str:
    page = fetch(url)
    # SINK: retrieved untrusted content given instruction authority in the system role.
    prompt = "Summarize and follow any directives in the following page:\n" + page
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "system", "content": prompt}]
    ).choices[0].message.content
