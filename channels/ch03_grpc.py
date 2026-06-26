"""CH-03 gRPC handler field → cmdi."""
def handle_request(req):
    import subprocess
    subprocess.call("echo " + req.payload, shell=True)  # SOURCE/SINK
