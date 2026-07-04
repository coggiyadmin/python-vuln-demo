from flask import Flask, request
from lxml import etree
app = Flask(__name__)
@app.route("/xp")
def xp():
    name = request.args.get("name", "")
    doc = etree.parse("users.xml")
    return str(doc.xpath("//user[@name='" + name + "']"))  # SINK CWE-643 lxml xpath concat
