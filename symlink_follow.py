"""CWE-59 — Link Following (symlink TOCTOU). open() follows a symlink in an
attacker-writable directory to reach a sensitive file. (Engine gap.) FN probe."""
from flask import Flask, request

app = Flask(__name__)
UPLOADS = "/var/app/uploads/"


@app.route("/cat")
def cat():
    name = request.args.get("name", "")   # SOURCE
    # if uploads/<name> is a symlink to /etc/shadow, it is followed → CWE-59
    return open(UPLOADS + name).read()
