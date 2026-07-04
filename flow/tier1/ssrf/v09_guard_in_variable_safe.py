# v09 guard-in-variable — host allowlist in module frozenset.
from urllib.parse import urlparse
import urllib.request

ALLOWED_HOSTS = frozenset({"api.internal.example.com"})

def fetch(url: str) -> bytes:
    host = urlparse(url).netloc.split(":")[0]
    if host in ALLOWED_HOSTS:
        return urllib.request.urlopen(url).read()
    return b"blocked"
