import country
from location import Location

class TestLocation:

    def test_location(self):

        belgium = country.Belgium()
        france = country.France()

        paris = Location("Paris", france)
        nantes = Location("Nantes", france)

        assert paris.qualified_location(france) == "Paris"
        assert paris.qualified_location(belgium) == "Paris (France)"
