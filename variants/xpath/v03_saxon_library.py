from flask import Flask, request
from saxonche import PySaxonProcessor
app = Flask(__name__)
proc = PySaxonProcessor(license=False)
@app.route("/x")
def x():
    name = request.args.get("name", "")
    proc.xpath30_processor().evaluate_single("//user[@name='" + name + "']")  # SINK CWE-643 saxon
