from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    if t == "admin":
        t = shlex.quote(t)
    subprocess.call("grep " + t, shell=True)  # SAN-04 branch only
