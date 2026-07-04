# v09 guard-in-variable
import json
ALLOWED = frozenset({b'{}', b'[]'})
def loads(raw: bytes):
    if raw in ALLOWED:
        return json.loads(raw)
