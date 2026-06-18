"""SAFE mirror — oop_openredirect.py; the tainted target is constrained to a
relative same-site path before redirect(). Expect 0 security findings."""
from urllib.parse import urlparse
from flask import Flask, request, redirect

app = Flask(__name__)


class Navigation:
    def __init__(self, url):
        self.url = url

    def _safe_dest(self):
        parts = urlparse(self.url)
        if parts.scheme or parts.netloc:        # reject absolute / cross-host URLs
            return "/"
        return "/" + parts.path.lstrip("/")

    def go_direct(self):
        return redirect(self._safe_dest())      # only same-site relative paths


@app.route("/login")
def login():
    nav = Navigation(request.args.get("next", ""))
    return nav.go_direct()
