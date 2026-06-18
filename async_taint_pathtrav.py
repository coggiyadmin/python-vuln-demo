"""Combination #4 — ASYNC taint × PATH TRAVERSAL (CWE-22, Python). await a
coroutine carrying the taint, then open. NO finding = FALSE NEGATIVE."""
import asyncio
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


async def ident(x):
    return x


@app.route("/a")
async def h():
    n = request.args.get("n", "")
    v = asyncio.run(ident(n))   # taint through await/coroutine
    open(BASE + v)              # CWE-22
    return "ok"
