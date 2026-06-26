from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    q = request.args.get("q", "")  # SOURCE SRC-01 query
    subprocess.call("grep " + q, shell=True)  # SINK CWE-78
