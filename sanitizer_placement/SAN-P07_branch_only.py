"""SAN-P07 — sanitizer on branch only (flow-sensitive)."""
import subprocess, shlex
from flask import Flask, request

app = Flask(__name__)

@app.route("/x")
def h():
    t = request.args.get("q", "")
    if len(t) > 100:
        t = shlex.quote(t)
    subprocess.call("grep " + t, shell=True)
