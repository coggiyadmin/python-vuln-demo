"""Combination #9 — COMMENT / STRING-LITERAL × DESERIALIZE (CWE-502, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    s = request.args.get("s", "")
    # pickle.loads(base64.b64decode(s))
    example = "pickle.loads(s)"
    return str(len(example) + len(s))

