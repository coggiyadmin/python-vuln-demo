"""FP-target (upstream cognium-dev#161, py) — eval of a HARDCODED constant expression, not user
input. The engine must not flag a library eval surface when the expression is a constant literal."""


def discount(price: float) -> float:
    # Constant expression literal; `price` is bound into a restricted namespace, not concatenated.
    return eval("price * 0.9", {"__builtins__": {}}, {"price": price})  # constant expr — NOT a sink
