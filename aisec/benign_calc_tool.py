"""TN — benign calculator tool. Pure, side-effect-free, bounded input domain; no
shell, no fs, no network. The canonical 'safe tool' an agent can be granted freely.
"""


def add(a: float, b: float) -> float:
    return a + b


def percent_of(value: float, pct: float) -> float:
    return value * pct / 100.0


TOOLS = [{"name": "add", "fn": add}, {"name": "percent_of", "fn": percent_of}]
