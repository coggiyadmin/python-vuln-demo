"""Combination #4 — ASYNC TAINT × DESERIALIZE (CWE-502, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
import pickle
from flask import Flask, request
app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a", methods=["POST"])
async def h():
    body = request.get_data()
    body = asyncio.run(ident(body))   # taint through await/coroutine
    pickle.loads(body)  # CWE-502
    return "ok"
