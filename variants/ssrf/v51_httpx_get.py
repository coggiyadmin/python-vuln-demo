from flask import Flask, request
import httpx
app = Flask(__name__)
@app.route("/f")
def f():
    url = request.args.get("url", "")
    return httpx.get(url).text  # SINK CWE-918 httpx client
