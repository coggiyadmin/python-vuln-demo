# v09 guard-in-variable
ALLOWED = frozenset({'1+1', '2*3'})
def eval_expr(expr: str):
    if expr in ALLOWED:
        return eval(expr, {"__builtins__": {}}, {})
