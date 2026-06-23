"""SAFE mirror — same behavior, decomposed into small low-CC helpers (table-driven).
High Maintainability Index. The metric must DISCRIMINATE this from complex_high_cc.py."""


def _sign(n):
    return "p" if n > 0 else "n" if n < 0 else "z"


def classify(a, b, c, d, kind):
    handlers = {"x": _classify_x, "y": _classify_y, "z": _classify_z}
    handler = handlers.get(kind)
    return handler(a, b, c, d) if handler else "default"


def _classify_x(a, b, c, d):
    return "x" + _sign(a) + _sign(b) + _sign(c)


def _classify_y(a, b, c, d):
    return "y_ok" if a and b else "y_alt"


def _classify_z(a, b, c, d):
    return "z_even" if a % 2 == 0 else "z_odd"
