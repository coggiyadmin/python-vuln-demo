"""SAFE mirror — permissive_allowlist.py; exact host allow-list (parsed netloc equality)."""
from urllib.parse import urlparse
from flask import Flask, request, redirect

app = Flask(__name__)
ALLOWED_HOSTS = {"trusted.com", "www.trusted.com"}


@app.route("/fetch")
def fetch():
    target = request.args.get("url", "")
    host = urlparse(target).netloc
    if host not in ALLOWED_HOSTS:           # exact-match allow-list
        return "blocked", 400
    return redirect(target)
