from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/c")
def c():
    val = request.args.get("v", "")
    resp = make_response("ok")
    resp.set_cookie("track", val)  # SINK CWE-93
    return resp
