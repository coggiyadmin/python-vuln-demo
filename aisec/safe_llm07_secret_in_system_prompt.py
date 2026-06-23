"""SAFE mirror (OWASP LLM07) — no secret in the prompt. The key stays server-side and is
used only to authorize a tool call; the model never sees it.
"""
import os

from openai import OpenAI

client = OpenAI()
_KEY = os.environ.get("BILLING_API_KEY", "")  # used by tools, never placed in a prompt


def build_agent():
    system = "You are billing-bot. Use the authorized billing tool for balances."
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "system", "content": system}])
