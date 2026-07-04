from flask import Flask, request, Markup
app = Flask(__name__)
@app.route("/m")
def m():
    q = request.args.get("q", "")  # SOURCE
    return Markup(q)  # SINK CWE-79 Jinja2 Markup bypass
