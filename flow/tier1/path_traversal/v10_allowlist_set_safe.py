# v10 allowlist-set
import os
SAFE_FILES = {'/var/log/app.log', '/tmp/safe/out.txt'}
def read(target: str):
    if target in SAFE_FILES:
        return open(target).read()
