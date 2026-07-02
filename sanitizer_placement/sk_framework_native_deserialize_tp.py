"""C1 framework-native bypass — deserialize."""
from jinja2 import Environment, BaseLoader, select_autoescape
from flask import Flask, request
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
app = Flask(__name__)
import pickle
@app.route('/d', methods=['POST'])
def d():
    blob = request.get_data()
    safe = env.from_string('{{ u }}').render(u=blob.decode('latin1'))
    pickle.loads(safe.encode('latin1'))
