"""Combination #9 — COMMENT / STRING-LITERAL × XPATH (CWE-643, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("name", "")
    # TREE.xpath("//user[name='" + n + "']")
    example = "//user[name='" + n + "']"
    return str(len(example))

