import os, subprocess
def test_run():
    q = os.environ.get("Q", "")  # source
    subprocess.call("grep " + q, shell=True)  # SINK — test file
