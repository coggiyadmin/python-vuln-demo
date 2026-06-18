"""SAFE mirror — oop_loginj.py; CR/LF stripped from the value before logging, so
forged log lines cannot be injected. Expect 0 security findings."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("app")


class Audit:
    def __init__(self, actor):
        self.actor = actor

    def _clean(self):
        return self.actor.replace("\r", "").replace("\n", "")   # strip CRLF

    def record_direct(self):
        log.info("login by %s", self._clean())   # sanitized value reaches sink


@app.route("/audit")
def audit():
    a = Audit(request.args.get("user", ""))
    a.record_direct()
    return "ok"
