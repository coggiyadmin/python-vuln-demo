from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    t = shlex.quote(t)
    subprocess.call("grep " + t + " /var/log/app.log", shell=True)
