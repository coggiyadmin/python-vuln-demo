from html import escape
from flask import Flask, request
app = Flask(__name__)
@app.route("/r")
def r():
    p = escape(request.args.get("p", ""))  # HTML escape wrong for path
    return open("/data/" + p).read()  # TP wrong context
