from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = ""
    try:
        t = request.args.get("q", "")
    except Exception:
        pass
    subprocess.call("grep " + t, shell=True)  # PRP-08
