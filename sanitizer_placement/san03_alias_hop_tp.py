from flask import Flask, request
import subprocess, shlex
app = Flask(__name__)
@app.route("/x")
def h():
    t = shlex.quote(request.args.get("q", ""))
    u = t
    subprocess.call("grep " + request.args.get("q", ""), shell=True)  # SAN-03 alias hop ignores sanitize
