# v09 guard-in-variable
ALLOWED_COLS = frozenset({'name', 'status'})
def find(col: str, val: str):
    if col in ALLOWED_COLS:
        return {col: val}
