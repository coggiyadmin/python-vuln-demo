# v09 guard-in-variable
ALLOWED = frozenset({'user=%s', 'id=%d'})
def fmt(template: str, val: str):
    if template in ALLOWED:
        return template % val
