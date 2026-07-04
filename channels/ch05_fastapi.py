"""CH-05 FastAPI route param → outbound fetch SSRF."""
from fastapi import FastAPI
import urllib.request
app = FastAPI()
@app.get("/proxy")
def proxy(url: str):
    return urllib.request.urlopen(url).read()  # SOURCE/SINK CWE-918
