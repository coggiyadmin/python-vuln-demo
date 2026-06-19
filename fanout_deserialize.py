"""Combination #11 — FAN-OUT × DESERIALIZE (CWE-502, Python)."""
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    s = request.args.get("s", "")  # SOURCE
    blob = base64.b64decode(s)
    pickle.loads(blob)  # sink 1
    pickle.loads(blob + b"")  # sink 2
    pickle.loads(blob)  # sink 3

