import inspect
import pytest
import paris_nice

class TestParisNice:

    def test_paris_nice2018(self):
        route = """1,4 March,Chatou to Meudon,134.5 km,Road stage
        2,5 March,Orsonville to Vierzon,187.5 km,Road stage
        3,6 March,Bourges to Chatel-Guyon,210.0 km,Road stage
        4,7 March,La Fouillouse to Saint-Étienne,18.4 km,Individual time trial
        5,8 March,Salon-de-Provence to Sisteron,165.0 km,Road stage
        6,9 March,Sisteron to Vence,198.0 km,Road stage
        7,10 March,Nice to Valdeblore La Colmiane,175.0 km,Road stage
        8,11 March,Nice,110.0 km,Road stage"""

        edition = paris_nice.paris_nice2018()
        assert edition.route == inspect.cleandoc(route)
        assert edition.summit_finishes == 1
        assert edition.stage_summary == "8 stages"
