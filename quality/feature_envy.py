"""Hygiene — feature envy: method uses other class data heavily."""
class Report:
    def __init__(self, customer): self.customer = customer
class ReportPrinter:
    def print_header(self, report):
        c = report.customer
        return c.name + c.email + c.phone + c.address + c.zip  # envy of Customer fields
