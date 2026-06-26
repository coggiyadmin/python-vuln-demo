import subprocess
def public_run(user_supplied: str) -> None:
    """Library API — param is NOT an HTTP entry point (TN)."""
    subprocess.call("grep " + user_supplied, shell=True)  # SINK same shape, no route
