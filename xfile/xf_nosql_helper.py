"""Cross-file taint — SINK side (NoSQL injection). Imported by xf_nosql_controller.py."""
from pymongo import MongoClient

coll = MongoClient().app.users


def find(expr: str):
    # SINK: `expr` arrives tainted across the file boundary → NoSQL injection (CWE-943)
    return coll.find({"$where": "this.user == '" + expr + "'"})
