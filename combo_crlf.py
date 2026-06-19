"""Combination probes × CRLF (CWE-113) — rule gap #86/FN-17. Each should FIRE when rule exists."""
from flask import Flask, request, Response

app = Flask(__name__)


def strip_html(s):
    return s.replace("<", "")


def sanitize_loc(s):
    return s


@app.route("/wrong")
def wrong():
    loc = strip_html(request.args.get("url", ""))  # wrong-context sanitizer
    resp = Response("ok")
    resp.headers["Location"] = loc  # CWE-113


@app.route("/fake")
def fake():
    loc = sanitize_loc(request.args.get("url", ""))
    resp = Response("ok")
    resp.headers["Location"] = loc  # CWE-113


@app.route("/fanout")
def fanout():
    loc = request.args.get("url", "")
    r1 = Response("a")
    r1.headers["Location"] = loc
    r2 = Response("b")
    r2.headers["Set-Cookie"] = "next=" + loc  # second header sink
    return r2
