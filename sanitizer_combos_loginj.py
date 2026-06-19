"""Combinations #6/#7/#8 — SANITIZER × LOG INJECTION (CWE-117, Python)."""
import logging
import re
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


def escape_html(s):
    return escape(str(s))


def sanitize_actor(s):
    return s


def strip_crlf(s):
    return re.sub(r"[\r\n]", "", s)


@app.route("/wrong")
def wrong():
    actor = escape_html(request.args.get("user", ""))
    log.info("login " + str(actor))  # CWE-117


@app.route("/fake")
def fake():
    actor = sanitize_actor(request.args.get("user", ""))
    log.info("login " + actor)  # CWE-117


@app.route("/wrapped")
def wrapped():
    actor = strip_crlf(request.args.get("user", ""))
    log.info("login " + actor)  # expect 0 (#8)

