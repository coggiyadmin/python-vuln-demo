from flask import Flask, request
from jinja2 import Environment
app = Flask(__name__)
@app.route("/s")
def s():
    q = request.args.get("q", "")
    Environment().from_string(q).render()  # SINK CWE-94 Jinja2 SSTI
