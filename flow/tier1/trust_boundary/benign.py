"""Flow quartet benign TN — no trusted store mutation."""
from decimal import Decimal


def line_total(qty: int, price: str) -> Decimal:
    return Decimal(qty) * Decimal(price)
