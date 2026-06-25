"""Combination #4 — ASYNC TAINT × SSTI (CWE-1336, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
from jinja2 import Template
from flask import Flask, request
app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a")
async def h():
    t = request.args.get("t", "")
    t = asyncio.run(ident(t))   # taint through await/coroutine
    Template(t).render()  # CWE-1336
    return "ok"
