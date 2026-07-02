"""C1 custom wrapper — org helper strips ENTITY only; external entities remain."""
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(raw: bytes) -> bytes:
    return raw.replace(b"ENTITY", b"")

@app.route("/xml", methods=["POST"])
def parse_xml():
    ET.fromstring(company_sanitize(request.get_data()))
