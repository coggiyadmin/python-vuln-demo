"""Combination #13 — ENCODED PAYLOAD × XPATH (CWE-643, Python)."""
import base64
import lxml.etree as ET
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    TREE.xpath("//user[name='" + name + "']")  # CWE-643


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    TREE.xpath("//user[name='" + name + "']")  # CWE-643

