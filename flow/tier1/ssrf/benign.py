"""Flow quartet benign TN — pricing logic only, no security surface."""
from decimal import Decimal

def line_total(qty: int, price: str) -> Decimal:
    return Decimal(qty) * Decimal(price)
