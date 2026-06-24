"""FP-target — logging a constant must not be flagged log injection."""
import logging
log = logging.getLogger("app")
def start():
    log.info("service started")  # constant — NOT a sink
