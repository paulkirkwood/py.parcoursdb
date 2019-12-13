from country import Austria
from location import Location

def grossglockner():
    return Location("Großglockner", Austria(), 1908)

def innsbruck():
    return _austrian_location("Innsbruck")

def klagenfurt():
    return _austrian_location("Klagenfurt")

def lienz():
    return _austrian_location("Lienz")

def mayrhofen():
    return _austrian_location("Mayrhofen")

def velden_am_worther():
    return _austrian_location("Velden am Worther")

def _austrian_location(name):
    return Location(name, Austria())
