"""TN — redirect with host allowlist."""
from urllib.parse import urlparse
from flask import Flask, request, redirect
ALLOWED = frozenset({"app.example.com"})
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    if urlparse(nxt).netloc.split(":")[0] in ALLOWED:
        return redirect(nxt)
    return redirect("/home")
