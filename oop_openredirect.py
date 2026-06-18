"""Combination #5 — OOP OBJECT FLOW × OPEN REDIRECT (CWE-601, Python). Taint
injected via __init__, stored on self, used in a method sink (directly and via a
property). Each is a REAL open redirect; NO finding = FALSE NEGATIVE."""
from flask import Flask, request, redirect

app = Flask(__name__)


class Navigation:
    def __init__(self, url):
        self.url = url                     # constructor-injected taint

    @property
    def destination(self):
        return self.url                    # property exposes tainted field

    def go_direct(self):
        return redirect(self.url)           # 5a: field → redirect sink (CWE-601)

    def go_via_property(self):
        return redirect(self.destination)   # 5b: via property → sink (CWE-601)


@app.route("/login")
def login():
    nav = Navigation(request.args.get("next", ""))  # SOURCE → constructor
    return nav.go_direct()
