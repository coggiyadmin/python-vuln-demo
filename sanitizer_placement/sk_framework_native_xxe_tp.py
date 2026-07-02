"""C1 framework-native bypass — xxe."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import xml.etree.ElementTree as ET
@app.route('/x')
def x():
    xml = request.get_data(as_text=True)
    safe = env.from_string('{{ u }}').render(u=xml)
    ET.fromstring(safe)
