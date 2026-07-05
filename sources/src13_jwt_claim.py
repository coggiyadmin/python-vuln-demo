import jwt, subprocess
def handle(token):
    claims = jwt.decode(token, options={"verify_signature": False})  # SOURCE jwt claim
    subprocess.call("echo " + claims["cmd"], shell=True)  # SINK
