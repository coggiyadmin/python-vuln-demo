from html import escape
from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = escape(request.args.get("url", ""))
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp
