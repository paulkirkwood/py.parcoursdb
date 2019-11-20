import inspect
import paris_roubaix

class TestParisRoubaix:

    def test_paris_roubaix_1896(self):
        edition = paris_roubaix.paris_roubaix_1896()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Porte Maillot, Paris (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1897(self):
        edition = paris_roubaix.paris_roubaix_1897()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Porte Maillot, Paris (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1898(self):
        edition = paris_roubaix.paris_roubaix_1898()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Chatou (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1899(self):
        edition = paris_roubaix.paris_roubaix_1899()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Chatou (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1900(self):
         edition = paris_roubaix.paris_roubaix_1900()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Germain (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1901(self):
         edition = paris_roubaix.paris_roubaix_1901()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1902(self):
         edition = paris_roubaix.paris_roubaix_1902()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1903(self):
         edition = paris_roubaix.paris_roubaix_1903()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1904(self):
         edition = paris_roubaix.paris_roubaix_1904()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1905(self):
         edition = paris_roubaix.paris_roubaix_1905()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1906(self):
         edition = paris_roubaix.paris_roubaix_1906()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1907(self):
         edition = paris_roubaix.paris_roubaix_1907()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1908(self):
         edition = paris_roubaix.paris_roubaix_1908()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1909(self):
         edition = paris_roubaix.paris_roubaix_1909()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1910(self):
         edition = paris_roubaix.paris_roubaix_1910()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1911(self):
         edition = paris_roubaix.paris_roubaix_1911()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1912(self):
         edition = paris_roubaix.paris_roubaix_1912()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1913(self):
         edition = paris_roubaix.paris_roubaix_1913()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chatou (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1914(self):
         edition = paris_roubaix.paris_roubaix_1914()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1919(self):
         edition = paris_roubaix.paris_roubaix_1919()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1920(self):
         edition = paris_roubaix.paris_roubaix_1920()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1921(self):
         edition = paris_roubaix.paris_roubaix_1921()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1922(self):
         edition = paris_roubaix.paris_roubaix_1922()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1923(self):
         edition = paris_roubaix.paris_roubaix_1923()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1924(self):
         edition = paris_roubaix.paris_roubaix_1924()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1925(self):
         edition = paris_roubaix.paris_roubaix_1925()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1926(self):
         edition = paris_roubaix.paris_roubaix_1926()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1927(self):
         edition = paris_roubaix.paris_roubaix_1927()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1928(self):
         edition = paris_roubaix.paris_roubaix_1928()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Suresnes, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1929(self):
         edition = paris_roubaix.paris_roubaix_1929()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1930(self):
         edition = paris_roubaix.paris_roubaix_1930()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1931(self):
         edition = paris_roubaix.paris_roubaix_1931()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1932(self):
         edition = paris_roubaix.paris_roubaix_1932()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1933(self):
         edition = paris_roubaix.paris_roubaix_1933()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1934(self):
         edition = paris_roubaix.paris_roubaix_1934()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1935(self):
         edition = paris_roubaix.paris_roubaix_1935()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1936(self):
         edition = paris_roubaix.paris_roubaix_1936()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1937(self):
         edition = paris_roubaix.paris_roubaix_1937()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1938(self):
         edition = paris_roubaix.paris_roubaix_1938()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Argenteuil (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1939(self):
         edition = paris_roubaix.paris_roubaix_1939()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Porte Maillot, Paris (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1943(self):
         edition = paris_roubaix.paris_roubaix_1943()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1944(self):
         edition = paris_roubaix.paris_roubaix_1944()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1945(self):
         edition = paris_roubaix.paris_roubaix_1945()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1946(self):
         edition = paris_roubaix.paris_roubaix_1946()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1947(self):
         edition = paris_roubaix.paris_roubaix_1947()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1948(self):
         edition = paris_roubaix.paris_roubaix_1948()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1949(self):
         edition = paris_roubaix.paris_roubaix_1949()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1950(self):
         edition = paris_roubaix.paris_roubaix_1950()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1951(self):
         edition = paris_roubaix.paris_roubaix_1951()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1952(self):
         edition = paris_roubaix.paris_roubaix_1952()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1953(self):
         edition = paris_roubaix.paris_roubaix_1953()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1954(self):
         edition = paris_roubaix.paris_roubaix_1954()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1955(self):
         edition = paris_roubaix.paris_roubaix_1955()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1956(self):
         edition = paris_roubaix.paris_roubaix_1956()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1957(self):
         edition = paris_roubaix.paris_roubaix_1957()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1958(self):
         edition = paris_roubaix.paris_roubaix_1958()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1959(self):
         edition = paris_roubaix.paris_roubaix_1959()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1960(self):
         edition = paris_roubaix.paris_roubaix_1960()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1961(self):
         edition = paris_roubaix.paris_roubaix_1961()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1962(self):
         edition = paris_roubaix.paris_roubaix_1962()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1963(self):
         edition = paris_roubaix.paris_roubaix_1963()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1964(self):
         edition = paris_roubaix.paris_roubaix_1964()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1965(self):
         edition = paris_roubaix.paris_roubaix_1965()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Saint-Denis (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1966(self):
         edition = paris_roubaix.paris_roubaix_1966()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1967(self):
         edition = paris_roubaix.paris_roubaix_1967()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1968(self):
         edition = paris_roubaix.paris_roubaix_1968()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1969(self):
         edition = paris_roubaix.paris_roubaix_1969()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1970(self):
         edition = paris_roubaix.paris_roubaix_1970()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1971(self):
         edition = paris_roubaix.paris_roubaix_1971()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1972(self):
         edition = paris_roubaix.paris_roubaix_1972()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1973(self):
         edition = paris_roubaix.paris_roubaix_1973()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1974(self):
         edition = paris_roubaix.paris_roubaix_1974()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1975(self):
         edition = paris_roubaix.paris_roubaix_1975()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1976(self):
         edition = paris_roubaix.paris_roubaix_1976()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Chantilly (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1977(self):
         edition = paris_roubaix.paris_roubaix_1977()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1978(self):
         edition = paris_roubaix.paris_roubaix_1978()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1979(self):
         edition = paris_roubaix.paris_roubaix_1979()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1980(self):
         edition = paris_roubaix.paris_roubaix_1980()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1981(self):
         edition = paris_roubaix.paris_roubaix_1981()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1982(self):
         edition = paris_roubaix.paris_roubaix_1982()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1983(self):
         edition = paris_roubaix.paris_roubaix_1983()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1984(self):
         edition = paris_roubaix.paris_roubaix_1984()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1985(self):
         edition = paris_roubaix.paris_roubaix_1985()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1986(self):
         edition = paris_roubaix.paris_roubaix_1986()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1987(self):
         edition = paris_roubaix.paris_roubaix_1987()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1988(self):
         edition = paris_roubaix.paris_roubaix_1988()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1989(self):
         edition = paris_roubaix.paris_roubaix_1989()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1990(self):
         edition = paris_roubaix.paris_roubaix_1990()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1991(self):
         edition = paris_roubaix.paris_roubaix_1991()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1992(self):
         edition = paris_roubaix.paris_roubaix_1992()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1993(self):
         edition = paris_roubaix.paris_roubaix_1993()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1994(self):
         edition = paris_roubaix.paris_roubaix_1994()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1995(self):
         edition = paris_roubaix.paris_roubaix_1995()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1996(self):
         edition = paris_roubaix.paris_roubaix_1996()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1997(self):
         edition = paris_roubaix.paris_roubaix_1997()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1998(self):
         edition = paris_roubaix.paris_roubaix_1998()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_1999(self):
         edition = paris_roubaix.paris_roubaix_1999()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2000(self):
         edition = paris_roubaix.paris_roubaix_2000()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2001(self):
         edition = paris_roubaix.paris_roubaix_2001()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2002(self):
         edition = paris_roubaix.paris_roubaix_2002()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2003(self):
         edition = paris_roubaix.paris_roubaix_2003()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2004(self):
         edition = paris_roubaix.paris_roubaix_2004()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2005(self):
         edition = paris_roubaix.paris_roubaix_2005()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2006(self):
         edition = paris_roubaix.paris_roubaix_2006()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2007(self):
         edition = paris_roubaix.paris_roubaix_2007()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2008(self):
         edition = paris_roubaix.paris_roubaix_2008()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2009(self):
         edition = paris_roubaix.paris_roubaix_2009()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2010(self):
         edition = paris_roubaix.paris_roubaix_2010()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2011(self):
         edition = paris_roubaix.paris_roubaix_2011()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2012(self):
         edition = paris_roubaix.paris_roubaix_2012()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2013(self):
         edition = paris_roubaix.paris_roubaix_2013()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2014(self):
         edition = paris_roubaix.paris_roubaix_2014()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2015(self):
         edition = paris_roubaix.paris_roubaix_2015()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2016(self):
         edition = paris_roubaix.paris_roubaix_2016()
         assert edition.name == "Paris-Roubaix"
         assert edition.start.fqnc == "Compiegne (France)"
         assert edition.finish.fqnc == "Roubaix (France)"

    def test_paris_roubaix_2017(self):
        edition = paris_roubaix.paris_roubaix_2017()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Compiegne (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

        cobbles = """29,160.0 km,Troisvilles à Inchy,2.2 km,***
        28,153.5 km,Viesly à Quiévy,1.8 km,***
        27,151.0 km,Quiévy à Saint Python,3.7 km,****
        26,144.5 km,Viesly à Biastre,3.0 km,***
        25,141.0 km,Biastre à Solesmes,0.8 km,**
        24,132.5 km,Vertain à Saint-Martin-sur-Ecaillon,2.3 km,***
        23,122.5 km,Verchain-Maugré à Quérénaing,1.6 km,***
        22,119.5 km,Quérénaing à Maing,2.5 km,***
        21,116.5 km,Maing à Monchaux-sur-Ecaillon,1.6 km,***
        20,103.5 km,Haveluy à Wallers,2.5 km,****
        19,95.5 km,Trouée d'Arenberg,2.4 km,*****
        18,89.0 km,Wallers à Hélesmes,1.6 km,***
        17,82.5 km,Hornaing à Wandignies,3.7 km,****
        16,75.0 km,Warlaing à Brillion,2.4 km,***
        15,71.5 km,Tilloy à Sars-et-Rosières,2.4 km,****
        14,65.0 km,Beuvry-la-Forêt à Orchies,1.4 km,***
        13,60.0 km,Orchies,1.7 km,***
        12,54.0 km,Auchy-lez-Orchies à Bersée,2.7 km,****
        11,48.5 km,Mons-en-Pévèle,3.0 km,*****
        10,42.5 km,Mérignies à Avelin,0.7 km,**
        9,39.0 km,Pont-Thibault à Ennevelin,1.4 km,***
        8,33.0 km,Templeuve,0.5 km,**
        7,26.5 km,Cysoing à Bourghelles,1.3 km,***
        6,24.0 km,Bourghelles à Wannehain,1.1 km,***
        5,19.5 km,Camphin-en-Pévèle,1.8 km,****
        4,17.0 km,Carrefour de l'Arbre,2.1 km,*****
        3,14.5 km,Grusson,1.1 km,**
        2,8.0 km,Willems à Hem,1.4 km,***
        1,1.0 km,Roubaix,0.3 km,*"""

        assert edition.cobbles == inspect.cleandoc(cobbles)

    def test_paris_roubaix_2018(self):
        edition = paris_roubaix.paris_roubaix_2018()
        assert edition.name == "Paris-Roubaix"
        assert edition.start.fqnc == "Compiegne (France)"
        assert edition.finish.fqnc == "Roubaix (France)"

        cobbles = """29,163.5 km,Troisvilles,2.2 km,***
        28,157.0 km,Briastre,3.0 km,***
        27,148.0 km,Saint-Python,1.5 km,***
        26,145.5 km,Quiévy,3.7 km,****
        25,138.0 km,Saint-Vaast,1.5 km,***
        24,127.0 km,Verchain-Maugré,1.5 km,***
        23,122.5 km,Quérénaing,1.6 km,***
        22,119.5 km,Maing,2.5 km,***
        21,116.5 km,Monchaux-sur-Ecaillon,1.6 km,***
        20,103.5 km,Haveluy,2.5 km,****
        19,95.0 km,Trouée d'Arenberg,2.4 km,*****
        18,89.0 km,Hellesmes, dit Pont-Gibus,1.6 km,***
        17,82.5 km,Wandignies,3.7 km,****
        16,75.0 km,Brillon,2.4 km,***
        15,71.5 km,Sars-et-Rosières,2.4 km,****
        14,65.0 km,Beuvry-la-Forêt,1.4 km,***
        13,60.0 km,Orchies,1.7 km,***
        12,54.0 km,Bersée,2.7 km,****
        11,48.5 km,Mons-en-Pévèle,3.0 km,*****
        10,42.5 km,Mérignies à Avelin,0.7 km,**
        9,39.0 km,Pont-Thibaut,1.4 km,***
        8,33.5 km,Templeuve-L'Epinette,0.2 km,*
        8,33.0 km,Templeuve, Moulin de Vertain,0.5 km,**
        7,26.5 km,Cysoing à Bourghelles,1.3 km,***
        6,24.0 km,Bourghelles à Wannehain,1.1 km,***
        5,19.5 km,Camphin-en-Pévèle,1.8 km,*****
        4,17.0 km,Carrefour de l'Arbre,2.1 km,*****
        3,14.5 km,Grouson,1.1 km,**
        2,8.0 km,Hem,1.4 km,***
        1,1.0 km,Roubaix, espace Charles-Crupelandt,0.3 km,*"""

        assert edition.cobbles == inspect.cleandoc(cobbles)
