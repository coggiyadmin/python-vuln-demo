"""C1 fake — comment-only before XML parse."""
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    raw = request.get_data()  # sanitized
    ET.fromstring(raw)
