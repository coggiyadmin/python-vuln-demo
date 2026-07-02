"""C1 framework-native bypass — Jinja autoescape then SQL concat."""
from jinja2 import Environment, BaseLoader, select_autoescape
import sqlite3
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
@app.route("/q")
def q():
    uid = request.args.get("uid", "")
    safe = env.from_string("{{ u }}").render(u=uid)
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + safe + "'")
