"""Combination #10 — TEST-FILE handling. This file's name matches the test
pattern (*_test.py). It contains a REAL command injection. Question: does the
engine fire by default, and does --exclude-tests suppress it?"""
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run():
    cmd = request.args.get("cmd", "")
    os.system("echo " + cmd)   # real CWE-78 — in a *_test.py file
    return "ok"
