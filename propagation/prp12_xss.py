from flask import Flask, request
app = Flask(__name__)
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    globals()['_G'] = s  # store in module global
    t = globals()['_G']
    return '<p>' + t + '</p>'  # SINK
