"""c08 SAFE — custom wrapper × SSTI (CWE-1336). Expect clean."""
from flask import Flask, request, abort
from jinja2 import Environment, BaseLoader

app = Flask(__name__)
env = Environment(loader=BaseLoader())
ALLOWED = {"hello", "status"}


@app.route("/wrapped")
def wrapped():
    t = request.args.get("t", "")
    if t not in ALLOWED:
        abort(403)
    env.from_string("{{ " + t + " }}").render()
