"""SAFE — documented public APIs."""
def compute_total(items, tax_rate, ship, discount_code):
    """Return order total including tax and shipping."""
    sub = sum(i["price"] for i in items)
    return sub + sub * tax_rate + ship
def export_csv(rows, delimiter):
    """Serialize rows to CSV using delimiter."""
    return delimiter.join(",".join(r) for r in rows)
