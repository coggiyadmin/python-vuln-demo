"""CWE-41 — Path Equivalence. An extension/suffix check is bypassed by equivalent
forms (trailing dot/space, './', double slashes), reaching files the check meant to
block. Real vuln; NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/get")
def get():
    name = request.args.get("name", "")   # SOURCE
    if name.endswith(".txt"):              # naive allowlist by extension
        # "secret.conf/./x.txt" or "secret.txt." resolve to other files → CWE-41
        return open(BASE + name).read()
    return "blocked", 403
