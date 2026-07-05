from flask import Flask, request
app = Flask(__name__)
import sqlite3
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    import json
    t = json.loads(json.dumps({'v': s}))['v']  # serialize round-trip
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE n='" + t + "'")  # SINK
