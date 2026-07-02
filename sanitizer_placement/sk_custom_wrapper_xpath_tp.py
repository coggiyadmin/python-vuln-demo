"""C1 custom wrapper — org helper strips quotes only before XPath."""
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")

def company_sanitize(v: str) -> str:
    return v.replace("'", "").replace('"', "")

@app.route("/x")
def x():
    name = company_sanitize(request.args.get("name", ""))
    doc.xpath("//user[name='" + name + "']")
