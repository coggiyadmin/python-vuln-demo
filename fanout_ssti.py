"""Combination #11 — FAN-OUT × SSTI (CWE-1336, Python)."""
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    render_template_string("<p>" + n + "</p>")
    render_template_string("<h1>" + n + "</h1>")
    render_template_string("{% set x = '" + n + "' %}{{ x }}")

