"""SAFE mirror — named constants explain the intent."""
RATE_REMOTE = 4.75
RATE_LOCAL = 2.1
HEAVY_KG = 30
SURCHARGE_HEAVY_REMOTE = 12.5
SURCHARGE_LIGHT_REMOTE = 7.25
SURCHARGE_HEAVY_LOCAL = 9.99
SURCHARGE_LIGHT_LOCAL = 4.99
REMOTE_ZONE = 3


def price(weight, zone):
    heavy = weight > HEAVY_KG
    if zone == REMOTE_ZONE:
        return weight * RATE_REMOTE + (SURCHARGE_HEAVY_REMOTE if heavy else SURCHARGE_LIGHT_REMOTE)
    return weight * RATE_LOCAL + (SURCHARGE_HEAVY_LOCAL if heavy else SURCHARGE_LIGHT_LOCAL)
