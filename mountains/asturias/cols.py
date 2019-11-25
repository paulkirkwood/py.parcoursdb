from ..util import spanish_col

def alto_de_cotobello():
    return spanish_col("Alto de Cotobello", 1196)

def alto_de_la_cobertoria():
    return spanish_col("Alto de la Cobertoria", 1173)

def alto_de_l_angliru():
    return spanish_col("Alto de l'Angliru", 1573, 12.5, 10.13, 23.6)

def alto_del_morredero(municipality = None):
    if municipality is None:
        return spanish_col("Alto del Morredero", 1735)
    return spanish_col("Alto del Morredero ({})".format(municipality), 1735)

def alto_del_naranco():
    return spanish_col("Alto del Naranco", 634)

def lagos_de_covadonga():
    return spanish_col("Lagos de Covadonga", 1094)
