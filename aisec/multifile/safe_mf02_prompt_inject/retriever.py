"""Retrieval step — SAFE mirror: host-allowlisted fetch of external content (LLM01, part 1 of 2)."""
from urllib.parse import urlparse

import requests

_ALLOWED = {"docs.example.com", "wiki.example.com"}


def fetch(url: str) -> str:
    if urlparse(url).hostname not in _ALLOWED:
        raise ValueError("host not allowlisted")
    return requests.get(url).text
