from flask import Flask, request
from mako.template import Template
app = Flask(__name__)
@app.route("/t")
def t():
    q = request.args.get("q", "")
    Template(q).render()  # SINK CWE-94 Mako
