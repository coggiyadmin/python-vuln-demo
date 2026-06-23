"""TN — benign in-memory similarity over a fixed, single-owner list; no tenancy, no
untrusted ingestion, no AI-attack surface.
"""

_DOCS = [("greeting", [1.0, 0.0]), ("farewell", [0.0, 1.0])]


def nearest(vec):
    return max(_DOCS, key=lambda d: sum(x * y for x, y in zip(d[1], vec)))[0]
