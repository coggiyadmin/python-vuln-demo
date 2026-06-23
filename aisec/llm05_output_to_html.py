"""Improper Output Handling (OWASP LLM05) — model output rendered as raw HTML. The LLM
response is returned in an HTML response without escaping, so model-produced markup/script
(e.g. via indirect injection) executes in the victim's browser (stored/reflected XSS). TP-3.
"""
from flask import Flask, request

from openai import OpenAI

app = Flask(__name__)
client = OpenAI()


@app.route("/ask")
def ask():
    answer = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": request.args.get("q", "")}],
    ).choices[0].message.content
    # SINK (LLM05 -> XSS): model output injected into HTML unescaped
    return f"<div class='answer'>{answer}</div>"
