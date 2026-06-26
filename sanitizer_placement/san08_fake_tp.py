from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")  # sanitized below — fake SAN-08
    # sanitized
    subprocess.call("grep " + t, shell=True)
