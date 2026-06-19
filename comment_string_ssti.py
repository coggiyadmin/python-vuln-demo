"""Combination #9 — COMMENT / STRING-LITERAL × SSTI (CWE-1336, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("name", "")
    # render_template_string("<p>" + n + "</p>")
    example = "{{ " + n + " }}"
    return str(len(example))

