"""Hygiene — Fowler god-class smell (high LoC + many responsibilities)."""
class OrderGod:
    def __init__(self): self.items = []; self.tax = 0.0; self.discount = 0.0
    def add(self, x): self.items.append(x)
    def calc_tax(self): self.tax = sum(i["p"] for i in self.items) * 0.08
    def calc_ship(self): return 9.99 if sum(i["p"] for i in self.items) < 50 else 0
    def render_email(self): return "<html>" + "".join(i["n"] for i in self.items) + "</html>"
    def charge_card(self): return "charged"
    def save_db(self): return "saved"
