import os
def test_read():
    q = os.environ.get("Q", "")
    open("/data/" + q).read()  # SINK — test file
