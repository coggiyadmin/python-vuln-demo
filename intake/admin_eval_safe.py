"""Safe mirror — constant expression only."""
from flask import Flask

app = Flask(__name__)


@app.post("/admin/eval")
def eval_expr():
    return str(1 + 1)
