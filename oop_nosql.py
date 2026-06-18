"""Combination #5 — OOP OBJECT FLOW × NoSQL INJECTION (CWE-943, Python). Taint
injected via __init__, stored on self, used in a Mongo $where clause (directly and
via a property). Each is a REAL NoSQL injection; NO finding = FALSE NEGATIVE."""
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


class Query:
    def __init__(self, expr):
        self.expr = expr                    # constructor-injected taint

    @property
    def cond(self):
        return self.expr                    # property exposes tainted field

    def find_direct(self):
        return coll.find({"$where": "this.user == '" + self.expr + "'"})  # 5a → NoSQL sink (CWE-943)

    def find_via_property(self):
        return coll.find({"$where": "this.user == '" + self.cond + "'"})  # 5b via property → sink (CWE-943)


@app.route("/q")
def q():
    qq = Query(request.args.get("user", ""))  # SOURCE → constructor
    list(qq.find_direct())
    list(qq.find_via_property())
    return "ok"
