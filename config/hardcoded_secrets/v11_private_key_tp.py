PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA1c3EXAMPLEKEYMATERIALdoNotUseInProduction0000
-----END RSA PRIVATE KEY-----'''  # SINK CWE-798 embedded private key
def sign():
    return PRIVATE_KEY
