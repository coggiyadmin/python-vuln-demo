"""SAFE — decomposed order services (refactored smell mirror)."""
class OrderItems:
    def __init__(self): self.items = []
    def add(self, x): self.items.append(x)
class TaxService:
    def calc(self, items): return sum(i["p"] for i in items) * 0.08
class EmailRenderer:
    def render(self, items): return "<html>" + "".join(i["n"] for i in items) + "</html>"
