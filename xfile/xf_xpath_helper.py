"""Cross-file taint — SINK side (XPath injection). Imported by xf_xpath_controller.py."""
import lxml.etree as ET

TREE = ET.parse("users.xml")


def find(name: str):
    # SINK: `name` arrives tainted across the file boundary → XPath injection (CWE-643)
    return TREE.xpath("//user[name='" + name + "']")
