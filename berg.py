from enum import Enum

class Pavement(Enum):

    Cobbles = 0
    Asphalt = 1

    def describe(self):
        return self.name, self.value

    def __str__(self):
        if self.value == 0:
            return "Cobbles"
        else:
            return "Asphalt"

class Berg(object):

    def __init__(self, name, length, pavement):
        self._name = name
        self._length = length
        self._pavement = pavement

    @property
    def name(self):
        return self._name

    @property
    def length(self):
        return self._length

    @property
    def pavement(self):
        return self._pavement
