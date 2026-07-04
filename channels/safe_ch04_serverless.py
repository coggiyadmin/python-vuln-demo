"""TN — serverless event field validated."""
import subprocess
import re
def handler(event, _ctx):
    val = event.get("cmd", "")
    if re.fullmatch(r"[a-z0-9_-]+", val):
        subprocess.call(["echo", val])
