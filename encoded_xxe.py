"""Combination #13 — ENCODED PAYLOAD × XXE (CWE-611, Python)."""
import base64
import lxml.etree as ET
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    xml = base64.b64decode(raw)
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml, parser)  # CWE-611


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    xml = unquote(raw).encode()
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml, parser)  # CWE-611

