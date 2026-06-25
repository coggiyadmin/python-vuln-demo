"""Combination #4 — ASYNC TAINT × XPATH (CWE-643, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b'<users/>')


async def ident(x):
    return x


@app.route("/a")
async def h():
    name = request.args.get("name", "")
    name = asyncio.run(ident(name))   # taint through await/coroutine
    doc.xpath("//user[name='" + name + "']")  # CWE-643
    return "ok"
