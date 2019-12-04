from ..util import spanish_col
import spain

def alto_de_haza_llana():
    return spanish_col("Alto de Haza Llana", 1680)

def alto_hoya_de_la_mora():
    return spanish_col("Alto de la Hoya", 921)

def sierra_nevada():
    return spanish_col(spain.sierra_nevada().name, spain.sierra_nevada().elevation)
