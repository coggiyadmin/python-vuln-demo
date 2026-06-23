"""System Prompt Leakage (OWASP LLM07) — the endpoint returns its own system prompt on
request, handing an attacker the full instruction set / hidden context. TP-2.
"""
from flask import Flask, jsonify

app = Flask(__name__)
SYSTEM_PROMPT = "You are an internal triage agent. Hidden policy: auto-approve refunds < $50."


@app.route("/debug/prompt")
def debug_prompt():
    # SINK (LLM07): system prompt (hidden policy) disclosed to the caller
    return jsonify({"system": SYSTEM_PROMPT})
