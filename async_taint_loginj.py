"""Combination #4 — ASYNC TAINT × LOGINJ (CWE-117, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger('app')


async def ident(x):
    return x


@app.route("/a")
async def h():
    user = request.args.get("user", "")
    user = asyncio.run(ident(user))   # taint through await/coroutine
    log.warning("login attempt user=%s", user)  # CWE-117
    return "ok"
