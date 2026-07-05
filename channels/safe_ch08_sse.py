"""TN — SSE data HTML-escaped."""
from flask import Flask, request, Response
from markupsafe import escape
app = Flask(__name__)
@app.route('/stream')
def stream():
    msg = request.args.get('msg', '')
    return Response('data: <p>' + str(escape(msg)) + '</p>\n\n', mimetype='text/event-stream')
