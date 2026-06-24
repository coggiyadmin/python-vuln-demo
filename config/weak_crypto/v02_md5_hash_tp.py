import hashlib
def digest_pw(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()  # SINK CWE-328
