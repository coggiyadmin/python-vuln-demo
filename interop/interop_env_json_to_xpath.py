"""IL-60 — JSON env blob → XPath string (IL-5 config frontier)."""
import json
import os
from lxml import etree

def lookup():
    blob = os.environ.get("USER_FILTER", "{}")
    name = json.loads(blob).get("name", "")
    doc = etree.fromstring(b"<users/>")
    doc.xpath("//user[name='" + name + "']")
