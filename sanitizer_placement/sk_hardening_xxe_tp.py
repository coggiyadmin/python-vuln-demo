"""C1 hardening — payload size cap only; entities still enabled."""
import xml.etree.ElementTree as ET
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    raw = request.get_data()
    if len(raw) > 65536:
        abort(413)
    ET.fromstring(raw)
