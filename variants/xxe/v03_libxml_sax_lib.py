from flask import Flask, request
from lxml import etree
app = Flask(__name__)
@app.route("/x", methods=["POST"])
def x():
    etree.fromstring(request.get_data())  # SINK CWE-611 lxml etree
