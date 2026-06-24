# trust_boundary variant: Flask g — request-scoped trusted application context.
from flask import Flask, request, g
app = Flask(__name__)
@app.before_request
def load():
    g.is_admin = request.headers.get("X-Is-Admin", "")  # SINK CWE-501
