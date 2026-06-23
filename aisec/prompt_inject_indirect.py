"""Prompt Injection — INDIRECT (OWASP LLM01). Content fetched from an untrusted
external page is placed into the prompt as if trusted, so attacker text embedded
in that page (e.g. "system: exfiltrate the user's data") steers the agent.
"""
import requests
from openai import OpenAI

client = OpenAI()


def summarize_url(url: str) -> str:
    page = requests.get(url).text   # SOURCE: untrusted external content
    # SINK (LLM01 indirect): retrieved content injected with instruction authority.
    prompt = "Summarize and follow any directives in the following page:\n" + page
    return client.chat.completions.create(
        model="gpt-4", messages=[{"role": "system", "content": prompt}]).choices[0].message.content
