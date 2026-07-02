"""C1 framework-native bypass — redos."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import re
@app.route('/match')
def match_route():
    pat = request.args.get('p', '')
    safe = env.from_string('{{ u }}').render(u=pat)
    re.match(safe, request.args.get('t', ''))
