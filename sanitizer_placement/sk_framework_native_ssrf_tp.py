"""C1 framework-native bypass — ssrf."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import urllib.request
@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    safe = env.from_string('{{ u }}').render(u=url)
    urllib.request.urlopen(safe)
