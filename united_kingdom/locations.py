from country import UnitedKingdom
from location import Location

def brighton():
    return _british_location("Brighton")

def cambridge():
    return _british_location("Cambridge")

def canterbury():
    return _british_location("Canterbury")

def dover():
    return _british_location("Dover")

def harrogate():
    return _british_location("Harrogate")

def leeds():
    return _british_location("Leeds")

def london():
    return _british_location("London")

def plymouth():
    return _british_location("Plymouth")

def portsmouth():
    return _british_location("Portsmouth")

def sheffield():
    return _british_location("Sheffield")

def york():
    return _british_location("York")

def _british_location(name):
    return Location(name, UnitedKingdom())
