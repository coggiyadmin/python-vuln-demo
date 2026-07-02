"""C1 wrong-context — HTML escape before XPath query."""
import html
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = html.escape(request.args.get("name", ""))
    doc.xpath("//user[name='" + name + "']")
