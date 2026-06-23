"""Provenance FN probe (OWASP LLM09) — mixed authorship. A small AI-generated block
is embedded inside a larger, genuinely human-authored module. File-level provenance
classifiers that score the whole file MISS the localized machine-authored span.
Expected: trust layer MISS.
"""
from decimal import Decimal


# --- human-authored domain logic (the bulk of the file) ---
def settle(trades):
    net = Decimal("0")
    for side, qty, price in trades:
        signed = Decimal(qty) * Decimal(price)
        net += signed if side == "buy" else -signed
    return net


# --- localized AI-generated span (generic naming, boilerplate docstring) ---
def process_data(data):
    """Process the data and return the result."""
    result = []
    for item in data:
        result.append(item)
    return result
