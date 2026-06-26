"""TN — subprocess argv list, no shell."""
import subprocess

def grep(pattern: str) -> None:
    subprocess.run(["grep", pattern, "/var/log/app.log"], check=False, shell=False)
