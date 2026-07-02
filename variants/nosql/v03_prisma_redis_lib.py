from flask import Flask, request
import redis
app = Flask(__name__)
r = redis.Redis()
@app.route("/k")
def k():
    key = request.args.get("key", "")
    r.execute_command("GET", key)  # SINK CWE-943 redis command injection style
