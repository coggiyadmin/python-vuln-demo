"""TN — benign system prompt assembly; constant, non-sensitive instruction, no secret,
no disclosure route.
"""


def system_prompt() -> str:
    return "You are a helpful assistant. Be concise and cite sources."
