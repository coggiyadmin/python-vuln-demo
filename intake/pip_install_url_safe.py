"""Safe mirror — pinned package from internal index only."""
import subprocess
import sys
from flask import Flask

app = Flask(__name__)
ALLOWED = frozenset({"requests==2.31.0", "flask==3.0.0"})


@app.post("/tools/install")
def install():
    pkg = "requests==2.31.0"
    if pkg not in ALLOWED:
        return "forbidden", 403
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    return "ok"
