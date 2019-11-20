from country import WestGermany
from location import Location

def cologne():
    return _west_german_location("Cologne")

def felsberg():
    return _west_german_location("Felsberg")

def frankfurt():
    return _west_german_location("Frankfurt")

def freiburg():
    return _west_german_location("Freiburg")

def karlsruhe():
    return _west_german_location("Karlsruhe")

def pforzheim():
    return _west_german_location("Pforzheim")

def saarlouis():
    return _west_german_location("Saarlouis")

def stuttgart():
    return _west_german_location("Stuttgart")

def west_berlin():
    return _west_german_location("West Berlin")

def wiesbaden():
    return _west_german_location("Wiesbaden")

def _west_german_location(name):
    return Location(name, WestGermany())
