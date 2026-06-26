import sys, subprocess
def main():
    v = sys.argv[1] if len(sys.argv) > 1 else ""  # SOURCE SRC-08 argv
    subprocess.call("echo " + v, shell=True)  # SINK
