from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/h")
def h():
    lang = request.args.get("lang", "")
    r = Response("ok")
    r.headers["Content-Language"] = lang  # SINK CWE-113 header injection
    return r
