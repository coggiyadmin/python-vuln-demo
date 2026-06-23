"""Vector/Embedding Weakness (OWASP LLM08) — retrieval with no tenant filter. A query
searches the whole shared store, so one tenant's prompt can retrieve another tenant's
private documents (cross-tenant disclosure). TP-2.
"""
_INDEX = []  # all tenants' docs in one space


def retrieve(query_vec, k: int = 5):
    # SINK (LLM08): no tenant/ACL filter on the similarity search
    scored = sorted(_INDEX, key=lambda d: _sim(d["vector"], query_vec), reverse=True)
    return [d["text"] for d in scored[:k]]


def _sim(a, b):
    return sum(x * y for x, y in zip(a, b))
