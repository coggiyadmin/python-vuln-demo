"""c08 SAFE — custom wrapper × XXE (CWE-611). Expect clean."""
import defusedxml.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)


@app.route("/wrapped")
def wrapped():
    ET.fromstring(request.get_data())
