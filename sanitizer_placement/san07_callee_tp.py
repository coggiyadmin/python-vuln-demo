from flask import Flask, request
import subprocess
app = Flask(__name__)
def sink(v): subprocess.call("grep " + v, shell=True)
@app.route("/x")
def h():
    sink(request.args.get("q", ""))  # SAN-07 caller sink no sanitize
