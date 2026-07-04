# v10 allowlist-set
SAFE_ARGS = {('grep', '/var/log/app.log')}
import subprocess
def run(cmd: str, path: str):
    if (cmd, path) in SAFE_ARGS:
        subprocess.run([cmd, path], shell=False)
