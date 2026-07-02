"""C1 custom wrapper — org helper strips only semicolons before shell."""
import subprocess
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace(";", "")

@app.route("/x")
def x():
    t = company_sanitize(request.args.get("q", ""))
    subprocess.call("grep " + t, shell=True)
