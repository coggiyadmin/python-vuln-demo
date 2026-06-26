import sqlite3
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b"<users/>")
@app.route("/x")
def x():
    name = request.args.get("name", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + name + "'")
    doc.xpath("//user[name='" + name + "']")
