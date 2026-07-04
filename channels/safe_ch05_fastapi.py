"""TN — FastAPI proxy with host allowlist."""
from urllib.parse import urlparse
import urllib.request
from fastapi import FastAPI
ALLOWED = frozenset({"api.internal.example.com"})
app = FastAPI()
@app.get("/proxy")
def proxy(url: str):
    if urlparse(url).netloc.split(":")[0] in ALLOWED:
        return urllib.request.urlopen(url).read()
    return b"blocked"
