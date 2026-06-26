from flask import Flask, request
import subprocess
app = Flask(__name__)
def wrap(x): return x  # fake wrapper — not a sanitizer
@app.route("/x")
def h():
    t = wrap(request.args.get("q", ""))
    subprocess.call("grep " + t, shell=True)  # SAN-02 interproc TP
