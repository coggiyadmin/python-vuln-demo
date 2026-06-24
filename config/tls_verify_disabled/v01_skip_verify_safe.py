import urllib.request
def fetch() -> bytes:
    return urllib.request.urlopen("https://api.internal.example.com/health").read()
