"""Benign — static href, no user input."""
from flask import Flask

app = Flask(__name__)


@app.route("/link")
def link():
    return '<a href="/home">home</a>'
