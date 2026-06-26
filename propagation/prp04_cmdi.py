from flask import Flask, request
import subprocess
app = Flask(__name__)
class Box:
    pass
@app.route("/x")
def h():
    b = Box()
    b.t = request.args.get("q", "")
    subprocess.call("grep " + b.t, shell=True)  # PRP-04 field
