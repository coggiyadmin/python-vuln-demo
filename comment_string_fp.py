"""Combination #9 — COMMENT / STRING-LITERAL specificity (Python).
Sink syntax appears only inside comments and string literals, never executed
on tainted data. The scanner MUST produce ZERO security findings. Any finding
is a FALSE POSITIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/docs")
def docs():
    user = request.args.get("u", "")  # a real source, but never reaches a real sink

    # The following are DOCUMENTATION / examples, not executed:
    #   os.system("rm -rf " + user)
    #   cursor.execute("SELECT * FROM t WHERE x='" + user + "'")
    #   eval(user)

    example_sql = "SELECT * FROM users WHERE name = '\" + name + \"'"  # string literal
    example_cmd = "os.system('whoami')"                                 # string literal
    snippet = "eval(request.args.get('x'))"                             # string literal

    # `user` is only echoed back as plain text, no sink:
    return "examples: " + example_sql + example_cmd + snippet
