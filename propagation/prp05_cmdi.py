from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")[0:999]
    subprocess.call("grep " + t, shell=True)  # PRP-05 slice
