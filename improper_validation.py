"""CWE-1173 — Improper Use of Validation Framework. The validator is invoked but its result
is discarded, so invalid input proceeds. Real vuln; NO finding = FALSE NEGATIVE."""
import re
from flask import Flask, request

app = Flask(__name__)
EMAIL = re.compile(r"^[^@]+@[^@]+\.[^@]+$")


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email", "")
    EMAIL.match(email)                     # validation result IGNORED → CWE-1173
    save_subscriber(email)                 # proceeds with unvalidated input
    return "ok"


def save_subscriber(_email):
    pass
