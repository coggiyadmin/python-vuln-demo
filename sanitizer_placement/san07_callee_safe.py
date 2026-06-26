from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
def sink(v): subprocess.call("grep " + v + " /var/log/app.log", shell=True)
@app.route("/x")
def h():
    sink(shlex.quote(request.args.get("q", "")))
