"""CWE-470 — Unsafe Reflection. User input selects a class/function to instantiate
or import, enabling arbitrary code paths. Real vuln; NO finding = FALSE NEGATIVE."""
import importlib
from flask import Flask, request

app = Flask(__name__)


@app.route("/make")
def make():
    mod = request.args.get("mod", "")     # SOURCE
    fn = request.args.get("fn", "")        # SOURCE
    m = importlib.import_module(mod)        # arbitrary module load → CWE-470
    return str(getattr(m, fn)())           # arbitrary attribute/callable → CWE-470
