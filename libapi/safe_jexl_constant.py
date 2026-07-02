"""TN — JEXL-style eval on constant expression only. cognium-dev #161."""
import ast

EXPR = "a + b"

def calc(a: int, b: int) -> int:
    # Constant expression tree — not user-controlled code
    tree = ast.parse(EXPR, mode="eval")
    return eval(compile(tree, "<expr>", "eval"), {}, {"a": a, "b": b})
