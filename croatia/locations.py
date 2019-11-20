from country import Croatia
from location import Location

def porec():
    return _croatian_location("Porec")

def pula():
    return _croatian_location("Pula")

def _croatian_location(name):
    return Location(name, Croatia())
