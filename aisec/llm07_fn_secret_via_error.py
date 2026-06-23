"""System Prompt Leakage FN probe (OWASP LLM07) — indirect leak via an error path. The
secret is not printed directly; it rides inside an exception/debug payload returned to the
user, so direct-string scanners MISS it. Expected: trust layer MISS.
"""
import os

from flask import Flask

app = Flask(__name__)


@app.route("/run")
def run():
    try:
        cfg = {"system": "triage agent", "key": os.environ["BILLING_API_KEY"]}
        raise RuntimeError(f"config dump: {cfg}")  # secret folded into the error
    except RuntimeError as e:
        # SINK (LLM07 indirect): error string (carrying the secret) echoed to the client
        return str(e), 500
