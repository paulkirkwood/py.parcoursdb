from ..util import spanish_col

def alto_de_la_cruz_de_la_demanda(municipality = None):
    if municipality is None:
        return spanish_col("Alto de la Cruz de la Demanda", 1842)
    else:
        return spanish_col("Alto de la Cruz de la Demanda ({})".format(municipality), 1842)
        
