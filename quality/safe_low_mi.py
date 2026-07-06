"""SAFE — decomposed helpers (higher MI)."""
def _even(idx, g, h):
    return idx * h if idx % 2 == 0 and g else 0

def _odd(idx, i, j, k, l):
    return -(idx + j) if idx % 3 == 0 and i else k + l

def orchestrate(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    acc = 0
    if a and b and c and (d or e):
        for idx in range(len(str(f))):
            acc += _even(idx, g, h) or _odd(idx, i, j, k, l)
    elif m and n:
        acc = sum(x for x in (o, p, a, b) if x)
    return acc + len(str(a)) + len(str(b)) + len(str(c))
