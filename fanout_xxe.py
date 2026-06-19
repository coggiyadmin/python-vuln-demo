"""Combination #11 — FAN-OUT × XXE (CWE-611, Python)."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
PARSER = ET.XMLParser(resolve_entities=True, no_network=False)


@app.route("/fanout")
def fanout():
    xml = request.args.get("xml", "").encode()  # SOURCE
    ET.fromstring(xml, PARSER)
    ET.fromstring(b"<r>" + xml + b"</r>", PARSER)
    ET.fromstring(xml, PARSER)

