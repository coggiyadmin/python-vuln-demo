from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    subprocess.call(f"grep {t}", shell=True)  # PRP-06 template
