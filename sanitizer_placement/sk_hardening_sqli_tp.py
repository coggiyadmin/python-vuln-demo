"""C1 hardening — sqli."""
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route('/q')
def q():
    n = request.args.get('n', '').replace('--', '')
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE n='" + n + "'")
