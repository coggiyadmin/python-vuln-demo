"""C1 framework-native bypass — xpath."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
from lxml import etree
@app.route('/q')
def q():
    q = request.args.get('q', '')
    safe = env.from_string('{{ u }}').render(u=q)
    etree.XML('<root/>').xpath(safe)
