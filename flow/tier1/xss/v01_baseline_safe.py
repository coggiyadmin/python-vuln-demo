from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route("/s")
def s():
    q = request.args.get("q", "")
    return "<h1>" + str(escape(q)) + "</h1>"
