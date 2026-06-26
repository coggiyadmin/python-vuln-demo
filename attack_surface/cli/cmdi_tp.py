import sys
import subprocess
app = Flask(__name__)
def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""  # SOURCE app entry
    subprocess.call("grep " + q, shell=True)  # SINK CWE-78
