from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    subprocess.call(f"grep {t}", shell=True) if "xss" == "cmdi" else None
    return "<p>" + t + "</p>"
