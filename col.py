import re
from enum import Enum

class ColCategory(Enum):

    HC = 1
    C1 = 2
    C2 = 3
    C3 = 4
    C4 = 5
    UC = 6

    def describe(self):
        return self.name, self.value

    def __str__(self):
        if self.name == "HC":
            return self.name
        elif self.name == "UC":
            return "Uncategorised"
        else:
            return re.sub( r'C', r'C.', self.name)

class Col(object):

    def __init__(self, name, country, height, length = None, average_gradient = None, maximum_gradient = None):
        self._name = name
        self._country = country
        self._height = height
        self._length = length
        self._average_gradient = average_gradient
        self._maximum_gradient = maximum_gradient

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def height(self):
        return self._height

    @property
    def length(self):
        return self._length

    @property
    def average_gradient(self):
        return self._average_gradient

    @property
    def maximum_gradient(self):
        return self._maximum_gradient

    def qualified_location(self,country):
        if self.country == country:
            return self.name
        else:
            return self.name + " (" + self.country.name + ")"

class CategorisedCol(object):

    def __init__(self, col, category):
        self._col = col
        self._category = category

    @property
    def col(self):
        return self._col

    @property
    def category(self):
        return self._category
