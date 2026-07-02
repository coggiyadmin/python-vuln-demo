"""C1 framework-native bypass — code_inj."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
@app.route('/eval')
def eval_route():
    expr = request.args.get('expr', '')
    safe = env.from_string('{{ u }}').render(u=expr)
    eval(safe)
