"""Combination #13 — ENCODED PAYLOAD × NoSQL (CWE-943, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    expr = base64.b64decode(raw).decode()
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    expr = unquote(raw)
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943

