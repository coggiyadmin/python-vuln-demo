"""CH-08 server-sent events — event data reflected into HTML."""
from flask import Flask, request, Response
app = Flask(__name__)
@app.route('/stream')
def stream():
    msg = request.args.get('msg', '')  # SOURCE
    return Response('data: <p>' + msg + '</p>\n\n', mimetype='text/event-stream')  # SINK CWE-79
