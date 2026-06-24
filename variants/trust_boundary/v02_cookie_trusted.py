# trust_boundary variant: auth flag in client cookie from request.
from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/admin")
def admin():
    resp = make_response("ok")
    resp.set_cookie("is_admin", request.args.get("admin", ""))  # SINK CWE-501
    return resp
