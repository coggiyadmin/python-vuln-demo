# v09 guard-in-variable
import os
ALLOWED_BASES = frozenset({'/var/log', '/tmp/safe'})
def read(base: str, name: str):
    if base in ALLOWED_BASES:
        return open(os.path.join(base, name)).read()
