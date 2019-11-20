from col import ColCategory

class TestCol:

    def test_col_category(self):
        assert str(ColCategory.HC) == "HC"
        assert str(ColCategory.C1) == "C.1"
        assert str(ColCategory.UC) == "Uncategorised"
