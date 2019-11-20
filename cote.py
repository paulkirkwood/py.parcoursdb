class Cote(object):

    def __init__(self, name, height):
        self._name = name
        self._height = height

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        return self._height
