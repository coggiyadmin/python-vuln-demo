from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/h")
def h():
    loc = request.args.get("url", "")
    resp = Response("ok")
    resp.headers["Location"] = loc  # SINK CWE-601
    return resp
