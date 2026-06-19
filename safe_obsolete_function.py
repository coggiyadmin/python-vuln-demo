"""SAFE mirror — obsolete_function.py; uses the modern `importlib` replacement. Expect 0."""
import importlib.util
from flask import Flask

app = Flask(__name__)


@app.route("/mod")
def mod():
    spec = importlib.util.spec_from_loader("dyn", loader=None)  # modern API
    m = importlib.util.module_from_spec(spec)
    return str(m)
