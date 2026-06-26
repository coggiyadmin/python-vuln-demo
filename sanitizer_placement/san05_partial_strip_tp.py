from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "").replace("<", "")
    subprocess.call("grep " + t, shell=True)  # SAN-05 partial strip
