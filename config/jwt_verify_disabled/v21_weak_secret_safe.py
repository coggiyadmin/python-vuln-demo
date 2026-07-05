import jwt, os
def sign(payload):
    return jwt.encode(payload, os.environ['JWT_SECRET'], algorithm='HS256')  # from env
