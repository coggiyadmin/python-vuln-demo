import ssl, urllib.request
def fetch(url: str) -> bytes:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # SINK CWE-295
    return urllib.request.urlopen(url, context=ctx).read()
