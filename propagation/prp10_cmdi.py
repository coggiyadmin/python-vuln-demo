from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    parts = []
    for x in request.args.getlist("q"):
        parts.append(x)
    t = "".join(parts)
    subprocess.call("grep " + t, shell=True)  # PRP-10 collect
