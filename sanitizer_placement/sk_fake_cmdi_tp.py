"""C1 fake sanitizer — partial semicolon strip."""
import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def x():
    t = request.args.get("q", "").replace(";", "")
    subprocess.call("grep " + t, shell=True)
