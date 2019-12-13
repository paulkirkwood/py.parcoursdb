from ..util import italian_col
import italy

def abetone():
    return italian_col(italy.abetone().name, italy.abetone().elevation)

def blockhaus():
    return italian_col("Blockhaus", 1210)

def montevergine_di_mercogliano():
    return italian_col("Montevergine di Mercogliano", 1260)

def monte_carpegna():
    return italian_col("Monte Carpegna", 1369)

def monte_petrano():
    return italian_col("Monte Petrano", 1105)

def monte_terminillo():
    return italian_col("Monte Terminillo", 2217)

def monte_trebbio():
    return italian_col("Monte Trebbio", 575)

def mount_vesuvius():
    return italian_col(italy.mount_vesuvius().name, italy.mount_vesuvius().elevation)
