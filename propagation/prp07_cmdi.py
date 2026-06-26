from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = (request.args.get("q") or "") if request.args else ""
    subprocess.call("grep " + t, shell=True)  # PRP-07
