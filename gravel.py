class Gravel(object):

    def __init__(self, name, length):
        self._name = name
        self._length = length

    @property
    def name(self):
        return self._name

    @property
    def length(self):
        return self._length
