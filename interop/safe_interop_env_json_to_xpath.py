"""SAFE — constant XPath only."""
from lxml import etree

def lookup():
    doc = etree.fromstring(b"<users/>")
    doc.xpath("//user[name='alice']")
