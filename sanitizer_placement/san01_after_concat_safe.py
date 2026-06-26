from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    safe = shlex.quote(t)
    subprocess.call("grep " + safe + " /var/log/app.log", shell=True)  # SAN-01 BEFORE → safe
