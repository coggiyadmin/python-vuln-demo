from flask import Flask, request, Response
def company_sanitize(x: str) -> str:
    return x.replace("\r", "").replace("\n", "")
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = company_sanitize(request.args.get("url", ""))
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp
