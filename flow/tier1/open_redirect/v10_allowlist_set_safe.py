# v10 allowlist-set — path prefix tuple gate before redirect.
from flask import Flask, request, redirect

ALLOWED_PREFIXES = ("https://app.example.com/", "https://cdn.example.com/")

app = Flask(__name__)

@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    if nxt.startswith(ALLOWED_PREFIXES):
        return redirect(nxt)
    return redirect("/home")
