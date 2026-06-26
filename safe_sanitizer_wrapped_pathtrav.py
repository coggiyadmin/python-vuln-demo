"""c08 SAFE — custom wrapper × path traversal (CWE-22). Expect clean."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


def checked_name(s):
    return os.path.basename(s)


@app.route("/wrapped")
def wrapped():
    name = checked_name(request.args.get("name", ""))
    open(BASE + name)
