from singleton import Singleton

class Location(object):
    def __init__(self,name, country, metaclass=Singleton):
        self._name = name
        self._country = country

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def fqnc(self):
        return self.name + " (" + self.country.name + ")"

    def qualified_location(self,country):
        if self.country == country:
            return self.name
        else:
            return self.fqnc
