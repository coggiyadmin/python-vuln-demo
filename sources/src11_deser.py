import json, sqlite3
def handle(raw: bytes):
    obj = json.loads(raw)  # SOURCE SRC-11 deser
    q = obj.get("q", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM t WHERE n='" + q + "'")  # SINK CWE-89
