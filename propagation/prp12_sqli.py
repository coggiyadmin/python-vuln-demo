from flask import Flask, request
app = Flask(__name__)
import sqlite3
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    globals()['_G'] = s  # store in module global
    t = globals()['_G']
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE n='" + t + "'")  # SINK
