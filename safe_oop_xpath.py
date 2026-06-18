"""SAFE mirror — oop_xpath.py; the tainted value is bound as an XPath variable
instead of concatenated into the query string. Expect 0 security findings."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


class UserLookup:
    def __init__(self, name):
        self.name = name

    def find_direct(self):
        # parameterized XPath — value passed as a variable, never concatenated
        return TREE.xpath("//user[name=$n]", n=self.name)


@app.route("/lookup")
def lookup():
    u = UserLookup(request.args.get("name", ""))
    u.find_direct()
    return "ok"
