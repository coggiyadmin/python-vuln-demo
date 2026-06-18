"""Combination #5 — OOP OBJECT FLOW × LOG INJECTION (CWE-117, Python). Taint
injected via __init__, stored on self, written to a log sink (directly and via a
property). Each is a REAL log injection; NO finding = FALSE NEGATIVE."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("app")


class Audit:
    def __init__(self, actor):
        self.actor = actor                  # constructor-injected taint

    @property
    def who(self):
        return self.actor                   # property exposes tainted field

    def record_direct(self):
        log.info("login by " + self.actor)   # 5a: field → log sink (CWE-117)

    def record_via_property(self):
        log.info("logout by " + self.who)    # 5b: via property → sink (CWE-117)


@app.route("/audit")
def audit():
    a = Audit(request.args.get("user", ""))  # SOURCE → constructor
    a.record_direct()
    a.record_via_property()
    return "ok"
