"""
BENIGN-BASELINE TRUE-NEGATIVE FIXTURE.

Ordinary business logic with NO security surface: no HTTP, no DB, no file I/O,
no exec, no crypto, no secrets. The scanner MUST produce ZERO security findings
here. Measures specificity / the noise floor.
"""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable


@dataclass(frozen=True)
class LineItem:
    """A product line with a unit price and quantity."""
    sku: str
    unit_price: Decimal
    quantity: int

    def extended(self) -> Decimal:
        """Extended price: unit_price * quantity."""
        return self.unit_price * self.quantity


TIER_RATES = {"standard": Decimal("0"), "silver": Decimal("0.05"), "gold": Decimal("0.10")}


def subtotal(items: Iterable[LineItem]) -> Decimal:
    """Sum of line extended prices, rounded to cents."""
    total = sum((li.extended() for li in items), Decimal("0"))
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def tier_for(amount: Decimal) -> str:
    """Pick a discount tier from a subtotal."""
    if amount >= Decimal("1000"):
        return "gold"
    if amount >= Decimal("250"):
        return "silver"
    return "standard"


def total(items: Iterable[LineItem]) -> Decimal:
    """Final total after the tier discount."""
    items = list(items)
    sub = subtotal(items)
    discount = sub * TIER_RATES[tier_for(sub)]
    return (sub - discount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def by_category(items: Iterable[LineItem]) -> dict:
    """Group items by the category code before the dash in the SKU."""
    groups: dict = {}
    for li in items:
        code = li.sku.split("-", 1)[0] if "-" in li.sku else "misc"
        groups.setdefault(code, []).append(li)
    return groups


def top_skus(items: Iterable[LineItem], limit: int) -> list:
    """SKUs sorted by descending extended price."""
    ordered = sorted(items, key=lambda li: li.extended(), reverse=True)
    return [li.sku for li in ordered[:limit]]
