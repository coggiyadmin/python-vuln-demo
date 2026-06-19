"""CWE-778 — Insufficient Logging. A security-relevant action (account deletion) executes with
no audit log, so the event is untraceable. NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/users/delete", methods=["POST"])
def delete_user():
    target = request.form.get("id", "")
    do_delete(target)                      # security-relevant action, NO audit log → CWE-778
    return "deleted"


def do_delete(_target):
    pass
