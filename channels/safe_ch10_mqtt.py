"""TN — MQTT payload allowlisted."""
import subprocess, re
def on_message(client, userdata, message):
    cmd = message.payload.decode()
    if not re.fullmatch(r'[a-z_]+', cmd):
        return
    subprocess.run(['handle', cmd])
