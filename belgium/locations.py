from country import Belgium
from location import Location

# A
def ans():
    return _belgian_location("Ans")

def antwerp():
    return _belgian_location("Antwerp")

def arlon():
    return _belgian_location("Arlon")

# B
def bastogne():
    return _belgian_location("Bastogne")

def beauraing():
    return _belgian_location("Beauraing")

def beringen():
    return _belgian_location("Beringen")

def beveren():
    return _belgian_location("Beveren")

def bornem():
    return _belgian_location("Bornem")

def brasschaat():
    return _belgian_location("Brasschaat")

def bruges():
    return _belgian_location("Bruges")

def brussels():
    return _belgian_location("Brussels")

# C
def charleroi():
    return _belgian_location("Charleroi")

def circuit_zolder():
    return _belgian_location("Circuit Zolder")

# D
def deinze():
    return _belgian_location("Deinze")

def dinant():
    return _belgian_location("Dinant")

# E
def esneux():
    return _belgian_location("Esneux")

def evergem():
    return _belgian_location("Evergem")

# F
def forest():
    return _belgian_location( "Forest" )

# G
def gentbrugge():
    return _belgian_location("Gentbrugge")

def ghent():
    return _belgian_location("Ghent")

# H
def harelbeke():
    return _belgian_location("Harelbeke")

def hasselt():
    return _belgian_location("Hasselt")

def herentals():
    return _belgian_location("Herentals")

def hotton():
    return _belgian_location("Hotton")

def huy():
    return _belgian_location("Huy")

# J
def jambes():
    return _belgian_location("Jambes")

# L
def leuven():
    return _belgian_location("Leuven")

def liege():
    return _belgian_location("Liège")

# M
def marche_en_famenne():
    return _belgian_location("Marche-en-Famenne")

def mariakerke():
    return _belgian_location("Mariakerke")

def marcinelle():
    return _belgian_location("Marcinelle")

def meerbeke():
    return _belgian_location("Merebeke")

def molenbeek():
    return _belgian_location("Molenbeek")

def mons():
    return _belgian_location("Mons")

def mouscron():
    return _belgian_location("Mouscron")
 
# N
def namur():
    return _belgian_location("Namur")

# O
def oudenaarde():
    return _belgian_location("Oudenaarde")

# P
def perwez():
    return _belgian_location("Perwez")

# R
def rochefort():
    return _belgian_location("Rochefort")

def rocourt():
    return _belgian_location("Rocourt")

# S
def seraing():
    return _belgian_location("Seraing")

def sint_niklaas():
    return _belgian_location("Sint-Niklaas")

def sint_pieters_woluwe():
    return _belgian_location("Sint-Pieters-Woluwe")

def spa():
    return _belgian_location("Spa")

# T
def tournai():
    return _belgian_location("Tournai")

# V
def verviers():
    return _belgian_location("Verviers")

def vise():
    return _belgian_location("Vise")

# W
def wanze():
    return _belgian_location("Wanze")

def waregem():
    return _belgian_location("Waregem")

def waterloo():
    return _belgian_location("Waterloo")

def wetteren():
    return _belgian_location("Wetteren")

def wevelgem():
    return _belgian_location("Wevelgem")

# Y
def ypres():
    return _belgian_location("Ypres")

def _belgian_location(name):
    return Location(name, Belgium())
