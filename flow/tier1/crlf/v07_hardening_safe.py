# hardening mirror — crlf
import re
from flask import Flask, request, Response, abort
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = request.args.get("url", "")
    if re.search(r"[\r\n]", loc):
        abort(400)
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp
