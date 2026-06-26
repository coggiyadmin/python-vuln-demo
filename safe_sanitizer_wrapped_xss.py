"""c08 SAFE — custom wrapper × XSS (CWE-79). Expect clean."""
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


@app.route("/wrapped")
def wrapped():
    return escape(request.args.get("q", ""))
