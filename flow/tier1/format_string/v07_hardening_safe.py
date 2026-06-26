from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    if not name.isalnum():
        abort(400)
    return "Hello " + name
