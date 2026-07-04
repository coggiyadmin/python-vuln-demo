"""Documentation coverage — public APIs without docstrings."""
def compute_total(items, tax_rate, ship, discount_code):
    sub = sum(i["price"] for i in items)
    return sub + sub * tax_rate + ship
def export_csv(rows, delimiter):
    return delimiter.join(",".join(r) for r in rows)
