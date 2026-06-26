from flask import Flask, request, render_template_string, abort
app = Flask(__name__)
@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    if len(name) > 32:
        abort(400)
    return render_template_string("<p>Hello {{ name }}</p>", name=name)
