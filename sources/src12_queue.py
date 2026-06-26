def on_message(payload: dict):
    q = payload.get("body", "")  # SOURCE SRC-12 queue
    import subprocess
    subprocess.call("echo " + q, shell=True)  # SINK
