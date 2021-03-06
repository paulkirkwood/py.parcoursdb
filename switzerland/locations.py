from country import Switzerland
from location import Location

def basel():
    return _swiss_location("Basel")

def bern():
    return _swiss_location("Bern")

def crans_montana():
    return _swiss_location("Crans-Montana", 1670)

def fribourg():
    return _swiss_location("Fribourg")

def geneva():
    return _swiss_location("Geneva")

def la_chaux_de_fonds():
    return _swiss_location("La Chaux-de-Fonds")

def lausanne():
    return _swiss_location("Lausanne")

def lenzerheide():
    return _swiss_location("Lenzerheide")

def leukerbad():
    return _swiss_location("Leukerbad")

def locarno():
    return _swiss_location("Locarno")

def lugano():
    return _swiss_location("Lugano")

def martigny():
    return _swiss_location("Martigny")

def melide():
    return _swiss_location("Melide")

def mendrisio():
    return _swiss_location("Mendrisio")

def mohin():
    return _swiss_location("Mohin")

def neuchatel():
    return _swiss_location("Neuchatel")

def saas_fee():
    return _swiss_location("Saas Fee")

def saint_moritz():
    return _swiss_location("Saint Moritz", 1822)

def sion():
    return _swiss_location("Sion")

def verbier():
    return _swiss_location("Verbier", 1468)

def zurich():
    return _swiss_location("Zurich")

def _swiss_location(name, elevation = None):
    return Location(name, Switzerland(), elevation)
