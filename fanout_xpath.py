"""Combination #11 — FAN-OUT × XPATH (CWE-643, Python)."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    TREE.xpath("//user[name='" + n + "']")  # sink 1
    TREE.xpath("//account[name='" + n + "']")  # sink 2
    TREE.xpath("//*[@id='" + n + "']")  # sink 3

