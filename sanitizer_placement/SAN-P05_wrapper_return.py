"""SAN-P05 — sanitizer in wrapper returned to sink (c08)."""
import subprocess
from flask import Flask, request

app = Flask(__name__)

def wrap(x: str) -> str:
    return x.replace("<", "")  # weak wrapper, not applied at sink

@app.route("/x")
def h():
    t = wrap(request.args.get("q", ""))
    subprocess.call("grep " + t, shell=True)
