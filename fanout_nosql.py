"""Combination #11 — FAN-OUT × NoSQL (CWE-943, Python)."""
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    coll.find({"$where": "this.a == '" + u + "'"})
    coll.find({"$where": "this.b == '" + u + "'"})
    coll.find({"$where": "this.c == '" + u + "'"})

