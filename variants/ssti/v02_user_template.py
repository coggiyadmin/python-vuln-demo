from jinja2 import Template
from flask import Flask, request
app = Flask(__name__)
@app.route("/t")
def t():
    t = request.args.get("t", "")
    return Template(t).render()  # SINK CWE-1336
