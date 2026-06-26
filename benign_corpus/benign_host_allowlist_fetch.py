"""TN — SSRF host allowlist."""
import requests
from urllib.parse import urlparse

ALLOWED = {"api.internal.example.com"}

def fetch(url: str) -> str:
    host = urlparse(url).hostname
    if host not in ALLOWED:
        raise ValueError("host not allowed")
    return requests.get(url, timeout=5).text
