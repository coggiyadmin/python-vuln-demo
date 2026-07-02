"""TN — wait for fixed process, not user shell. cognium-dev #124."""
import subprocess

def wait_fixed() -> int:
    return subprocess.run(["echo", "ok"], capture_output=True).returncode
