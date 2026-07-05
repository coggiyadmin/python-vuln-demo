import subprocess
def resolve_run(_root, _info, cmd):  # SOURCE graphql variable
    subprocess.call("echo " + cmd, shell=True)  # SINK
