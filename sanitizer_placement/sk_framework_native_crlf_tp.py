"""C1 framework-native bypass — HTML escape before CRLF header."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request, make_response
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    loc = env.from_string("/home?u={{ u }}").render(u=nxt)
    resp = make_response("ok")
    resp.headers["Location"] = loc
    return resp
