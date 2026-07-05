import jwt, os
def verify(token):
    return jwt.decode(token, os.environ['JWT_PUBKEY'], algorithms=['RS256'])  # verified
