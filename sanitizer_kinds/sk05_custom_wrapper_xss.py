import shlex
def company_sanitize(x: str) -> str:
    return shlex.quote(x)
def run(q: str) -> None:
    import subprocess
    subprocess.call("grep " + company_sanitize(q) + " /var/log/app.log", shell=True)  # SK-05 TN
