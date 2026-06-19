"""SAFE mirror — insufficient_logging.py; the action is audited (CRLF-stripped actor). Expect 0."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("audit")


@app.route("/users/delete", methods=["POST"])
def delete_user():
    target = request.form.get("id", "")
    actor = request.headers.get("X-Actor", "")
    safe_actor = actor.replace("\r", "").replace("\n", "")
    safe_target = target.replace("\r", "").replace("\n", "")
    do_delete(target)
    log.info("action=delete-user actor=%s target=%s outcome=ok", safe_actor, safe_target)  # audited
    return "deleted"


def do_delete(_target):
    pass
