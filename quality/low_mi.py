"""Low MI — high Halstead volume, CC, and LoC in one module."""
def orchestrate(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    accumulator = 0
    if a and b and c:
        if d or e:
            for idx in range(len(str(f))):
                if idx % 2 == 0 and g:
                    accumulator += idx * h
                elif idx % 3 == 0 and i:
                    accumulator -= idx + j
                else:
                    accumulator ^= k + l
        elif m and n:
            accumulator = sum(x for x in (o, p, a, b) if x)
    return accumulator + len(str(a)) + len(str(b)) + len(str(c))
