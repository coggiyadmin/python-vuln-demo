import jwt
def decode_token(token: str, key: str) -> dict:
    return jwt.decode(token, key, algorithms=["HS256"])
