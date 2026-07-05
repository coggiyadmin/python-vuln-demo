"""CH-10 MQTT message handler — payload -> shell."""
import os
def on_message(client, userdata, message):
    cmd = message.payload.decode()  # SOURCE MQTT payload
    os.system('handle ' + cmd)  # SINK CWE-78
