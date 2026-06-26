"""TN — JSON parse only (no pickle)."""
import json

def parse(raw: bytes) -> dict:
    return json.loads(raw)
