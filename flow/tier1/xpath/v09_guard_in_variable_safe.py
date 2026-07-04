# v09 guard-in-variable
ALLOWED = frozenset({'//users/user[@id="1"]'})
def query(expr: str):
    if expr in ALLOWED:
        return expr
