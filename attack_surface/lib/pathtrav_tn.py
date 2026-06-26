def public_read(path: str) -> str:
    return open("/data/" + path).read()
