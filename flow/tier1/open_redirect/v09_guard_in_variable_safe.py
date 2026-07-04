# v09 guard-in-variable — host allowlist in module frozenset.
from urllib.parse import urlparse
from flask import Flask, request, redirect

ALLOWED_HOSTS = frozenset({"app.example.com", "cdn.example.com"})
app = Flask(__name__)

@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    host = urlparse(nxt).netloc.split(":")[0]
    if host in ALLOWED_HOSTS:
        return redirect(nxt)
    return redirect("/home")
