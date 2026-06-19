"""CWE-1284 — Improper Validation of Specified Quantity in Input. A user-supplied count is used
to allocate and to compute totals with no bound check. NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)
UNIT_PRICE = 999


@app.route("/order")
def order():
    qty = int(request.args.get("qty", "0"))  # SOURCE — no bound/range validation → CWE-1284
    items = [None] * qty                     # unbounded allocation driven by qty
    return "total=" + str(qty * UNIT_PRICE) + " items=" + str(len(items))
