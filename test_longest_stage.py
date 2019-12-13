import inspect
import pytest
import giro
import tdf
import vuelta

def giro_longest_stage(edition):
    longest_stages = {
        "1":  [1909,1910,1911,1912],
        "2":  [1921,1927,1971,2011],
        "3":  [1914,1922,1931,1981],
        "4":  [1919,1928,1954,1975,1998],
        "6":  [1929,1930,1940,1953,1958,2014,1979,1999],
        "7":  [1923,1934,1949,1973,1974,2001,2006,2007,2015],
        "8":  [1913,1920,1948,1955,2000,2002,2019],
        "9":  [1925,1926,1935,1947,1950,1964,1978,1980],
        "10": [1924,1932,1951,1990,2009,2018],
        "11": [1946,2010,2012],
        "12": [1936,1962,2017],
        "13": [1961,1967,1984,2013],
        "14": [1966,1970,1972,1977,1987,1994,1995,1997],
        "15": [1937,1939,1956,1986,1993,2004],
        "16": [1938,1976],
        "17": [1933,1985],
        "18": [1960,2016],
        "19": [1952,1992,2003,2008],
        "21": [1957,1959,1982,1996],
        "22": [1965,1968],
        "23": [1969]
    }

    return find_longest_stage(edition, longest_stages, "5")

def tdf_longest_stage(edition):
    longest_stages = {
        "1":  [1937],
        "2":  [1997],
        "3":  [1926,1932,1947,1978,1980,2007],
        "4":  [1905,1913,1914,1976,1977,1983,1991,1998,2015,2016],
        "5":  [1919,1920,1921,1922,1923,1924,1933,1934,1950,1963,1990,1995,2008],
        "6":  [1903,1904,1931,1976,1989,1994,2010,2011],
        "8":  [1953,1984],
        "9":  [1928,1939,1954,1955,1970,1987],
        "10": [1981,2004],
        "11": [1929,1965,1986],
        "12": [1911,1912,1985,1992,1993],
        "13": [1907,1908,1909,1910,1927,1975,1999,2006,2012],
        "14": [1974,1979],
        "15": [1930,1935,1936,1938,1968,2001,2002,2013],
        "16": [2014],
        "17": [1925,1973,1982,1996,2005],
        "18": [1972],
        "19": [1966,2017],
        "20": [1961,1969,1988,2000],
        "21": [1948,1949,1957,1964,1967],
        "22": [1956,1959,1962],
        "23": [1952],
        "24": [1951,1958]
    }

    return find_longest_stage(edition, longest_stages, "7")

def vuelta_longest_stage(edition):

    longest_stages = {
        "1":  [1947,1984],
        "1B": [1969],
        "2":  [1971,1982,1985,1993,1998,2004],
        "3":  [1948,1957,1965,1970,1983,1999,2000,2006],
        "4":  [1991,2005,2009],
        "5":  [1960,1989,1997],
        "7":  [1936,1942,1977,1984,1994,2008,2017],
        "8":  [1978,1992,2014],
        "10": [1945,1979,1981,1990,2003,2007],
        "11": [1959,1966,1967,1972,1980,2010,2018],
        "12": [1956,1962,1973,2002],
        "13": [1946,1963,1964,2016],
        "14": [1955,1961,1968,1975,1976,2015],
        "15": [2001,2013],
        "16": [1986,1987,1996],
        "17": [1988,2011],
        "18": [1950,2012],
        "20": [1941],
    }

    return find_longest_stage(edition, longest_stages, "6")

def find_longest_stage(edition, longest_stages, default_stage_id):
    year = edition.start_date.year
    for stage_id, years in longest_stages.items():
        hit = next((stage_id for yr in years if yr == year), None)
        if hit is not None:
            return stage_id
    return default_stage_id

test_cases = []
for giro_func in giro.editions():
    edition = giro_func()
    test_cases.append(pytest.param(edition.longest_stage().id, giro_longest_stage(edition),
        id="{} {} longest stage".format(edition.name, edition.start_date.year)))

for tdf_func in tdf.editions():
    edition = tdf_func()
    test_cases.append(pytest.param(edition.longest_stage().id, tdf_longest_stage(edition),
        id="{} {} longest stage".format(edition.name, edition.start_date.year)))

for vuelta_func in vuelta.editions():
    edition = vuelta_func()
    test_cases.append(pytest.param(edition.longest_stage().id, vuelta_longest_stage(edition),
        id="{} {} longest stage".format(edition.name, edition.start_date.year)))

@pytest.mark.parametrize("actual,expected", test_cases)
def test_longest_stage(actual,expected):
    assert actual == expected
