from flask import Flask, request, abort
import defusedxml.ElementTree as ET
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    raw = request.get_data()
    if len(raw) > 65536:
        abort(413)
    return ET.fromstring(raw).tag
