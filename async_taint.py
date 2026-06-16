"""Combination #4 — ASYNC taint (Python). await a coroutine carrying the taint."""
import asyncio, os
from flask import Flask, request
app = Flask(__name__)
async def echo(x): return x
@app.route("/a")
async def h():
    u = request.args.get("u", "")
    v = asyncio.run(echo(u))   # taint through await/coroutine
    os.system("echo " + v)     # CWE-78
    return "ok"
