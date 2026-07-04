# Z6 benign mirror — FastAPI proxy gated by host frozenset (SSRF FP tax).
from urllib.parse import urlparse
import urllib.request
from fastapi import FastAPI

ALLOWED_HOSTS = frozenset({"api.internal.example.com"})
app = FastAPI()

@app.get("/proxy")
def proxy(url: str):
    host = urlparse(url).netloc.split(":")[0]
    if host in ALLOWED_HOSTS:
        return urllib.request.urlopen(url).read()
    return b"blocked"
