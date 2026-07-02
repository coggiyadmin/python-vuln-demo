import logging
from flask import Flask, request
app = Flask(__name__)
@app.route('/g')
def g():
    user = request.args.get('user', '')
    logging.warning('user=%s' % user)  # SINK CWE-134 py percent format in log sink path
