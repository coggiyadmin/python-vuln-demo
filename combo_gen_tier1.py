#!/usr/bin/env python3
"""One-shot generator for Tier-1 combo #6–#11/#13 Python fixtures. Run once, then delete or keep for regen."""
from pathlib import Path

ROOT = Path(__file__).parent

SANITIZER = {
    "ssrf": '''"""Combinations #6/#7/#8 — SANITIZER × SSRF (CWE-918, Python)."""
import requests
from markupsafe import escape
from urllib.parse import urlparse
from flask import Flask, request

app = Flask(__name__)
ALLOWED = {"api.internal.example.com"}


def escape_html(s):
    return escape(str(s))


def sanitize_url(u):
    return u


def checked_url(u):
    host = urlparse(u).hostname
    if host not in ALLOWED:
        raise ValueError("host not allowed")
    return u


@app.route("/wrong")
def wrong():
    u = escape_html(request.args.get("url", ""))  # wrong-context for SSRF
    requests.get(str(u))  # CWE-918


@app.route("/fake")
def fake():
    u = sanitize_url(request.args.get("url", ""))
    requests.get(u)  # CWE-918


@app.route("/wrapped")
def wrapped():
    u = checked_url(request.args.get("url", ""))
    requests.get(u)  # expect 0 (#8 custom wrapper)
''',
    "pathtrav": '''"""Combinations #6/#7/#8 — SANITIZER × PATH TRAVERSAL (CWE-22, Python)."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


def strip_html(s):
    return s.replace("<", "").replace(">", "")  # wrong-context — useless for paths


def sanitize_name(s):
    return s


def checked_name(s):
    return os.path.basename(s)


@app.route("/wrong")
def wrong():
    name = strip_html(request.args.get("name", ""))
    open(BASE + name)  # CWE-22 — HTML strip does not confine path


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    open(BASE + name)  # CWE-22


@app.route("/wrapped")
def wrapped():
    name = checked_name(request.args.get("name", ""))
    open(BASE + name)  # expect 0 (#8)
''',
    "openredirect": '''"""Combinations #6/#7/#8 — SANITIZER × OPEN REDIRECT (CWE-601, Python)."""
from markupsafe import escape
from urllib.parse import urlparse
from flask import Flask, request, redirect

app = Flask(__name__)
ALLOWED_HOSTS = {"login.example.com"}


def escape_html(s):
    return escape(str(s))


def sanitize_next(s):
    return s


def checked_next(s):
    host = urlparse(s).hostname
    if host not in ALLOWED_HOSTS:
        raise ValueError("host not allowed")
    return s


@app.route("/wrong")
def wrong():
    n = escape_html(request.args.get("next", ""))
    return redirect(str(n))  # CWE-601


@app.route("/fake")
def fake():
    n = sanitize_next(request.args.get("next", ""))
    return redirect(n)  # CWE-601


@app.route("/wrapped")
def wrapped():
    n = checked_next(request.args.get("next", ""))
    return redirect(n)  # expect 0 (#8)
''',
    "loginj": '''"""Combinations #6/#7/#8 — SANITIZER × LOG INJECTION (CWE-117, Python)."""
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
    return re.sub(r"[\\r\\n]", "", s)


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
''',
    "ldap": '''"""Combinations #6/#7/#8 — SANITIZER × LDAP INJECTION (CWE-90, Python)."""
import ldap
import re
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


def escape_html(s):
    return escape(str(s))


def sanitize_user(s):
    return s


def ldap_safe(s):
    return re.sub(r"[()=*\\\\]", "", s)


@app.route("/wrong")
def wrong():
    user = escape_html(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + str(user) + ")")  # CWE-90


@app.route("/fake")
def fake():
    user = sanitize_user(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90


@app.route("/wrapped")
def wrapped():
    user = ldap_safe(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # expect 0 (#8)
''',
    "xpath": '''"""Combinations #6/#7/#8 — SANITIZER × XPATH INJECTION (CWE-643, Python)."""
import re
import lxml.etree as ET
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


def escape_html(s):
    return escape(str(s))


def sanitize_name(s):
    return s


def xpath_safe(s):
    return re.sub(r"['\\\\]", "", s)


@app.route("/wrong")
def wrong():
    name = escape_html(request.args.get("name", ""))
    TREE.xpath("//user[name='" + str(name) + "']")  # CWE-643


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    TREE.xpath("//user[name='" + name + "']")  # CWE-643


@app.route("/wrapped")
def wrapped():
    name = xpath_safe(request.args.get("name", ""))
    TREE.xpath("//user[name='" + name + "']")  # expect 0 (#8)
''',
    "nosql": '''"""Combinations #6/#7/#8 — SANITIZER × NoSQL INJECTION (CWE-943, Python)."""
from markupsafe import escape
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


def escape_html(s):
    return escape(str(s))


def sanitize_expr(s):
    return s


def safe_query(user):
    return coll.find({"user": user})


@app.route("/wrong")
def wrong():
    expr = escape_html(request.args.get("user", ""))
    coll.find({"$where": "this.user == '" + str(expr) + "'"})  # CWE-943


@app.route("/fake")
def fake():
    expr = sanitize_expr(request.args.get("user", ""))
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943


@app.route("/wrapped")
def wrapped():
    user = request.args.get("user", "")
    list(safe_query(user))  # expect 0 (#8 — no $where)
''',
    "ssti": '''"""Combinations #6/#7/#8 — SANITIZER × SSTI (CWE-1336, Python)."""
from markupsafe import escape
from flask import Flask, request, render_template_string

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_name(s):
    return s


@app.route("/wrong")
def wrong():
    name = escape_html(request.args.get("name", ""))
    render_template_string("<p>Hello " + str(name) + "</p>")  # CWE-1336


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    render_template_string("<p>Hello " + name + "</p>")  # CWE-1336


@app.route("/wrapped")
def wrapped():
    name = request.args.get("name", "")
    render_template_string("<p>Hello {{ name }}</p>", name=name)  # expect 0 (#8)
''',
    "deserialize": '''"""Combinations #6/#7/#8 — SANITIZER × DESERIALIZATION (CWE-502, Python)."""
import base64
import json
import pickle
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_blob(s):
    return s


@app.route("/wrong")
def wrong():
    blob = escape_html(request.args.get("s", ""))
    pickle.loads(base64.b64decode(str(blob)))  # CWE-502


@app.route("/fake")
def fake():
    blob = sanitize_blob(request.args.get("s", ""))
    pickle.loads(base64.b64decode(blob))  # CWE-502


@app.route("/wrapped")
def wrapped():
    blob = request.args.get("s", "")
    json.loads(base64.b64decode(blob))  # expect 0 (#8 — json not pickle)
''',
    "xxe": '''"""Combinations #6/#7/#8 — SANITIZER × XXE (CWE-611, Python)."""
import lxml.etree as ET
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_xml(s):
    return s


def safe_parse(xml_bytes):
    parser = ET.XMLParser(resolve_entities=False, no_network=True)
    return ET.fromstring(xml_bytes, parser)


@app.route("/wrong")
def wrong():
    xml = escape_html(request.args.get("xml", ""))
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(str(xml).encode(), parser)  # CWE-611


@app.route("/fake")
def fake():
    xml = sanitize_xml(request.args.get("xml", ""))
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml.encode(), parser)  # CWE-611


@app.route("/wrapped")
def wrapped():
    xml = request.args.get("xml", "")
    safe_parse(xml.encode())  # expect 0 (#8)
''',
}

COMMENT = {
    "ssrf": '''"""Combination #9 — COMMENT / STRING-LITERAL × SSRF (CWE-918, Python). Expect 0 findings."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    url = request.args.get("url", "")
    # requests.get(url)  # commented sink — must not fire
    example = "requests.get(url)"  # string literal
    return str(len(example) + len(url))
''',
    "pathtrav": '''"""Combination #9 — COMMENT / STRING-LITERAL × PATH TRAVERSAL (CWE-22, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    name = request.args.get("name", "")
    # open("/data/" + name)  # commented
    example = "open('/data/' + name)"
    return str(len(example) + len(name))
''',
    "openredirect": '''"""Combination #9 — COMMENT / STRING-LITERAL × OPEN REDIRECT (CWE-601, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("next", "")
    # redirect(n)  # commented
    example = "redirect(next)"
    return str(len(example) + len(n))
''',
    "loginj": '''"""Combination #9 — COMMENT / STRING-LITERAL × LOG INJECTION (CWE-117, Python). Expect 0."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # log.info("user " + u)  # commented
    example = "log.info(u)"
    return str(len(example) + len(u))
''',
    "ldap": '''"""Combination #9 — COMMENT / STRING-LITERAL × LDAP (CWE-90, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # conn.search_s(BASE, ldap.SCOPE_SUBTREE, "(uid=" + u + ")")
    example = "(uid=" + u + ")"  # string only, not executed as filter
    return str(len(example))
''',
    "xpath": '''"""Combination #9 — COMMENT / STRING-LITERAL × XPATH (CWE-643, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("name", "")
    # TREE.xpath("//user[name='" + n + "']")
    example = "//user[name='" + n + "']"
    return str(len(example))
''',
    "nosql": '''"""Combination #9 — COMMENT / STRING-LITERAL × NoSQL (CWE-943, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # coll.find({"$where": "this.user == '" + u + "'"})
    example = "$where: this.user == '" + u + "'"
    return str(len(example))
''',
    "ssti": '''"""Combination #9 — COMMENT / STRING-LITERAL × SSTI (CWE-1336, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("name", "")
    # render_template_string("<p>" + n + "</p>")
    example = "{{ " + n + " }}"
    return str(len(example))
''',
    "deserialize": '''"""Combination #9 — COMMENT / STRING-LITERAL × DESERIALIZE (CWE-502, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    s = request.args.get("s", "")
    # pickle.loads(base64.b64decode(s))
    example = "pickle.loads(s)"
    return str(len(example) + len(s))
''',
    "xxe": '''"""Combination #9 — COMMENT / STRING-LITERAL × XXE (CWE-611, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    xml = request.args.get("xml", "")
    # ET.fromstring(xml.encode(), parser)
    example = "fromstring(xml)"
    return str(len(example) + len(xml))
''',
}

ENCODED = {
    "ssrf": '''"""Combination #13 — ENCODED PAYLOAD × SSRF (CWE-918, Python)."""
import base64
import requests
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    u = base64.b64decode(raw).decode()
    requests.get(u)  # CWE-918


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    u = unquote(raw)
    requests.get(u)  # CWE-918
''',
    "pathtrav": '''"""Combination #13 — ENCODED PAYLOAD × PATH TRAVERSAL (CWE-22, Python)."""
import base64
import os
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    open(BASE + name)  # CWE-22


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    open(BASE + name)  # CWE-22
''',
    "openredirect": '''"""Combination #13 — ENCODED PAYLOAD × OPEN REDIRECT (CWE-601, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    n = base64.b64decode(raw).decode()
    return redirect(n)  # CWE-601


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    n = unquote(raw)
    return redirect(n)  # CWE-601
''',
    "loginj": '''"""Combination #13 — ENCODED PAYLOAD × LOG INJECTION (CWE-117, Python)."""
import base64
import logging
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    actor = base64.b64decode(raw).decode()
    log.info("actor " + actor)  # CWE-117


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    actor = unquote(raw)
    log.info("actor " + actor)  # CWE-117
''',
    "ldap": '''"""Combination #13 — ENCODED PAYLOAD × LDAP (CWE-90, Python)."""
import base64
import ldap
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    user = base64.b64decode(raw).decode()
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    user = unquote(raw)
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90
''',
    "xpath": '''"""Combination #13 — ENCODED PAYLOAD × XPATH (CWE-643, Python)."""
import base64
import lxml.etree as ET
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    TREE.xpath("//user[name='" + name + "']")  # CWE-643


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    TREE.xpath("//user[name='" + name + "']")  # CWE-643
''',
    "nosql": '''"""Combination #13 — ENCODED PAYLOAD × NoSQL (CWE-943, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    expr = base64.b64decode(raw).decode()
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    expr = unquote(raw)
    coll.find({"$where": "this.user == '" + expr + "'"})  # CWE-943
''',
    "ssti": '''"""Combination #13 — ENCODED PAYLOAD × SSTI (CWE-1336, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    render_template_string("<p>" + name + "</p>")  # CWE-1336


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    render_template_string("<p>" + name + "</p>")  # CWE-1336
''',
    "deserialize": '''"""Combination #13 — ENCODED PAYLOAD × DESERIALIZE (CWE-502, Python)."""
import base64
import pickle
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    blob = base64.b64decode(raw)
    pickle.loads(blob)  # CWE-502


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    blob = unquote(raw).encode()
    pickle.loads(blob)  # CWE-502
''',
    "xxe": '''"""Combination #13 — ENCODED PAYLOAD × XXE (CWE-611, Python)."""
import base64
import lxml.etree as ET
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    xml = base64.b64decode(raw)
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml, parser)  # CWE-611


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    xml = unquote(raw).encode()
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    ET.fromstring(xml, parser)  # CWE-611
''',
}

FANOUT = {
    "ssrf": '''"""Combination #11 — FAN-OUT × SSRF (CWE-918, Python). One source → multiple SSRF sinks."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    requests.get(u)  # sink 1
    requests.get("http://proxy/?url=" + u)  # sink 2
    requests.post(u)  # sink 3
''',
    "pathtrav": '''"""Combination #11 — FAN-OUT × PATH TRAVERSAL (CWE-22, Python)."""
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/fanout")
def fanout():
    name = request.args.get("name", "")  # SOURCE
    open(BASE + name)  # sink 1
    open(BASE + "tmp/" + name)  # sink 2
    open("/var/tmp/" + name)  # sink 3
''',
    "openredirect": '''"""Combination #11 — FAN-OUT × OPEN REDIRECT (CWE-601, Python)."""
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    redirect(n)  # sink 1 (unused response)
    redirect("https://a.example/" + n)  # sink 2
    return redirect("https://b.example/" + n)  # sink 3
''',
    "loginj": '''"""Combination #11 — FAN-OUT × LOG INJECTION (CWE-117, Python)."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    log.info("a " + u)  # sink 1
    log.warning("b " + u)  # sink 2
    log.error("c " + u)  # sink 3
''',
    "ldap": '''"""Combination #11 — FAN-OUT × LDAP (CWE-90, Python)."""
import ldap
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + u + ")")  # sink 1
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(cn=" + u + ")")  # sink 2
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(mail=" + u + ")")  # sink 3
''',
    "xpath": '''"""Combination #11 — FAN-OUT × XPATH (CWE-643, Python)."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
TREE = ET.parse("users.xml")


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    TREE.xpath("//user[name='" + n + "']")  # sink 1
    TREE.xpath("//account[name='" + n + "']")  # sink 2
    TREE.xpath("//*[@id='" + n + "']")  # sink 3
''',
    "nosql": '''"""Combination #11 — FAN-OUT × NoSQL (CWE-943, Python)."""
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
coll = MongoClient().app.users


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    coll.find({"$where": "this.a == '" + u + "'"})
    coll.find({"$where": "this.b == '" + u + "'"})
    coll.find({"$where": "this.c == '" + u + "'"})
''',
    "ssti": '''"""Combination #11 — FAN-OUT × SSTI (CWE-1336, Python)."""
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    n = request.args.get("n", "")  # SOURCE
    render_template_string("<p>" + n + "</p>")
    render_template_string("<h1>" + n + "</h1>")
    render_template_string("{% set x = '" + n + "' %}{{ x }}")
''',
    "deserialize": '''"""Combination #11 — FAN-OUT × DESERIALIZE (CWE-502, Python)."""
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    s = request.args.get("s", "")  # SOURCE
    blob = base64.b64decode(s)
    pickle.loads(blob)  # sink 1
    pickle.loads(blob + b"")  # sink 2
    pickle.loads(blob)  # sink 3
''',
    "xxe": '''"""Combination #11 — FAN-OUT × XXE (CWE-611, Python)."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)
PARSER = ET.XMLParser(resolve_entities=True, no_network=False)


@app.route("/fanout")
def fanout():
    xml = request.args.get("xml", "").encode()  # SOURCE
    ET.fromstring(xml, PARSER)
    ET.fromstring(b"<r>" + xml + b"</r>", PARSER)
    ET.fromstring(xml, PARSER)
''',
}


def write(name: str, content: str) -> None:
    path = ROOT / name
    path.write_text(content + "\n")
    print("wrote", path.name)


def main() -> None:
    for key in SANITIZER:
        write(f"sanitizer_combos_{key}.py", SANITIZER[key])
        write(f"comment_string_{key}.py", COMMENT[key])
        write(f"encoded_{key}.py", ENCODED[key])
        write(f"fanout_{key}.py", FANOUT[key])
    print("done:", len(SANITIZER) * 4, "files")


if __name__ == "__main__":
    main()
