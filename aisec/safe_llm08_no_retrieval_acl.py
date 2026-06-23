"""SAFE mirror (OWASP LLM08) — retrieval is scoped to the caller's tenant before ranking.
"""
_INDEX = []


def retrieve(tenant: str, query_vec, k: int = 5):
    scoped = [d for d in _INDEX if d["tenant"] == tenant]  # ACL filter first
    scored = sorted(scoped, key=lambda d: _sim(d["vector"], query_vec), reverse=True)
    return [d["text"] for d in scored[:k]]


def _sim(a, b):
    return sum(x * y for x, y in zip(a, b))
