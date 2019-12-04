from singleton import Singleton

class Location(object):
    def __init__(self,name, country, elevation = None,metaclass=Singleton):
        self._name = name
        self._country = country
        if elevation is None:
          self._elevation = 0
        else:
          self._elevation = elevation

    def __repr__(self):
        return 'Location(%r, %r, %r)' % (self.name, self.country, self.elevation)

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def elevation(self):
        return self._elevation

    @property
    def fqnc(self):
        return self.name + " (" + self.country.name + ")"

    def qualified_location(self,country):
        if self.country == country:
            return self.name
        else:
            return self.fqnc

def commune(loc, name):
    return Location('{}/{}'.format(loc.name,name), loc.country, loc.elevation)

def vicinity(loc, name):
    return Location('{} ({})'.format(loc.name,name), loc.country, loc.elevation)
