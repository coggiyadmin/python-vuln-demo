"""Combination #4 — ASYNC taint × OPEN REDIRECT (CWE-601, Python). await a
coroutine carrying the taint, then redirect. NO finding = FALSE NEGATIVE."""
import asyncio
from flask import Flask, request, redirect

app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a")
async def h():
    nxt = request.args.get("next", "")
    v = asyncio.run(ident(nxt))   # taint through await/coroutine
    return redirect(v)            # CWE-601
