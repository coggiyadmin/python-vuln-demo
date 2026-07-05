import ssl
def ctx():
    c = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    c.minimum_version = ssl.TLSVersion.TLSv1  # SINK weak min protocol (TLS 1.0)
    return c
