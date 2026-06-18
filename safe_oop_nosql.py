"""SAFE mirror — oop_nosql.py; the tainted value is used as a plain equality match
value (no $where, no operator injection). Expect 0 security findings."""
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


class Query:
    def __init__(self, expr):
        self.expr = expr

    def find_direct(self):
        return coll.find({"user": self.expr})   # value-bound equality, not a JS expression


@app.route("/q")
def q():
    qq = Query(request.args.get("user", ""))
    list(qq.find_direct())
    return "ok"
