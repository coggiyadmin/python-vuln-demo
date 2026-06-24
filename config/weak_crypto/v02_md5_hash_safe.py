import hashlib
def digest_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()
