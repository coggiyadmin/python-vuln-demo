import smtplib
from flask import Flask, request
app = Flask(__name__)
@app.route("/m")
def m():
    subj = request.args.get("subj", "")
    smtplib.SMTP("localhost").sendmail("a@b.c", "d@e.f", "Subject: " + subj + "\r\nBcc: evil@x.y\r\n\n")  # SINK CWE-113
