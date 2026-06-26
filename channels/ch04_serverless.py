"""CH-04 serverless handler event field."""
def lambda_handler(event, context):
    import subprocess
    subprocess.call("grep " + event.get("q", ""), shell=True)
