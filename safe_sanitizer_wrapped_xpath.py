"""c08 SAFE — custom wrapper × XPath (CWE-643). Expect clean."""
import re
from lxml import etree
from flask import Flask, request, abort

app = Flask(__name__)


def checked_name(name):
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", name):
        abort(400)
    return name


@app.route("/wrapped")
def wrapped():
    name = checked_name(request.args.get("name", ""))
    etree.XPath(f"/users/user[@name='{name}']")
