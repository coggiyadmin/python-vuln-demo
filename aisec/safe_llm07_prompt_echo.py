"""SAFE mirror (OWASP LLM07) — the system prompt is never disclosed; the debug route
returns only a non-sensitive status.
"""
from flask import Flask, jsonify

app = Flask(__name__)
SYSTEM_PROMPT = "You are an internal triage agent. Hidden policy: auto-approve refunds < $50."


@app.route("/debug/prompt")
def debug_prompt():
    return jsonify({"status": "ok"})  # prompt withheld
