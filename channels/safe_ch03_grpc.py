"""TN — gRPC payload shell-escaped."""
import subprocess
import shlex
def handle_request(req):
    subprocess.call(["echo", shlex.quote(req.payload)])
