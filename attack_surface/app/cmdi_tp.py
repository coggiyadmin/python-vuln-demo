from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/run")
def run_cmd():
    q = request.args.get("q", "")  # SOURCE app entry
    subprocess.call("grep " + q, shell=True)  # SINK CWE-78
