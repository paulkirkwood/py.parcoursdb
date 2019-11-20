from country import Netherlands
from location import Location

def arnhem():
    return _dutch_location("Arnhem")

def amsterdam():
    return _dutch_location("Amsterdam")

def apeldoorn():
    return _dutch_location("Apeldoorn")

def assen():
    return _dutch_location("Assen")

def berg_en_terblijt():
    return _dutch_location("Berg en Terblijt")

def breda():
    return _dutch_location("Breda")

def elsloo():
    return _dutch_location("Elsloo")

def emmen():
    return _dutch_location("Emmen")

def groningen():
    return _dutch_location("Groningen")

def heerlen():
    return _dutch_location("Heerlen")

def helmond():
    return _dutch_location("Helmond")

def leiden():
    return _dutch_location("Leiden")

def maastricht():
    return _dutch_location("Maastricht")

def meerssen():
    return _dutch_location("Meerssen")

def middleburg():
    return _dutch_location("Middleburg")

def nijmegen():
    return _dutch_location("Nijmegen")

def rotterdam():
    return _dutch_location("Rotterdam")

def scheveningen():
    return _dutch_location("Scheveningen")

def s_hertogenbosch():
    return _dutch_location("'s-Hertogenbosch")

def sint_willebrord():
    return _dutch_location("Sint Willebrord")

def utrecht():
    return _dutch_location("Utrecht")

def valkenburg():
    return _dutch_location("Valkenburg")

def venlo():
    return _dutch_location("Venlo")

def zeeland():
    return _dutch_location("Zeeland")

def zutphen():
    return _dutch_location("Zutphen")

def _dutch_location(name):
    return Location(name, Netherlands())
