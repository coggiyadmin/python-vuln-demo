# v09 guard-in-variable
import logging
ALLOWED = frozenset({'INFO', 'WARN'})
def log(level: str, msg: str):
    if level in ALLOWED:
        logging.log(getattr(logging, level), msg)
