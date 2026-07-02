"""C1 framework-native bypass — Jinja HTML escape on format string keys only."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
@app.route("/greet")
def greet():
    fmt = request.args.get("fmt", "Hello {name}")
    name = request.args.get("name", "")
    safe_name = env.from_string("{{ n }}").render(n=name)
    return fmt.format(name=safe_name)
