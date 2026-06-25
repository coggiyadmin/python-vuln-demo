"""Combination #4 — ASYNC TAINT × XXE (CWE-611, Python). Taint carried through
a coroutine, then reaches the sink. NO finding = FALSE NEGATIVE."""
import asyncio
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)


async def ident(x):
    return x


@app.route("/a", methods=["POST"])
async def h():
    body = request.get_data()
    body = asyncio.run(ident(body))   # taint through await/coroutine
    ET.fromstring(body)  # CWE-611
    return "ok"
