from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/c")
def c():
    resp = make_response("ok")
    resp.headers["Set-Cookie"] = "session=" + request.args.get("val", "")
    return resp  # SINK CWE-93 Set-Cookie
