from flask import Flask, request
from pymongo import MongoClient
import json
app = Flask(__name__); col = MongoClient().app.users
@app.route('/agg')
def agg():
    stage = json.loads(request.args.get('stage', '{}'))
    col.aggregate([stage])  # SINK CWE-943
