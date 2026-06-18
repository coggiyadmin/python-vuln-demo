"""Combination #5 — OOP OBJECT FLOW × XPATH INJECTION (CWE-643, Python). Taint
injected via __init__, stored on self, used to build an XPath query (directly and
via a property). Each is a REAL XPath injection; NO finding = FALSE NEGATIVE."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


class UserLookup:
    def __init__(self, name):
        self.name = name                    # constructor-injected taint

    @property
    def q(self):
        return self.name                    # property exposes tainted field

    def find_direct(self):
        return TREE.xpath("//user[name='" + self.name + "']")   # 5a: field → XPath sink (CWE-643)

    def find_via_property(self):
        return TREE.xpath("//user[name='" + self.q + "']")      # 5b: via property → sink (CWE-643)


@app.route("/lookup")
def lookup():
    u = UserLookup(request.args.get("name", ""))  # SOURCE → constructor
    u.find_direct()
    u.find_via_property()
    return "ok"
