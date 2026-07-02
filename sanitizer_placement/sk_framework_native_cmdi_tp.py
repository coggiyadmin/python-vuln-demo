"""C1 framework-native bypass — cmdi."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import subprocess
@app.route('/run')
def run():
    cmd = request.args.get('cmd', '')
    safe = env.from_string('{{ u }}').render(u=cmd)
    subprocess.call(safe, shell=True)
