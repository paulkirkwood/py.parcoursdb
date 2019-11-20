from belgium     import antwerp, ans, bruges, charleroi, deinze, esneux, evergem, gentbrugge, ghent, harelbeke, huy
from belgium     import liege, marcinelle, mariakerke, meerbeke, mons, oudenaarde, rochefort, rocourt
from belgium     import sint_niklaas, spa, tournai, verviers, wevelgem, wetteren
from berg        import Berg, Pavement
from classic     import Classic, ParisRoubaix, ParisTours, TourOfFlanders
from cote        import Cote
from datetime    import datetime
from france      import argenteuil, blois, brou, chantilly, chartres, chatou, chaville, compiegne, creteil
from france      import la_loupe, montlhery, paris, porte_maillot, saint_arnoult_en_yvelines, roubaix
from france      import saint_denis, saint_germain, suresnes, tours, versailles
from gravel      import Gravel
from italy       import bergamo, cantu, como, lecco, milan, mendrisio, monza, san_remo, varese
from netherlands import berg_en_terblijt, breda, elsloo, helmond, heerlen, maastricht, meerssen, valkenburg
from operator    import itemgetter
from pave        import Pave, PaveRating

class ClassicBuilder(object):

    def __init__(self, year, month, day, distance):
        self._year = year
        self._month = month
        self._day = day
        self._distance = distance
        self._cotes = {}

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def distance(self):
        return self._distance

    def cote(self, name, height, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._cotes:
            raise DuplicateCoteError( "There is already a Cote at that point in the race" )
        self._cotes[km] = Cote(name, height)

    def _find(self, editions, default_value):
        for key, years in editions.items():
            if self.year in years:
                return key
        return default_value

    def _list(self, x, y):
        return list(range(x, y + 1))

    def _dict_to_list(self, dict, index = False, reverse = False):
        l = []

        if (reverse):
            #
            # Paris-Roubaix pave sectors countdown towards Roubaix
            #
            all_sector_ids = list( map( lambda x : x['id'], dict.values() ) )
            unique_sector_ids = set(all_sector_ids)
            number_of_sectors = len(unique_sector_ids) + 1

            sectors = sorted(dict.values(), key=itemgetter('km'))
            for sector in sectors:
                l.append((sector['km'], sector['id'] + number_of_sectors, sector['sector']))
        else:
            keys = sorted(dict.keys())
            idx = 1
            for k in keys:
                if (index):
                    l.append((k, idx, dict[k]))
                    idx += 1
                else:
                    l.append((k, dict[k]))
        return l

class AmstelGoldRaceBuilder(ClassicBuilder):

    def __init__(self, year, day, distance, month = 4):
        super().__init__(year, month, day, distance)

    def build(self):
        start_locations = [
            ( breda(),   [ 1966 ]),
            ( helmond(), self._list( 1967, 1970 ) ),
            ( heerlen(), self._list( 1970, 1997 ) ),
        ]

        finish_locations = [
            ( meerssen(),   [ 1966 ] + self._list( 1969, 1990 ) ),
            ( elsloo(),     [ 1968 ] ),
            ( maastricht(), self._list( 1991, 2002 ) ),
            (valkenburg(),  self._list( 2003, 2012 ) ),
        ]

        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), berg_en_terblijt()),
            name     = "Amstel Gold Race",
            start    = self._find(dict(start_locations), maastricht()),
        )

class E3HarelbekeBuilder(ClassicBuilder):

    def __init__(self, year, day, distance, month = 3):
        super().__init__(year, month, day, distance)

    def build(self):
        names = [
            ("Harelbeke-Antwerp-Harelbeke", self._list( 1958, 1961 ) ),
            ("E3 Prijs Vlaanderen",         self._list( 1962, 2013 ) ),
            ("E3 Harelbeke",                self._list( 2014, 2018 ) )
        ]

        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = harelbeke(),
            name     = self._find(dict(names), "E3 BinckBank Classic"),
            start    = harelbeke(),
        )

class GentWevelgemBuilder(ClassicBuilder):

    def __init__(self, year, day, distance, month = 4):
        super().__init__(year, month, day, distance)

    def build(self):
        if self.year > 2013:
            start = deinze()
        else:
            start = ghent()
        
        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = wevelgem(),
            name     = "Gent-Wevelgem",
            start    = start
        )

class LaFlecheWallonneBuilder(ClassicBuilder):

    def build(self):
        start_locations = [
            (tournai()   , self._list( 1936, 1938 ) ),
            (mons()      , self._list( 1939, 1947 ) + [ 1980 ] ),
            (charleroi() , self._list( 1948, 1959 ) + self._list( 1982, 1984 ) ),
            (liege()     , self._list( 1960, 1971 ) ),
            (verviers()  , self._list( 1972, 1978 ) ),
            (esneux()    , [ 1979] ),
            (huy()       , [ 1985] ),
        ]

        finish_locations = [
            (liege(),      [ 1936 ] + self._list( 1946, 1959 ) ),
            (ans(),        [ 1937 ]),
            (rocourt(),    self._list( 1938, 1941 ) ),
            (marcinelle(), [ 1942 ] + self._list( 1965, 1973 ) + [1979] ),
            (charleroi(),  self._list( 1943, 1954 ) + self._list( 1960, 1964 ) ),
            (verviers(),   self._list( 1974, 1978 ) ),
            (spa(),        [ 1980, 1982 ] ),
            (mons(),       [ 1981 ] ),
        ]

        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), huy()),
            name     = "La Flèche Wallonne",
            start    = self._find(dict(start_locations), spa())
        )

class LiegeBastogneLiegeBuilder(ClassicBuilder):

    def build(self):
        finish_locations = [ (ans(), self._list( 1992, 2018 ) ) ]

        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), liege()),
            name     = "Liège-Bastogne-Liège",
            start    = liege()
        )

class MilanoSanRemoBuilder(ClassicBuilder):

    def __init__(self, year, day, distance, month = 3):
        super().__init__(year, month, day, distance)

    def build(self):
        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = san_remo(),
            name     = "Milano-San Remo",
            start    = milan()
        )

    def passo_del_turchino(self, km):
        self.cote( "Passo del Turchino", 532, km )

    def capo_mele(self, km):
        self.cote( "Capo Mele", 67, km )

    def capo_cervo(self, km):
        self.cote( "Capo Cervo", 61, km )

    def capo_berta(self, km):
        self.cote( "Capo Berta", 130, km )

    def cipressa(self, km):
        self.cote( "Cipressa", 239, km )

    def poggio(self, km):
        self.cote( "Poggio", 160, km )

class OmloopHetVolkBuilder(ClassicBuilder):

    def build(self):
        names = [
             ("Omloop van Vlaanderen", [ 1945, 1946 ]),
             ("Omloop Het Volk",       self._list(1947, 2008) ),
        ]

        finish_locations = [ (lokeren(), self._list(1996, 2007) ) ]

        return Classic(
            bergs    = self._dict_to_list(self._bergs),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), ghent()),
            name     = self._find(dict(names), "Omloop Het Nieuwsblad"),
            start    = ghent(),
        )

class ParisRoubaixBuilder(ClassicBuilder):

    def __init__(self, year, month, day, distance):
        super().__init__(year, month, day, distance)
        self._pave = {}
        self._sector_id = -1
        self.__class__ = SingleSectorParisRoubaixBuilder

    def five_star_pave(self, name, length, km):
        self._add_pave(Pave(name, length, PaveRating.FiveStar), km)

    def four_star_pave(self, name, length, km):
        self._add_pave(Pave(name, length, PaveRating.FourStar), km)

    def three_star_pave(self, name, length, km):
        self._add_pave(Pave(name, length, PaveRating.ThreeStar), km)

    def two_star_pave(self, name, length, km):
        self._add_pave(Pave(name, length, PaveRating.TwoStar), km)

    def one_star_pave(self, name, length, km):
        self._add_pave(Pave(name, length, PaveRating.OneStar), km)

    def build(self):
        start_locations = [
            ( argenteuil(),    [ 1938]),
            ( chantilly(),     self._list( 1966, 1976 ) ),
            ( chatou(),        [ 1898, 1899 ] + self._list( 1902, 1913 ) ),
            ( porte_maillot(), [ 1896, 1897, 1901 ] + self._list( 1929, 1937 ) + [ 1939 ] ),
            ( saint_denis(),   self._list( 1943, 1965 ) ),
            ( saint_germain(), [ 1900 ] ),
            ( suresnes(),      [ 1914 ] + self._list( 1919, 1928 ) )
        ]

        return ParisRoubaix(
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = roubaix(),
            name     = "Paris-Roubaix",
            pave   = self._dict_to_list(dict = self._pave, reverse = True),
            start    = self._find(dict(start_locations), compiegne()),
        )

    def _add_pave(self, pave, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._pave:
            raise DuplicatePaveError( "There is already Pave at that point in the race" )
        self._pave[km] = { 'km': km, 'id': self._sector_id, 'sector': pave }

class SingleSectorParisRoubaixBuilder(ParisRoubaixBuilder):

    def enable_multiple_sectors(self):
        self.__class__ = MultiSectorParisRoubaixBuilder

    def _add_pave(self, pave, km):
        super()._add_pave(pave, km)
        self._sector_id -= 1

class MultiSectorParisRoubaixBuilder(ParisRoubaixBuilder):

    def disable_multiple_sectors(self):
        self._sector_id -= 1
        self.__class__ = SingleSectorParisRoubaixBuilder

class ParisToursBuilder(ClassicBuilder):

    def __init__(self, year, day, distance, month = 10):
        super().__init__(year, month, day, distance)
        self._gravel = {}
        self._sector_id = -1

    def build(self):
        start_locations = [
            ( tours(),                     self._list( 1974, 1977 ) ),
            ( blois(),                     self._list( 1978, 1984 ) ),
            ( creteil(),                   self._list( 1985, 1987 ) ),
            ( chaville(),                  self._list( 1988, 1990 ) ),
            ( saint_arnoult_en_yvelines(), self._list( 1993, 2008 ) + [ 2014 ] ),
            ( chartres(),                  [ 2009 ]),
            ( la_loupe(),                  [ 2010 ]),
            ( brou(),                      [ 2017 ]),
        ]

        finish_locations = [
            ( versailles(), self._list(1974, 1977) ),
            ( montlhery(),  [ 1978 ] ),
            ( chaville(),   self._list(1979, 1987) ),
        ]

        names = [
            ( "Grand Prix d'Automne", self._list( 1976, 1987 ) ),
        ]

        return ParisTours(
            cotes    = self._dict_to_list(self._cotes),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), tours()),
            gravel   = self._dict_to_list(dict = self._gravel, reverse = True),
            name     = self._find(dict(names), "Paris-Tours"),
            start    = self._find(dict(start_locations), paris()),
        )

    def gravel(self, name, length, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._gravel:
            raise DuplicateGravelError( "There is already a gravel sector at that point in the race" )
        self._gravel[km] = { 'km': km, 'id': self._sector_id, 'sector': Gravel(name, length) }
        self._sector_id -= 1

class TourOfFlandersBuilder(ClassicBuilder):

    def __init__(self, year, month, day, distance):
        super().__init__(year, month, day, distance)
        self._bergs = {}
        self._pave = {}

    def asphalt_berg(self, name, length, km):
        self.berg(Berg(name, length, Pavement.Asphalt), km)

    def cobbled_berg(self, name, length, km):
        self.berg(Berg(name, length, Pavement.Cobbles), km)

    def berg(self, berg, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._bergs:
            raise DuplicateBergError( "There is already a Berg at that point in the race" )
        self._bergs[km] = berg

    def pave(self, name, length, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._pave:
            raise DuplicatePaveError( "There is already Pave at that point in the race" )
        self._pave[km] = Pave(name, length, PaveRating.ZeroStar)

    def build(self):
        start_locations = [
            ( sint_niklaas(), self._list( 1977, 1997 ) ),
            ( bruges(),       self._list( 1998, 2016 ) ),
            ( antwerp(),      self._list( 2017, 2019 ) )
        ]

        finish_locations = [
            ( mariakerke(), [ 1913 ] ),
            ( evergem(),    [ 1914 ] ),
            ( gentbrugge(), self._list( 1919, 1923 ) + self._list( 1962, 1972 ) ),
            ( wetteren(),   self._list( 1928, 1941 ) + self._list( 1945, 1961 ) ),
            ( meerbeke(),   self._list( 1973, 2011 ) ),
            ( oudenaarde(), self._list( 2012, 2019 ) ),
        ]

        return TourOfFlanders(
            bergs    = self._dict_to_list(self._bergs, True),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), ghent()),
            name     = "Tour of Flanders",
            pave     = self._dict_to_list(self._pave, True),
            start    = self._find(dict(start_locations), ghent()),
        )

class TourOfLombardyBuilder(ClassicBuilder):

    def build(self):

        start_locations = [
            ( milan(),     self._list( 1905, 1984 ) + self._list( 1990, 1994 ) + [ 2010, 2011 ] ),
            ( como(),      self._list( 1985, 1989 ) + [ 2003, 2014, 2016 ] ),
            ( varese(),    self._list( 1995, 2001 ) + [ 2001, 2007, 2008, 2009 ] ),
            ( mendrisio(), [ 2004, 2005, 2006 ] ),
            ( cantu(),     [ 2002 ] ),
        ]

        finish_locations = [
            ( monza(),   [ 1990, 1991, 1992, 1993, 1994 ] ),
            ( lecco(),   [ 2011, 2012, 2013 ] ),
            ( milan(),   self._list( 1905, 1960 ) + [ 1985, 1986, 1987, 1988, 1989 ] ),
            ( bergamo(), self._list( 1995, 2003 ) + [ 2014, 2016 ] ),
        ]

        return Classic(
            cotes    = self._dict_to_list(self._cotes),
            date     = datetime(self.year, self.month, self.day),
            distance = self.distance,
            finish   = self._find(dict(finish_locations), bergamo()),
            name     = "Il Lombardia",
            start    = self._find(dict(start_locations), como()),
        )
