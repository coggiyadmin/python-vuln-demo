from fastapi import FastAPI
import urllib.request
app = FastAPI()
@app.get("/proxy")
def proxy(url: str):
    return urllib.request.urlopen(url).read()  # SINK CWE-918 FastAPI param
