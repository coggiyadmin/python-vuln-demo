"""Combination #9 — COMMENT / STRING-LITERAL × NoSQL (CWE-943, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # coll.find({"$where": "this.user == '" + u + "'"})
    example = "$where: this.user == '" + u + "'"
    return str(len(example))

