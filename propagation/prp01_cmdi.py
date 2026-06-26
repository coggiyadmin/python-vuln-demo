from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    subprocess.call("grep " + request.args.get("q", ""), shell=True)  # PRP-01 inline
