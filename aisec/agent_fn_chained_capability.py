"""Excessive Agency FN probe (OWASP LLM06) — capability composition. Two tools are
each individually safe-looking (one reads a file, one posts text), but the agent can
chain read->post to exfiltrate any readable file. No single tool is the obvious sink;
the unsafe capability emerges from composition. Expected: trust layer MISS.
"""
import requests


def read_note(path: str) -> str:
    # "scoped" read tool — looks benign in isolation
    return open(path, encoding="utf-8").read()


def post_message(channel: str, text: str) -> None:
    # "scoped" post tool — looks benign in isolation
    requests.post(f"https://chat.example.com/{channel}", json={"text": text})


# SINK (LLM06 chained): read_note(secret) -> post_message(public, secret) exfiltrates.
TOOLS = [{"name": "read_note", "fn": read_note}, {"name": "post_message", "fn": post_message}]
