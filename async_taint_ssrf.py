"""Combination #4 — ASYNC taint × SSRF (CWE-918, Python). await a coroutine
carrying the taint, then fetch. NO finding = FALSE NEGATIVE."""
import asyncio
import requests
from flask import Flask, request

app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a")
async def h():
    u = request.args.get("u", "")
    v = asyncio.run(ident(u))   # taint through await/coroutine
    requests.get(v)             # CWE-918
    return "ok"
