"""Cross-file taint — SINK side (insecure deserialization). Imported by
xf_deserialize_controller.py."""
import base64
import pickle


def load(blob: str):
    # SINK: `blob` arrives tainted across the file boundary → deserialization (CWE-502)
    return pickle.loads(base64.b64decode(blob))
