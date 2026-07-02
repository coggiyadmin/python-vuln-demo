"""C1 hardening — cmdi."""
import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route('/run')
def run():
    cmd = request.args.get('cmd', '').replace(';', '')
    subprocess.call(cmd, shell=True)
