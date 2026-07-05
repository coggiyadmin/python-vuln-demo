from flask import Flask, request
app = Flask(__name__)
@app.route('/x')
def h():
    s = request.args.get('q', '')  # SOURCE
    f = lambda: s  # taint captured in closure
    t = f()
    return '<p>' + t + '</p>'  # SINK
