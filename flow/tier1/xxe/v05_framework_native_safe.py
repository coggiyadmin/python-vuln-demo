import defusedxml.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    return ET.fromstring(request.get_data()).tag
