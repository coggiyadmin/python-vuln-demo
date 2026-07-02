"""SAN-P06 — chain encode → validate → sink (defense in depth)."""
import re
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/x")
def h():
    t = request.args.get("q", "")
    t = t.replace("<", "")
    if not re.fullmatch(r"[a-zA-Z0-9 _-]+", t):
        return "bad", 400
    subprocess.call("grep " + t, shell=True)
