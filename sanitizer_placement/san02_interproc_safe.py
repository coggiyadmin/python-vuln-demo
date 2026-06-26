from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
def sanitize(x): return shlex.quote(x)
@app.route("/x")
def h():
    t = sanitize(request.args.get("q", ""))
    subprocess.call("grep " + t + " /var/log/app.log", shell=True)  # SAN-02 interproc safe
