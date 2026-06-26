from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    ua = request.headers.get("User-Agent", "")  # SOURCE SRC-03 header
    subprocess.call("echo " + ua, shell=True)  # SINK
