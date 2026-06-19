"""Combinations #6/#7/#8 — SANITIZER × XPATH INJECTION (CWE-643, Python)."""
import re
import lxml.etree as ET
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


def escape_html(s):
    return escape(str(s))


def sanitize_name(s):
    return s


def xpath_safe(s):
    return re.sub(r"['\\]", "", s)


@app.route("/wrong")
def wrong():
    name = escape_html(request.args.get("name", ""))
    TREE.xpath("//user[name='" + str(name) + "']")  # CWE-643


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    TREE.xpath("//user[name='" + name + "']")  # CWE-643


@app.route("/wrapped")
def wrapped():
    name = xpath_safe(request.args.get("name", ""))
    TREE.xpath("//user[name='" + name + "']")  # expect 0 (#8)

