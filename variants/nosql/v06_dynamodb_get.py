import boto3
from flask import Flask, request
app = Flask(__name__)
ddb = boto3.client('dynamodb')
@app.route('/q')
def q():
    key = request.args.get('key', '')
    ddb.get_item(TableName='users', Key={'id': {'S': key}})  # SINK CWE-943 DynamoDB key
