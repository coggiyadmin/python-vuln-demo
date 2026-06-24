import random
def session_token() -> int:
    return random.randint(0, 999999)  # SINK CWE-330
