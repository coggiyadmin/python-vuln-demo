"""Combinations #6/#7/#8 — SANITIZER × XXE (CWE-611, Python)."""
import lxml.etree as ET
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_xml(s):
    return s


def safe_parse(xml_bytes):
    parser = ET.XMLParser(resolve_entities=False, no_network=True)
    return ET.fromstring(xml_bytes, parser)


@app.route("/wrong")
def wrong():
    xml = escape_html(request.args.get("xml", ""))
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(str(xml).encode(), parser)  # CWE-611


@app.route("/fake")
def fake():
    xml = sanitize_xml(request.args.get("xml", ""))
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml.encode(), parser)  # CWE-611


@app.route("/wrapped")
def wrapped():
    xml = request.args.get("xml", "")
    safe_parse(xml.encode())  # expect 0 (#8)

