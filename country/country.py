from singleton import Singleton

class Country(object):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

class Andorra(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Andorra")

class Austria(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Austria")

class Belgium(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Belgium")

class Croatia(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Croatia")

class Denmark(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Denmark")

class Fiume(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Free State of Fiume")

class France(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("France")

class Germany(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Germany")

class Greece(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Greece")

class Ireland(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Ireland")

class Israel(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Israel")

class Italy(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Italy")

class Luxembourg(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Luxembourg")

class Monaco(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Monaco")

class Netherlands(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Netherlands")

class NorthernIreland(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Northern Ireland")

class Portugal(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Portugal")

class SanMarino(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("San Marino")

class Slovenia(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Slovenia")

class Spain(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Spain")

class Switzerland(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Switzerland")

class UnitedKingdom(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("United Kingdom")

class VaticanCity(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Vatican City")

class WestGermany(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("West Germany")

class Yugoslavia(Country, metaclass=Singleton):
    def __init__(self):
        super().__init__("Yugoslavia")
