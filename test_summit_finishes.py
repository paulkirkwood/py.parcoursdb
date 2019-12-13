import inspect
import pytest
import giro
import tdf
import vuelta

def giro_summit_finishes(edition):
       
    one   = [1936,1937,1938,1948,1953,1955,1956,1957,1961,1965,1971,1977,1980,1981,1984,1987,1988,1993,1997,1998,2001,2004,2013]
    two   = [1939,1951,1959,1960,1973,1974,1975,1978,1982,1989,1992,2006,2014]
    three = [1954,1962,1967,1968,1990,1991,1994,1996,1999,2003,2005,2007,2008,2016,2017]
    four  = [1972,2000,2011,2012,2019]
    five  = [2009,2010,2015]
    seven = [2018]

    year = edition.start_date.year

    return next((1 for yr in one if yr == year),
        next((2 for yr in two if yr == year),
            next((3 for yr in three if yr == year),
                next((4 for yr in four if yr == year),
                    next((5 for yr in five if yr == year),
                        next((7 for yr in seven if yr == year), 0))))))

def tdf_summit_finishes(edition):

    one   = [1953,1958,1959,1961,1962,1963,1964,1965,1967,1969,1980,1991,2007]
    two   = [1970,1972,1977,1981,1982,1993,1998,2005,2010,2012]
    three = [1952,1971,1974,1978,1983,1985,1990,1992,1997,1999,2000,2003,2006,2009,2013,2016]
    four  = [1973,1976,1979,1986,1995,2001,2004,2008,2014,2017,2018]
    five  = [1975,1984,1987,1988,1989,1994,1996,2002]
    six   = [2011,2015]

    year = edition.start_date.year

    return next((1 for yr in one if yr == year),
        next((2 for yr in two if yr == year),
            next((3 for yr in three if yr == year),
                next((4 for yr in four if yr == year),
                    next((5 for yr in five if yr == year),
                        next((6 for yr in six if yr == year), 0))))))

def vuelta_summit_finishes(edition):

    one   = [1972,1975,1977,1979,1981,1982,1983,1984,1988,1989,2014,2015]
    two   = [1985,1990,1998,2005,2008,2010]
    three = [1986,1991,1992,1995,2003,2011,2012,2018]
    four  = [1987,1994,1996,1997,1999,2000,2001,2002,2006,2007,2009,2016]
    five  = [2004,2017]
    six   = [1993]
    seven = [2013]

    year = edition.start_date.year

    return next((1 for yr in one if yr == year),
        next((2 for yr in two if yr == year),
            next((3 for yr in three if yr == year),
                next((4 for yr in four if yr == year),
                    next((5 for yr in five if yr == year),
                        next((6 for yr in six if yr == year),
                            next((7 for yr in seven if yr == year), 0)))))))

test_cases = []
for giro_func in giro.editions():
    edition = giro_func()
    test_cases.append(pytest.param(edition.summit_finishes, giro_summit_finishes(edition),
        id="{} {} summit finishes".format(edition.name, edition.start_date.year)))

for tdf_func in tdf.editions():
    edition = tdf_func()
    test_cases.append(pytest.param(edition.summit_finishes, tdf_summit_finishes(edition),
        id="{} {} summit finishes".format(edition.name, edition.start_date.year)))

for vuelta_func in vuelta.editions():
    edition = vuelta_func()
    test_cases.append(pytest.param(edition.summit_finishes, vuelta_summit_finishes(edition),
        id="{} {} summit finishes".format(edition.name, edition.start_date.year)))

@pytest.mark.parametrize("actual,expected", test_cases)
def test_summit_finishes(actual,expected):
    assert actual == expected
