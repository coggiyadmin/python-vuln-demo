from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); col = MongoClient().db.u
@app.route("/a")
def a():
    filt = request.args.to_dict()
    list(col.aggregate([{"$match": filt}]))  # SINK CWE-943
