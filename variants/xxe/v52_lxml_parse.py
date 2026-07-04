from flask import Flask, request
from lxml import etree
app = Flask(__name__)
@app.route("/x", methods=["POST"])
def x():
    p = etree.XMLParser(no_network=False, resolve_entities=True)
    etree.parse(request.stream, p)  # SINK CWE-611 lxml.parse external entities
