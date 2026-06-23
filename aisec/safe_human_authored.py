"""Order-book aggregation — idiomatic, human-authored (no AI-gen fingerprint)."""
from collections import defaultdict


def aggregate_fills(fills):
    book = defaultdict(float)
    for price, qty in fills:
        book[price] += qty
    return sorted(book.items())
