"""CH-02 WebSocket onmessage → DOM XSS."""
def on_message(ws, message):
    payload = message  # SOURCE
    return "<p>" + payload + "</p>"  # SINK CWE-79
