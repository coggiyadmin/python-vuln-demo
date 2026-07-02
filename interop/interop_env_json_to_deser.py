"""IL-53 — JSON env blob → pickle.loads (IL-5 config frontier)."""
import base64
import json
import os
import pickle

def load():
    blob = os.environ.get("USER_BLOB", "{}")
    raw = json.loads(blob).get("payload", "")
    pickle.loads(base64.b64decode(raw))
