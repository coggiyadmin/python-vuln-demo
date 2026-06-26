from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    payload = {"q": request.args.get("q", "")}
    (t,) = (payload["q"],)
    subprocess.call("grep " + t, shell=True)  # PRP-03
