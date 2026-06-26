# custom_wrapper mirror — xpath
import re
from flask import Flask, request, abort
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = request.args.get("name", "")
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", name):
        abort(403)
    doc.xpath("//user[name=$name]", name=name)
