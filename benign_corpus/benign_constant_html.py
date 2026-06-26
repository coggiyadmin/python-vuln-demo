"""TN — static HTML response."""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><p>Hello</p></body></html>"
