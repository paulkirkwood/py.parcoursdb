from country import Germany
from location import Location

def cologne():
    return _german_location("Cologne")

def dusseldorf():
    return _german_location("Dusseldorf")

def freiburg():
    return _german_location("Freiburg")

def koblenz():
    return _german_location("Koblenz")

def munster():
    return _german_location("Münster")

def saarbrucken():
    return _german_location("Saarbrücken")

def pforzheim():
    return _german_location("Pforzheim")

def karlsruhe():
    return _german_location("Karlsruhe")

def _german_location(name):
    return Location(name, Germany())
