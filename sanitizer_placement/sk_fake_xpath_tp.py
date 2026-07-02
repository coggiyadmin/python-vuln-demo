"""C1 fake — comment-only before XPath query."""
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = request.args.get("name", "")  # sanitized
    doc.xpath("//user[name='" + name + "']")
