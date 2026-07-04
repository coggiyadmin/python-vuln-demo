import smtplib
from flask import Flask, request
app = Flask(__name__)
@app.route("/m")
def m():
    to = request.args.get("to", "")
    smtplib.SMTP("localhost").sendmail("a@b", to, "Subject: hi\r\n\r\nbody")  # SINK CWE-93 CRLF
