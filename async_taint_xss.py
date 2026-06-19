"""Combination #4 — ASYNC × XSS (CWE-79, Python)."""
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request

app = Flask(__name__)
pool = ThreadPoolExecutor(1)


def render(q):
    return "<p>" + q + "</p>"  # CWE-79


@app.route("/async")
def async_xss():
    q = request.args.get("q", "")
    fut = pool.submit(render, q)
    return fut.result()
