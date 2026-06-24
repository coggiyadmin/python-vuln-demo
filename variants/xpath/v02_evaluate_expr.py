from flask import Flask, request
import xml.etree.ElementTree as ET
app = Flask(__name__)
@app.route("/e")
def e():
    expr = request.args.get("expr", "")
    ET.ElementTree(ET.fromstring("<r/>")).find(expr)  # SINK CWE-643
