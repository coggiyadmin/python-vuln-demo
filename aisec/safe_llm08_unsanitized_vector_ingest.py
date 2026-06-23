"""SAFE mirror (OWASP LLM08) — ingestion is sanitized, size-bounded, and namespaced per
tenant so one tenant cannot poison another's retrieval space.
"""
_INDEX = {}


def ingest(tenant: str, text: str):
    clean = text.replace("\x00", "")[:20000]
    _INDEX.setdefault(tenant, []).append({"text": clean, "vector": _embed(clean)})


def _embed(text: str):
    return [float(len(w)) for w in text.split()][:512]
