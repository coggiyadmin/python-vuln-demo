import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/c")
def c():
    subprocess.run(["grep", request.args.get("q", ""), "/var/log/app.log"], shell=False)
