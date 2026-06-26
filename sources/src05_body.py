from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x", methods=["POST"])
def h():
    q = request.json.get("q", "")  # SOURCE SRC-05 body
    subprocess.call("grep " + q, shell=True)  # SINK
