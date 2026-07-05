import os
def test_render():
    q = os.environ.get("Q", "")
    assert ("<p>" + q + "</p>")  # SINK — test file
