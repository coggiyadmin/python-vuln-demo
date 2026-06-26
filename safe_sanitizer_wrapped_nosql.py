"""c08 SAFE — custom wrapper × NoSQL (CWE-943). Expect clean."""
import re
from flask import Flask, request, abort

app = Flask(__name__)
db = {}


def checked_key(k):
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", k):
        abort(400)
    return k


@app.route("/wrapped")
def wrapped():
    k = checked_key(request.args.get("k", ""))
    return str(db.get(k))
