"""Combination #5 — OOP OBJECT FLOW × PATH TRAVERSAL (CWE-22, Python). Taint
injected via __init__, stored on self, used in a method sink (directly and via a
property). Each is a REAL path traversal; NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


class Document:
    def __init__(self, name):
        self.name = name                   # constructor-injected taint

    @property
    def filename(self):
        return self.name                   # property exposes tainted field

    def read_direct(self):
        return open(BASE + self.name).read()      # 5a: field → open() sink (CWE-22)

    def read_via_property(self):
        return open(BASE + self.filename).read()  # 5b: via property → sink (CWE-22)


@app.route("/doc")
def doc():
    d = Document(request.args.get("name", ""))  # SOURCE → constructor
    d.read_direct()
    d.read_via_property()
    return "ok"
