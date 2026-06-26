# Phase-3 encode mirror
from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = request.args.get("name", "guest")
    return "Hello {}".format(name)
