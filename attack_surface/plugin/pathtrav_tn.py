def plugin_read(path: str) -> str:
    return open("/data/" + path).read()
