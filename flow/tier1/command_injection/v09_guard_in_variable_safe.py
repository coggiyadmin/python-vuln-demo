# v09 guard-in-variable
ALLOWED = frozenset({'grep', 'cat'})
import subprocess
def run(bin_name: str, arg: str):
    if bin_name in ALLOWED:
        subprocess.run([bin_name, arg], shell=False)
