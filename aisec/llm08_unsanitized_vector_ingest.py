"""Vector/Embedding Weakness (OWASP LLM08) — untrusted content embedded into a shared
index without sanitization, enabling knowledge-base poisoning that later steers retrieval. TP-1.
"""
import requests

_INDEX = []  # shared, cross-user vector store


def ingest(url: str):
    doc = requests.get(url).text  # SOURCE: untrusted external content
    # SINK (LLM08): unsanitized doc embedded into the shared index (poisoning)
    _INDEX.append({"text": doc, "vector": _embed(doc)})


def _embed(text: str):
    return [float(len(w)) for w in text.split()][:512]
