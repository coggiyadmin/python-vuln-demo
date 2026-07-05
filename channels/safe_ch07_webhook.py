"""TN — webhook field allowlisted before shell."""
import subprocess, re
def on_webhook(event):
    name = event['repository']['name']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', name):
        return
    subprocess.run(['git', 'clone', '/srv/' + name])
