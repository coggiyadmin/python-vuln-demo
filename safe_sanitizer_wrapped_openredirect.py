"""c08 SAFE — custom wrapper × open redirect (CWE-601). Expect clean."""
from flask import Flask, request, redirect, abort

app = Flask(__name__)
ALLOWED = {"/home", "/dashboard"}


@app.route("/wrapped")
def wrapped():
    nxt = request.args.get("next", "")
    if nxt not in ALLOWED:
        abort(403)
    return redirect(nxt)
