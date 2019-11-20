from country import Spain
from location import Location

def albacete():
    return _spanish_location("Albacete")

def alto_del_naranco():
    return _spanish_location("Alto del Naranco")

def badajoz():
    return _spanish_location("Badajoz")

def barcelona():
    return _spanish_location("Barcelona")

def benasque():
    return _spanish_location("Benasque")

def bossost():
    return _spanish_location("Bossost")

def caceres():
    return _spanish_location("Cáceres")

def cala_d_or():
    return _spanish_location("Cala d'Or")

def cangas_de_onis():
    return _spanish_location("Cangas de Onís")

def collado_villalba():
    return _spanish_location("Collado Villalba")

def ezcaray():
    return _spanish_location("Ezcaray")

def girona():
    return _spanish_location("Girona")

def jaca():
    return _spanish_location("Jaca")

def jaen():
    return _spanish_location("Jaén")

def la_seu_d_urgell():
    return _spanish_location("La Seu d'Urgell")

def leon():
    return _spanish_location("León")

def linares():
    return _spanish_location("Linares")

def lloret_de_mar():
    return _spanish_location("Lloret de Mar")

def madrid():
    return _spanish_location("Madrid")

def merida():
    return _spanish_location("Mérida")

def montigo():
    return _spanish_location("Montigo")

def montjuic_circuit():
    return _spanish_location("Montjuic circuit")

def palazuelos_de_eresma_destilerias_dyc():
    return _spanish_location("Palazuelos de Eresma (Destilerias DYC)")

def palma_de_mallorca():
    return _spanish_location("Palma de Mallorca")

def pla_de_beret():
    return _spanish_location("Pla de Beret")

def pamplona():
    return _spanish_location("Pamplona")

def san_sebastian():
    return _spanish_location("San Sebastián")

def sant_cugat_del_valles():
    return _spanish_location("Sant Cugat del Vallès")

def santo_domingo_de_la_calzada():
    return _spanish_location("Santo Domingo de la Calzada")

def santander():
    return _spanish_location("Santander")

def seville():
    return _spanish_location("Seville")

def valdezcaray():
    return _spanish_location("Valdezcaray")

def valencia():
    return _spanish_location("Valencia")

def valladolid():
    return _spanish_location("Valladolid")

def vielha_val_d_aran():
    return _spanish_location("Vielha Val d'Aran")

def vitoria_gasteiz():
    return _spanish_location("Vitoria-Gasteiz")

def zaragoza():
    return _spanish_location("Zaragoza")

def _spanish_location(name):
    return Location(name, Spain())
