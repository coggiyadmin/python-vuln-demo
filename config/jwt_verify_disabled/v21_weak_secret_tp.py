import jwt
def sign(payload):
    return jwt.encode(payload, 'secret', algorithm='HS256')  # SINK hardcoded weak secret
