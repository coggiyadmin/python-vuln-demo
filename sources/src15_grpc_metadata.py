import subprocess
def handle(context):
    md = dict(context.invocation_metadata())  # SOURCE grpc metadata
    subprocess.call("echo " + md.get("x-cmd", ""), shell=True)  # SINK
