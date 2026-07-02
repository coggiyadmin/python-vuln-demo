"""C1 framework-native bypass — Jinja HTML escape before log line."""
from jinja2 import Environment, BaseLoader, select_autoescape
import logging
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
log = logging.getLogger("app")
@app.route("/auth")
def auth():
    user = request.args.get("user", "")
    line = env.from_string("login user={{ u }}").render(u=user)
    log.warning(line)
