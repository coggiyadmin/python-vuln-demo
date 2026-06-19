"""Combination #9 — COMMENT / STRING-LITERAL × PATH TRAVERSAL (CWE-22, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    name = request.args.get("name", "")
    # open("/data/" + name)  # commented
    example = "open('/data/' + name)"
    return str(len(example) + len(name))

