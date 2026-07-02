"""C1 framework-native bypass — Jinja autoescape on LDAP filter."""
from jinja2 import Environment, BaseLoader, select_autoescape
import ldap
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
@app.route("/l")
def l():
    uid = request.args.get("uid", "")
    filt = env.from_string("(uid={{ u }})").render(u=uid)
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, filt)
