from country import Portugal
from location import Location

def evora():
    return _portuguese_location("Evora")

def estoril():
    return _portuguese_location("Estoril")

def lisbon():
    return _portuguese_location("Lisbon")

def loule():
    return _portuguese_location("Loule")

def vilamoura():
    return _portuguese_location("Vilamoura")

def _portuguese_location(name):
    return Location(name, Portugal())
