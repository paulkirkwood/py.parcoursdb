import inspect
import pytest
import dauphine

class TestDauphine:

    def test_dauphine2009(self):
        route = """1,7 June,Nancy,12.1 km,Individual time trial
        2,8 June,Nancy to Dijon,228.0 km,Road stage
        3,9 June,Tournus to Saint-Étienne,182.0 km,Road stage
        4,10 June,Bourg-lès-Valence to Valence,42.4 km,Individual time trial
        5,11 June,Valence to Mont Ventoux,154.0 km,Road stage
        6,12 June,Gap to Briançon,106.0 km,Road stage
        7,13 June,Briançon to Saint-François-Longchamp,157.0 km,Road stage
        8,14 June,Faverges to Grenoble,146.0 km,Road stage"""

        edition = dauphine.dauphine2009()
        assert edition.route == inspect.cleandoc(route)
        assert edition.summit_finishes == 1
        assert edition.stage_summary == "8 stages"

    def test_dauphine2018(self):
        route = """P,3 June,Valence,6.6 km,Individual time trial
        1,4 June,Valence to Saint-Just-Saint-Rambert,179.0 km,Road stage
        2,5 June,Montbrison to Belleville,181.0 km,Road stage
        3,6 June,Pont-de-Vaux to Louhans-Chateaurenaud,35.0 km,Team time trial
        4,7 June,Chazey-sur-Ain to Lans-en-Vercors,181.0 km,Road stage
        5,8 June,Grenoble to Valmorel,130.0 km,Road stage
        6,9 June,Frontenex to La Rosiere,110.0 km,Road stage
        7,10 June,Moûtiers to Saint-Gervais Mont-Blanc,136.0 km,Road stage"""

        edition = dauphine.dauphine2018()
        assert edition.route == inspect.cleandoc(route)
        assert edition.summit_finishes == 4
        assert edition.stage_summary == "7 stages + Prologue"
