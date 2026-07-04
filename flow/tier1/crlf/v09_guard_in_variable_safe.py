# v09 guard-in-variable
ALLOWED = frozenset({'text/plain', 'application/json'})
def set_ct(value: str):
    if value in ALLOWED:
        return f'Content-Type: {value}'
