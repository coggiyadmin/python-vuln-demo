import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/c")
def c():
    q = request.args.get("q", "")
    subprocess.call("grep " + q, shell=True)  # SINK CWE-78
