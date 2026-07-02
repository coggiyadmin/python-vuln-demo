"""SAN-P08 — partial strip (`replace('<','')`) weak sanitizer TP."""
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/x")
def h():
    t = request.args.get("q", "").replace("<", "")
    subprocess.call("grep " + t, shell=True)
