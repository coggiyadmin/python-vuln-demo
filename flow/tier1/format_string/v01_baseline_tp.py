from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    fmt = request.args.get("fmt", "{name}")  # SOURCE
    return fmt.format(name="guest", config=app.config)  # SINK CWE-134
