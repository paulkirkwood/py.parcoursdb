import la_fleche_wallonne

class TestLaFlecheWallonne:

    def test_la_fleche_wallonne_1974(self):
        edition = la_fleche_wallonne.la_fleche_wallonne_1974()
        assert edition.name == "La Flèche Wallonne"
        assert edition.start.fqnc == "Verviers (Belgium)"
        assert edition.finish.fqnc == "Verviers (Belgium)"

    def test_la_fleche_wallonne_1975(self):
        edition = la_fleche_wallonne.la_fleche_wallonne_1975()
        assert edition.name == "La Flèche Wallonne"
        assert edition.start.fqnc == "Verviers (Belgium)"
        assert edition.finish.fqnc == "Verviers (Belgium)"
