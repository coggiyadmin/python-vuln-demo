"""CWE-472 — External Control of Assumed-Immutable Web Parameter. The server trusts
a client-supplied 'price'/'role' field for a security/financial decision. (Engine
gap.) FN probe — NO finding = potential FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/checkout", methods=["POST"])
def checkout():
    price = request.form["price"]   # SOURCE — client-controlled "hidden" field
    qty = int(request.form["qty"])
    total = float(price) * qty       # trusts client-set price → CWE-472
    return {"charged": total}
