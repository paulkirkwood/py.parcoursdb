from enum import Enum

class PaveRating(Enum):

    ZeroStar  = 0
    OneStar    = 1
    TwoStar   = 2
    ThreeStar = 3
    FourStar  = 4
    FiveStar  = 5

    def describe(self):
        return self.name, self.value

    def __str__(self):
        if self.value == 0:
            return ""
        else:
            return '*'  * self.value

class Pave(object):

    def __init__(self, name, length, rating):
        self._name = name
        self._length = length
        self._rating = rating

    @property
    def name(self):
        return self._name

    @property
    def length(self):
        return self._length

    @property
    def rating(self):
        return self._rating
