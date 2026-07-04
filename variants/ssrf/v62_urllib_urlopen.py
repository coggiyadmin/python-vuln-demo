from flask import Flask, request
import urllib.request
app = Flask(__name__)
@app.route("/f")
def f():
    url = request.args.get("url", "")
    return urllib.request.urlopen(url).read()  # SINK CWE-918 urllib urlopen
