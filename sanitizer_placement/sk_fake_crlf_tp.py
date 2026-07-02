"""C1 fake — strip SAFE before Location header."""
from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = request.args.get("url", "").replace("SAFE", "")
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp
