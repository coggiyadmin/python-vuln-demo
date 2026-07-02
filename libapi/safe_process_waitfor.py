"""TN — Process.waitFor on fixed child, not shell (#124)."""
import subprocess

def wait_fixed() -> int:
    p = subprocess.Popen(["echo", "ok"], stdout=subprocess.PIPE)
    return p.wait()
