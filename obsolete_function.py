"""CWE-477 — Use of Obsolete Function. The deprecated `imp` module is used to load code.
Real vuln; NO finding = FALSE NEGATIVE."""
import imp                                  # obsolete/deprecated module → CWE-477
from flask import Flask

app = Flask(__name__)


@app.route("/mod")
def mod():
    m = imp.new_module("dyn")              # deprecated API
    return str(m)
