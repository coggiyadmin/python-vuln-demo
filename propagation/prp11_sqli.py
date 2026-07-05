from flask import Flask, request
app = Flask(__name__)
import sqlite3
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    f = lambda: s  # taint captured in closure
    t = f()
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE n='" + t + "'")  # SINK
