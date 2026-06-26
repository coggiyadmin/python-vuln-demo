import sqlite3
from flask import Flask, request
import xml.etree.ElementTree as ET
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    n = request.args.get("n", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
    ET.fromstring(request.get_data())
