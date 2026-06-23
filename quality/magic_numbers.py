"""Hygiene smell — MAGIC NUMBERS: unexplained literals scattered through logic."""


def price(weight, zone):
    if zone == 3:
        return weight * 4.75 + 12.5 if weight > 30 else weight * 4.75 + 7.25
    return weight * 2.1 + (9.99 if weight > 30 else 4.99)
