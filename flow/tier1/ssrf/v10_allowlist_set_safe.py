# v10 allowlist-set — scheme+host dict gate before fetch.
from urllib.parse import urlparse
import urllib.request

ALLOWED = {("https", "cdn.example.com"), ("https", "api.example.com")}

def fetch(url: str) -> bytes:
    p = urlparse(url)
    if (p.scheme, p.netloc.split(":")[0]) in ALLOWED:
        return urllib.request.urlopen(url).read()
    return b"blocked"
