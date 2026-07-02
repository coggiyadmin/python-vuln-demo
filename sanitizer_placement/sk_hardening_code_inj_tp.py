"""C1 hardening — code_inj."""
from flask import Flask, request
app = Flask(__name__)
@app.route('/eval')
def eval_route():
    expr = request.args.get('expr', '').replace('import', '')
    eval(expr)
