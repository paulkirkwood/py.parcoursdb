import inspect
import tour_of_flanders

class TestTourOfFlanders:

    def test_tour_of_flanders_1913(self):
        edition = tour_of_flanders.tour_of_flanders_1913()
        assert edition.name == "Tour of Flanders"
        assert edition.start.fqnc == "Ghent (Belgium)"
        assert edition.finish.fqnc == "Mariakerke (Belgium)"

    def test_tour_of_flanders_1914(self):
        edition = tour_of_flanders.tour_of_flanders_1914()
        assert edition.name == "Tour of Flanders"
        assert edition.start.fqnc == "Ghent (Belgium)"
        assert edition.finish.fqnc == "Evergem (Belgium)"

    def test_tour_of_flanders_1919(self):
        edition = tour_of_flanders.tour_of_flanders_1919()
        assert edition.name == "Tour of Flanders"
        assert edition.start.fqnc == "Ghent (Belgium)"
        assert edition.finish.fqnc == "Gentbrugge (Belgium)"

    def test_tour_of_flanders_2018(self):
        edition = tour_of_flanders.tour_of_flanders_2018()
        assert edition.name == "Tour of Flanders"
        assert edition.start.fqnc == "Antwerp (Belgium)"
        assert edition.finish.fqnc == "Oudenaarde (Belgium)"

        cobbles = """1,180.0 km,Lippenhovestraat,1.3 km
        2,178.0 km,Paddestraat,2.3 km
        3,125.0 km,Holleweg,0.35 km
        4,119.0 km,Haaghoek,2.0 km
        5,42.0 km,Mariaborrestraat,2.0 km"""

        assert edition.cobbles == inspect.cleandoc(cobbles)

        bergs = """1,146.0 km,Oude-Kwaremont,2.2 km,Cobbles
        2,135.0 km,Kortkeer,1.0 km,Asphalt
        3,130.0 km,Edelare,1.0 km,Asphalt
        4,125.0 km,Wolvenberg,1.5 km,Cobbles
        5,116.0 km,Leberg,0.95 km,Asphalt
        6,112.0 km,Berendries,0.94 km,Asphalt
        7,107.0 km,Tenbosse,0.45 km,Asphalt
        8,97.0 km,Muur-Kapelmuur,0.75 km,Asphalt
        9,78.0 km,Pottelberg,1.5 km,Asphalt
        10,72.0 km,Kanarieberg,1.0 km,Asphalt
        11,56.0 km,Oude-Kwaremont,2.2 km,Cobbles
        12,53.0 km,Paterberg,0.36 km,Cobbles
        13,46.0 km,Koppenberg,0.6 km,Cobbles
        14,41.0 km,Steenbeekdries,0.6 km,Asphalt
        15,38.0 km,Taaienberg,0.5 km,Cobbles
        16,27.0 km,Kruisberg (Oudestraat),0.45 km,Cobbles
        17,17.0 km,Oude-Kwaremont,2.2 km,Cobbles
        18,14.0 km,Paterberg,0.36 km,Cobbles"""

        assert edition.climbs == inspect.cleandoc(bergs)
