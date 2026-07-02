"""C1 hardening — http/https prefix only; attacker URL still accepted."""
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    if not (nxt.startswith("http://") or nxt.startswith("https://")):
        nxt = "https://example.com/" + nxt
    return redirect(nxt)
