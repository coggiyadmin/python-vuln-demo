from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = request.args.get("url", "")
    resp = Response("redirecting")
    resp.headers["Location"] = loc  # SINK CWE-93 CRLF
    return resp
