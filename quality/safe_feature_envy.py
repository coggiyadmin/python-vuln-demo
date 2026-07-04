"""SAFE — behavior moved to Customer."""
class Customer:
    def __init__(self, name, email, phone, address, zip_code):
        self.name, self.email, self.phone, self.address, self.zip_code = name, email, phone, address, zip_code
    def header_line(self): return self.name + self.email + self.phone + self.address + self.zip_code
