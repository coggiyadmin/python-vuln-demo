"""CWE-770 — Allocation of Resources Without Limits or Throttling. A buffer is allocated
from a user-supplied size with no upper bound, enabling memory-exhaustion DoS. NO finding = FN."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/alloc")
def alloc():
    n = int(request.args.get("n", "0"))   # SOURCE — attacker-controlled size
    buf = bytearray(n)                     # unbounded allocation → CWE-770
    return str(len(buf))
