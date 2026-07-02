"""C1 wrong-context — SQL concat before XML parse."""
import sqlite3
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)
@app.route("/xml", methods=["POST"])
def parse_xml():
    n = request.args.get("n", "").replace("'", "''")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
    ET.fromstring(request.get_data())
