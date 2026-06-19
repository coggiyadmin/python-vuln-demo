"""CWE-494 — Download of Code Without Integrity Check. A script is fetched over the network
and executed with no signature/hash verification. (Engine gap — cf #93.) FN probe."""
import subprocess
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/self-update")
def self_update():
    code = requests.get("http://updates.internal/install.sh").text  # no integrity check
    subprocess.run(["bash", "-c", code])       # executes unverified downloaded code → CWE-494
    return "updated"
