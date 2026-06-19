"""SAFE — Combination #8 custom-wrapper × PATH TRAVERSAL (CWE-22, Python).
Basename confines path under BASE; expect 0 substantive findings (FP = #79/#102)."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


def checked_name(s):
    return os.path.basename(s)


@app.route("/wrapped")
def wrapped():
    name = checked_name(request.args.get("name", ""))
    open(BASE + name)
