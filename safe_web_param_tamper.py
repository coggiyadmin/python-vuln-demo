"""SAFE mirror — web_param_tamper.py. Price comes from server catalog, not the client."""
from flask import Flask, request

app = Flask(__name__)
CATALOG = {"sku-1": 9.99}


@app.route("/checkout", methods=["POST"])
def checkout():
    sku = request.form["sku"]
    qty = int(request.form["qty"])
    price = CATALOG[sku]
    total = price * qty
    return {"charged": total}
