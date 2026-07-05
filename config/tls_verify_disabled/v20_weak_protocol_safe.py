import ssl
def ctx():
    c = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    c.minimum_version = ssl.TLSVersion.TLSv1_2  # TLS 1.2 minimum
    return c
