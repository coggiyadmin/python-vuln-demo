from flask import Flask, make_response
app=Flask(__name__)
@app.route("/x")
def x():
  r=make_response("ok"); r.set_cookie("session","abc"); return r  # no secure/httponly -> CWE-614
import hashlib
def h(p): return hashlib.md5(p.encode()).hexdigest()  # CWE-327 weak hash
