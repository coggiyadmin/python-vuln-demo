"""SAFE mirror — quantity_validation.py; the quantity is range-checked before use. Expect 0."""
from flask import Flask, request

app = Flask(__name__)
UNIT_PRICE = 999
MAX_QTY = 100


@app.route("/order")
def order():
    try:
        qty = int(request.args.get("qty", "0"))
    except ValueError:
        return "bad qty", 400
    if qty < 1 or qty > MAX_QTY:             # bounded range enforced
        return "qty out of range", 400
    items = [None] * qty
    return "total=" + str(qty * UNIT_PRICE) + " items=" + str(len(items))
