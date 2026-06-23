"""SAFE mirror (OWASP LLM05) — model output HTML-escaped before rendering, so markup in the
response is shown as text, never executed.
"""
from html import escape

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
    return f"<div class='answer'>{escape(answer)}</div>"
