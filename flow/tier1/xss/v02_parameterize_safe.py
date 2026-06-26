from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route("/s")
def s():
    return f"<h1>{escape(request.args.get('q', ''))}</h1>"
