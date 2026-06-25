"""TP — distributed API accepts pickled agent payload (CWE-502 intake pattern)."""
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.post("/api/agent/data")
def ingest():
    blob = request.get_data()
    obj = pickle.loads(blob)  # SINK CWE-502
    return {"status": "ok", "type": type(obj).__name__}
