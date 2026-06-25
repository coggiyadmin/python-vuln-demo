"""Combination #4 — ASYNC TAINT × LDAP (CWE-90, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
import ldap
from flask import Flask, request
app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a")
async def h():
    uid = request.args.get("uid", "")
    uid = asyncio.run(ident(uid))   # taint through await/coroutine
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # CWE-90
    return "ok"
