"""Code Complexity (McCabe) — HIGH cyclomatic complexity: many decision points,
deep nesting. Also drives a LOW Maintainability Index (high CC + LoC). Refactored
mirror: safe_complex_high_cc.py."""


def classify(a, b, c, d, kind):  # CC ~ 20+ (each and/or/if/elif adds a path)
    if kind == "x":
        if a > 0:
            if b > 0:
                if c > 0:
                    return "xppp" if d > 0 else "xppn"
                elif c < 0:
                    return "xpn"
                else:
                    return "xpz"
            elif b < 0:
                return "xan" if a > b else "xna"
        elif a < 0:
            return "xneg" if b > 0 or c > 0 or d > 0 else "xall"
    elif kind == "y":
        return "y1" if a and b else "y2" if c and d else "y3" if a or b else "y4"
    elif kind == "z":
        for i in range(a):
            if i % 2 == 0 and i % 3 == 0:
                return "zboth"
            elif i % 2 == 0 or i % 3 == 0:
                continue
    return "default"
