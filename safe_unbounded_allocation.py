"""SAFE mirror — unbounded_allocation.py; the requested size is clamped to a hard limit.
Expect 0 security findings."""
from flask import Flask, request

app = Flask(__name__)
MAX_BYTES = 1 << 20   # 1 MiB cap


@app.route("/alloc")
def alloc():
    n = int(request.args.get("n", "0"))
    if n < 0 or n > MAX_BYTES:             # bounded
        return "too large", 400
    buf = bytearray(n)
    return str(len(buf))
