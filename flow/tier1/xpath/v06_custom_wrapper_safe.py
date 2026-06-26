from flask import Flask, request
from lxml import etree
def company_sanitize(x: str) -> str:
    return x.replace("'", "")
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = company_sanitize(request.args.get("name", ""))
    doc.xpath("//user[name='" + name + "']")
