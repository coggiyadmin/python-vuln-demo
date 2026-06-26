from flask import Flask, request
import subprocess
app = Flask(__name__)
CACHE = {}
@app.route("/a")
def a():
    CACHE["v"] = request.args.get("q", "")
    return "ok"
@app.route("/b")
def b():
    t = CACHE.get("v", "")
    subprocess.call("grep " + t, shell=True)  # PRP-09 stored2
