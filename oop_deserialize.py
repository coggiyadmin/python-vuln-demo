"""Combination #5 — OOP OBJECT FLOW × INSECURE DESERIALIZATION (CWE-502, Python).
Taint injected via __init__, stored on self, fed to pickle.loads (directly and via
a property). Each is a REAL deserialization sink; NO finding = FALSE NEGATIVE."""
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)


class Session:
    def __init__(self, blob):
        self.blob = blob                    # constructor-injected taint

    @property
    def data(self):
        return self.blob                    # property exposes tainted field

    def load_direct(self):
        return pickle.loads(base64.b64decode(self.blob))   # 5a → deserialize sink (CWE-502)

    def load_via_property(self):
        return pickle.loads(base64.b64decode(self.data))   # 5b via property → sink (CWE-502)


@app.route("/restore")
def restore():
    s = Session(request.args.get("s", ""))  # SOURCE → constructor
    s.load_direct()
    s.load_via_property()
    return "ok"
