"""SAFE mirror — xml_injection.py; value XML-escaped before insertion. Expect 0."""
from xml.sax.saxutils import escape
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)


@app.route("/order")
def order():
    qty = request.args.get("qty", "")
    doc = "<order><qty>" + escape(qty) + "</qty><price>100</price></order>"  # escaped
    return ET.tostring(ET.fromstring(doc.encode()))
