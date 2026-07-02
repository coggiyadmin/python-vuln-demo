"""C1 wrong-context — URL encode before shell sink."""
import subprocess
from flask import Flask, request
from urllib.parse import quote
app = Flask(__name__)
@app.route("/x")
def x():
    t = quote(request.args.get("q", ""))
    subprocess.call("grep " + t, shell=True)
