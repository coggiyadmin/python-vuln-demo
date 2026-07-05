from flask import Flask, request
app = Flask(__name__)
import subprocess
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    globals()['_G'] = s  # store in module global
    t = globals()['_G']
    subprocess.call('grep ' + t, shell=True)  # SINK
