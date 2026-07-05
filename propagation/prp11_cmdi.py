from flask import Flask, request
app = Flask(__name__)
import subprocess
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    f = lambda: s  # taint captured in closure
    t = f()
    subprocess.call('grep ' + t, shell=True)  # SINK
