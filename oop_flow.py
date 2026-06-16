"""Combination #5 — OOP OBJECT FLOW (Python). Taint injected via __init__,
stored on self, used in a method sink (directly and via a property). Each is a
REAL command injection; NO finding = FALSE NEGATIVE."""
import os
from flask import Flask, request

app = Flask(__name__)


class Job:
    def __init__(self, host):
        self.host = host                 # constructor-injected taint

    @property
    def target(self):
        return self.host                 # property exposes tainted field

    def run_direct(self):
        os.system("echo " + self.host)    # 5a: field → sink

    def run_via_property(self):
        os.system("echo " + self.target)  # 5b: field via property → sink


@app.route("/run")
def run():
    j = Job(request.args.get("host", ""))  # SOURCE → constructor
    j.run_direct()
    j.run_via_property()
    return "ok"
