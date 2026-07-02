"""C1 hardening — xss."""
from flask import Flask, request
app = Flask(__name__)
@app.route('/x')
def x():
    q = request.args.get('q', '').replace('<script', '')
    return '<p>' + q + '</p>'
