from flask import Flask, request
from mako.template import Template
app = Flask(__name__)
@app.route("/s")
def s():
    tpl = request.args.get("tpl", "")
    return Template(tpl).render()  # SINK CWE-94 Mako from user string
