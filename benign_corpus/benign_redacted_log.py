"""TN — structured log with redaction."""
import logging
import re

log = logging.getLogger("app")

def log_user(user: str) -> None:
    safe = re.sub(r"[\r\n\t]", "_", user)
    log.info("event=user_lookup value=%s", safe)
