from ..util import spanish_col

def mirador_de_ezaro(municipality = None):
    if municipality is None:
        return spanish_col("Mirador de Ézaro", 274)
    else:
        return spanish_col("Mirador de Ézaro ({})".format(municipality), 274)
