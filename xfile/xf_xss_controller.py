"""Combination #1 — CROSS-FILE × XSS (CWE-79, Python). Controller passes tainted
value to helper; no finding on controller = FN (#74/#106)."""
from flask import Flask, request
from xfile.xf_xss_helper import render_title

app = Flask(__name__)


@app.route("/page")
def page():
    q = request.args.get("q", "")  # SOURCE
    return render_title(q)  # sink in helper
