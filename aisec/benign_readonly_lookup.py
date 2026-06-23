"""TN — benign read-only lookup tool. Returns values from a fixed in-memory catalog
by exact key; no dynamic path, no I/O, no model-controlled side effect.
"""

_CATALOG = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "JPY": "Japanese Yen",
}


def currency_name(code: str) -> str:
    return _CATALOG.get(code.upper(), "unknown")


TOOLS = [{"name": "currency_name", "fn": currency_name}]
