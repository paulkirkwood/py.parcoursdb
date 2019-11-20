import inspect
import pytest
import vuelta

class TestTourOfSpain:

    def test_tdf1991(self):
        route = """1,29 April,Mérida,8.8 km,Three man team time trial
        2a,30 April,Mérida to Cáceres,134.5 km,Road stage
        2b,30 April,Montigo to Badajoz,40.4 km,Team time trial
        3,1 May,Badajoz to Seville,233.2 km,Road stage
        4,2 May,Seville to Jaén,292.0 km,Road stage
        5,3 May,Linares to Albacete,227.8 km,Road stage
        6,4 May,Albacete to Valencia,236.5 km,Road stage
        7,5 May,Palma de Mallorca,188.0 km,Road stage
        8,6 May,Cala d'Or,47.0 km,Individual time trial
        9,7 May,Sant Cugat del Vallès to Lloret de Mar,140.0 km,Road stage
        10,8 May,Lloret de Mar to Andorra la Vella (Andorra),229.0 km,Road stage
        11,9 May,Andorra la Vella (Andorra) to Pla de Beret,0.0 km,Road stage
        12,10 May,Bossost to Cerler,111.0 km,Road stage
        13,11 May,Benasque to Zaragoza,219.0 km,Road stage
        14,12 May,Ezcaray to Valdezcaray,24.1 km,Individual time trial
        15,13 May,Santo Domingo de la Calzada to Santander,219.5 km,Road stage
        16,14 May,Santander to Lagos de Covadonga,186.6 km,Road stage
        17,15 May,Cangas de Onís to Alto del Naranco,152.0 km,Road stage
        18,16 May,León to Valladolid,137.5 km,Road stage
        19,17 May,Valladolid,53.2 km,Individual time trial
        20,18 May,Palazuelos de Eresma (Destilerias DYC),212.7 km,Road stage
        21,19 May,Collado Villalba to Madrid,169.6 km,Road stage"""

        edition = vuelta.vuelta1991()
        assert edition.route == inspect.cleandoc(route)
