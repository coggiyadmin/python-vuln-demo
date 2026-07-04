"""Performance — blocking sync I/O on hot path."""
import time
from urllib.request import urlopen
def handle(req_id: str) -> str:
    time.sleep(2)  # blocks caller
    return urlopen("https://api.example.com/" + req_id).read().decode()
