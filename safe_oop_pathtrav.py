"""SAFE mirror — oop_pathtrav.py; the tainted name is reduced to its basename and
confined to BASE before open(). Expect 0 security findings."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


class Document:
    def __init__(self, name):
        self.name = name

    def _safe_path(self):
        leaf = os.path.basename(self.name)          # strip any ../ components
        path = os.path.realpath(os.path.join(BASE, leaf))
        if not path.startswith(os.path.realpath(BASE)):
            raise ValueError("path escapes base")
        return path

    def read_direct(self):
        return open(self._safe_path()).read()       # confined path reaches sink


@app.route("/doc")
def doc():
    d = Document(request.args.get("name", ""))
    d.read_direct()
    return "ok"
