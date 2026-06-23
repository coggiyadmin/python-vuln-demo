"""Vector/Embedding FN probe (OWASP LLM08) — cross-tenant leak via a shared cache keyed
only by the query, not the tenant. Two tenants issuing the same query share cached results,
so private hits cross the boundary. No ACL check appears at retrieval. Expected: MISS.
"""
_CACHE = {}
_INDEX = []


def retrieve(tenant: str, query: str):
    if query in _CACHE:
        return _CACHE[query]  # SINK (LLM08 FN): cache key omits tenant -> cross-tenant reuse
    hits = [d["text"] for d in _INDEX if d["tenant"] == tenant and query in d["text"]]
    _CACHE[query] = hits
    return hits
