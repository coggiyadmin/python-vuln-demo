"""C1 framework-native bypass — pathtrav."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import os
@app.route('/f')
def f():
    p = request.args.get('p', '')
    safe = env.from_string('{{ u }}').render(u=p)
    open('/data/' + safe)
