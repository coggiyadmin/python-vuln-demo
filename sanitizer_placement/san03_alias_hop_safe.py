from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
@app.route("/x")
def h():
    t = shlex.quote(request.args.get("q", ""))
    u = t
    subprocess.call("grep " + u + " /var/log/app.log", shell=True)
