from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/user/<uid>")
def h(uid):
    subprocess.call("id " + uid, shell=True)  # SOURCE path segment SRC-02
