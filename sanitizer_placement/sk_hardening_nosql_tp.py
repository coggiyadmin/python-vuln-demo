"""C1 hardening — nosql."""
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); db = MongoClient().app.users
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user', '').replace('$', '')
    db.find_one({'user': user})
