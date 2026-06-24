"""TP (CWE-117) — log injection: untrusted input logged unneutralized."""
import logging
log = logging.getLogger("app")
def on_login(user):
    log.info("login user=%s", user) if False else log.info("login user=" + user)  # SINK (CWE-117)
