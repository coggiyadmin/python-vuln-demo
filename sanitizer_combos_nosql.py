"""Combinations #6/#7/#8 — SANITIZER × NoSQL INJECTION (CWE-943, Python)."""
from markupsafe import escape
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


def escape_html(s):
    return escape(str(s))


def sanitize_expr(s):
    return s


def safe_query(user):
    return coll.find({"user": user})


@app.route("/wrong")
def wrong():
    expr = escape_html(request.args.get("user", ""))
    coll.find({"$where": "this.user == '" + str(expr) + "'"})  # CWE-943


@app.route("/fake")
def fake():
    expr = sanitize_expr(request.args.get("user", ""))
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943


@app.route("/wrapped")
def wrapped():
    user = request.args.get("user", "")
    list(safe_query(user))  # expect 0 (#8 — no $where)

