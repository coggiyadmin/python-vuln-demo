"""SAFE mirror — oop_deserialize.py; JSON is parsed instead of pickle, so no
arbitrary object/gadget instantiation is possible. Expect 0 security findings."""
import json
from flask import Flask, request

app = Flask(__name__)


class Session:
    def __init__(self, blob):
        self.blob = blob

    def load_direct(self):
        return json.loads(self.blob)        # data-only parse, no code execution


@app.route("/restore")
def restore():
    s = Session(request.args.get("s", ""))
    s.load_direct()
    return "ok"
