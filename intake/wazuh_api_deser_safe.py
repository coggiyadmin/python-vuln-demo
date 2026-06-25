"""Safe mirror — JSON-only agent ingest."""
import json
from flask import Flask, request

app = Flask(__name__)


@app.post("/api/agent/data")
def ingest():
    obj = request.get_json(force=True, silent=True)
    if not isinstance(obj, dict):
        return {"error": "invalid"}, 400
    return {"status": "ok", "keys": list(obj.keys())}
