import jwt
def verify(token):
    return jwt.decode(token, options={'verify_signature': False})  # SINK signature not verified
