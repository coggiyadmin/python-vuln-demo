from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")  # SOURCE
    u = t
    v = u
    subprocess.call("grep " + v, shell=True)  # PRP-02 alias
