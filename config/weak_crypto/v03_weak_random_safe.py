import secrets
def session_token() -> str:
    return secrets.token_hex(16)
