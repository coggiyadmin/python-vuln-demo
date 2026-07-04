# v09 guard-in-variable
ALLOWED_BASES = frozenset({'dc=example,dc=com'})
def search(base: str, filt: str):
    if base in ALLOWED_BASES:
        return base + filt
