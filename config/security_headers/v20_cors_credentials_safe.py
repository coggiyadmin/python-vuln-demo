from flask import Flask, Response
app = Flask(__name__)
@app.after_request
def cors(resp: Response):
    resp.headers['Access-Control-Allow-Origin'] = 'https://app.example.com'  # specific
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp
