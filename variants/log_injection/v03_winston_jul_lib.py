import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger('app')
@app.route("/l")
def l():
    log.warning('user=' + request.args.get('user', ''))  # SINK CWE-117 stdlib logging
