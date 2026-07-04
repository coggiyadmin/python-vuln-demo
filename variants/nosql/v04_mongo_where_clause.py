from flask import Flask, request
import pymongo
app = Flask(__name__)
@app.route("/m")
def m():
    name = request.args.get("name", "")
    pymongo.MongoClient().app.users.find({"$where": "this.name == '" + name + "'"})  # SINK CWE-943
