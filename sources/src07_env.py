import os, subprocess
def main():
    v = os.environ.get("TARGET", "")  # SOURCE SRC-07 env
    subprocess.call("echo " + v, shell=True)  # SINK
