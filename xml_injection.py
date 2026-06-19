"""CWE-91 — XML Injection. Unescaped user input concatenated into an XML document
lets the attacker inject elements (e.g. override <price>). Real vuln; NO finding = FN."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)


@app.route("/order")
def order():
    qty = request.args.get("qty", "")   # SOURCE
    # qty = "1</qty><price>0</price><qty>1" injects structure → CWE-91
    doc = "<order><qty>" + qty + "</qty><price>100</price></order>"
    return ET.tostring(ET.fromstring(doc.encode()))
