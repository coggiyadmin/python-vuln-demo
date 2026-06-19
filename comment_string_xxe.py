"""Combination #9 — COMMENT / STRING-LITERAL × XXE (CWE-611, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    xml = request.args.get("xml", "")
    # ET.fromstring(xml.encode(), parser)
    example = "fromstring(xml)"
    return str(len(example) + len(xml))

