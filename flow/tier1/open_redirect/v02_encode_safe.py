# Phase-3 encode mirror
from flask import Flask, request, redirect, abort
app = Flask(__name__)
ALLOWED = {"/dashboard", "/profile", "/settings"}
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    if nxt not in ALLOWED:
        abort(403)
    return redirect(nxt)
