"""C1 framework-native bypass — openredirect."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
from flask import redirect
@app.route('/go')
def go():
    nxt = request.args.get('next', '')
    label = env.from_string('{{ u }}').render(u=nxt)
    return redirect(label)
