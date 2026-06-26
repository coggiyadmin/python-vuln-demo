from flask import Flask, request
import xml.etree.ElementTree as ET
def company_sanitize(raw: bytes) -> bytes:
    return raw.replace(b"<!ENTITY", b"")
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    ET.fromstring(company_sanitize(request.get_data()))
