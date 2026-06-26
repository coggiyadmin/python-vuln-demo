"""c08 SAFE — custom wrapper × deserialization (CWE-502). Expect clean."""
import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/wrapped")
def wrapped():
    json.loads(request.get_data())
