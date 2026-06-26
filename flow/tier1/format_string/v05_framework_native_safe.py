from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return "Hello %s" % name
