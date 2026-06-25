"""Combination #4 — ASYNC TAINT × NOSQL (CWE-943, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
col = MongoClient().db.u


async def ident(x):
    return x


@app.route("/a")
async def h():
    q = request.args.get("q", "")
    q = asyncio.run(ident(q))   # taint through await/coroutine
    list(col.find({"name": q}))  # CWE-943
    return "ok"
