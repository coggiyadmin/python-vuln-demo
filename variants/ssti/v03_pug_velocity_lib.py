from flask import Flask, request
from jinja2 import Template
app = Flask(__name__)
@app.route("/t")
def t():
    return Template('Hello ' + request.args.get('name', '')).render()  # SINK CWE-94 jinja Template
