from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route("/p")
def p():
    name = request.args.get("name", "")
    return render_template_string("<h1>Hello " + name + "</h1>")  # SINK CWE-79 render_template_string concat
