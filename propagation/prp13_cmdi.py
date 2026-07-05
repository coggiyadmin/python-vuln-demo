from flask import Flask, request
app = Flask(__name__)
import subprocess
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    import json
    t = json.loads(json.dumps({'v': s}))['v']  # serialize round-trip
    subprocess.call('grep ' + t, shell=True)  # SINK
