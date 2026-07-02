"""C1 hardening — input length cap only before XPath."""
from flask import Flask, request, abort
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = request.args.get("name", "")
    if len(name) > 256:
        abort(413)
    doc.xpath("//user[name='" + name + "']")
