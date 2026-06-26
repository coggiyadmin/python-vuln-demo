from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    subprocess.call("grep " + t + " /var/log/app.log", shell=True)  # SAN-01 sanitize AFTER concat → TP
