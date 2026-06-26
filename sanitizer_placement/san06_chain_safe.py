from flask import Flask, request
import subprocess, shlex, html
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    t = html.escape(t)
    t = shlex.quote(t)
    subprocess.call("grep " + t + " /var/log/app.log", shell=True)  # SAN-06 chain
