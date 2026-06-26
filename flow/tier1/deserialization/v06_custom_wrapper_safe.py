import json
from flask import Flask, request
def company_sanitize(raw: bytes) -> bytes:
    return raw.replace(b"__", b"")
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
    return str(json.loads(company_sanitize(request.get_data())))
