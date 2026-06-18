"""Cross-file taint — SINK side (log injection). Imported by xf_loginj_controller.py."""
import logging

log = logging.getLogger("app")


def record(actor: str):
    # SINK: `actor` arrives tainted across the file boundary → log injection (CWE-117)
    log.info("login by " + actor)
