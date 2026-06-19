"""Combination #11 — FAN-OUT × OPEN REDIRECT (CWE-601, Python)."""
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    redirect(n)  # sink 1 (unused response)
    redirect("https://a.example/" + n)  # sink 2
    return redirect("https://b.example/" + n)  # sink 3

