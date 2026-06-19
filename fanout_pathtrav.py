"""Combination #11 — FAN-OUT × PATH TRAVERSAL (CWE-22, Python)."""
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/fanout")
def fanout():
    name = request.args.get("name", "")  # SOURCE
    open(BASE + name)  # sink 1
    open(BASE + "tmp/" + name)  # sink 2
    open("/var/tmp/" + name)  # sink 3

