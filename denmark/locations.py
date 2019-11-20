from country import Denmark
from location import Location

def herning():
    return _danish_location("Herning")

def horsens():
    return _danish_location("Horsens")

def _danish_location(name):
    return Location(name, Denmark())
