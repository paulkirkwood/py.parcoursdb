from country import Greece
from location import Location

def athens():
    return _greek_location("Athens")

def eleusis():
    return _greek_location("Eleusis")

def ioannina():
    return _greek_location("Ioannina")

def missolonghi():
    return _greek_location("Missolonghi")

def naupactus():
    return _greek_location("Naupactus")

def _greek_location(name):
    return Location(name, Greece())
