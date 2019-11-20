from pave import Pave, PaveRating

class TestPave:

    def test_pave(self):
        mons_en_pevele = Pave( "Mons-en-Pévèle", 3, PaveRating.FiveStar)
        assert str(mons_en_pevele.rating) == '*****'
