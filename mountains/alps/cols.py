from ..util import french_col, italian_col, swiss_col
import france
import italy
import switzerland

def col_d_agnel():
    return french_col("Col d'Agnel", 2744)

def col_d_allos():
    return french_col("Col d'Allos", 2250)

def alpe_d_huez():
    return french_col(france.alpe_d_huez().name, france.alpe_d_huez().elevation, 13.8, 8.1)

def aprica():
    return italian_col(italy.aprica().name, italy.aprica().elevation)

def les_arcs():
    return french_col(france.les_arcs().name, france.les_arcs().elevation)

def col_des_aravis():
    return french_col("Col des Aravis",1498)

def avoriaz():
    return french_col(france.avoriaz().name, france.avoriaz().elevation)

# B
def col_bayard():
    return french_col("Col Bayard", 1264)

def le_bettex():
    return french_col("Le Bettex, Saint-Gervais - Mont-Blanc", 1372)

def montee_du_bisanne():
    return french_col("Montee de Bisanne", 1723, 12.4, 8.2)

def col_de_bluffy():
    return french_col("Col de Bluffy", 622, 1.5, 5.6)

def cote_de_brie():
    return french_col("Cote de Brie", 450, 2.4, 6.9)

def bardonecchia_monte_jafferau():
    return italian_col("Bardonecchia (Monte Jafferau)",  1980)

def bormio():
    return italian_col(italy.bormio().name, italy.bormio().elevation)

# C
def ceresole_reale(municipality = None):
    return italian_col(italy.ceresole_reale().name,  municipality, italy.ceresole_reale().elevation)

def cervinia():
    return italian_col(italy.cervinia().name, italy.cervinia().elevation)

def cevo():
    return italian_col(italy.cevo().name, italy.cevo().elevation)

def col_de_la_cabre():
    return french_col("Col de la Cabre",1180)

def col_de_la_cayolle():
    return french_col("Col de la Cayolle",2326)

def col_de_la_chau():
    return french_col("Col de la Chau",1430)

def col_du_chaussy():
    return french_col("Col du Chaussy",1533)

def chamrousse():
    return french_col(france.chamrousse().name, france.chamrousse().elevation)

def col_des_champs():
    return french_col("Col des Champs",2095)

def col_del_la_colle_saint_michel():
    return french_col("Col de la Colle-Saint-Michel",1431)

def col_de_la_colombiere():
    return french_col("Col de la Colombiere",1618, 7.5, 8.5)

def col_du_coq():
    return french_col("Col du Coq",1430)

def col_du_corbier():
    return french_col("Col du Corbier",1325)

def col_de_cordon():
    return french_col("Col de Cordon",975)

def colma_di_sormano():
    return italian_col("Colman di Sormano",1124)

def cormet_de_roselend():
    return french_col("Cormet de Roselend", 1968, 5.7, 6.5)

def cortina_d_ampezzo():
    return italian_col(italy.cortina_d_ampezzo().name, italy.cortina_d_ampezzo().elevation)

def courchevel():
    return french_col(france.courchevel().name, france.courchevel().elevation)

def crans_montana():
    return swiss_col(switzerland.crans_montana().name, switzerland.crans_montana().elevation)

def col_de_la_croix():
    return swiss_col("Col de la Croix",1778)

def colle_del_morte():
    return french_col("Colle del Morte",710)

def colle_san_carlo():
    return italian_col("Colle San Carlo",1951)

def croix_de_fer():
    return french_col("Croix de Fer", 2067, 29, 5.2)

def col_de_la_croix_fry():
    return french_col("Col de la Croix Fry", 1477, 11.3, 7)

def cucheron():
    return french_col("Cucheron",1139)

# E
def col_del_epine():
    return french_col("Col de l’Épine",947)

# F
def finhaut_emosson():
    return swiss_col("Finhaut-Emosson",1960)

def forclaz():
    return swiss_col("Forclaz",1527)

def forclaz_de_montmin():
    return french_col("Forclaz-de-Montmin",1150)

# G
def col_du_galibier():
    return french_col("Col du Galibier",2642)

def col_du_galibier_serre_chevalier():
    return french_col("Col du Galibier - Serre Chevalier", 2642)

def col_du_glandon():
    return french_col("Col du Glandon",1924)

def grand_cucheron():
    return french_col("Grand Cucheron",1188)

def grand_saint_bernard():
    return french_col("Grand-Saint-Bernard",2470)

def col_du_granier():
    return french_col("Col du Granier",1134)

def col_du_granon():
    return french_col("Col du Granon",2413)

# H
def montee_d_hauteville():
    return french_col("Montée d’Hauteville",1639)

# I
def col_de_l_iseran():
    return french_col("Col de l'Iseran",2770)

def col_d_izoard():
    return french_col("Col d'Izoard",2360)

# J
def monte_jafferau():
    return italian_col("Monte Jafferau",1980)

# L
def lacets_de_montvernier():
    return french_col("Lacets de Montvernier", 782, 3.4, 8.2)

def cote_de_laffrey():
    return french_col("Côte de Laffrey",900)

def col_de_la_lombarde():
    return french_col("Col de la Lombarde",2351)

def la_toussuire():
    return french_col(france.la_toussuire().name, france.la_toussuire().elevation)

def la_toussuire_les_sybelles():
    return french_col("La Toussuire - Les Sybelles",1705)

def lans_en_vercors():
    return french_col(france.lans_en_vercors().name, france.lans_en_vercors().elevation)

def col_du_lautaret():
    return french_col("Col du Lautaret",2058)

def les_deux_alpes():
    return french_col(france.les_deux_alpes().name, france.les_deux_alpes().elevation)

def les_menuires():
    return french_col(france.les_menuires().name, france.les_menuires().elevation)

def les_orres():
    return french_col("Les Orres", 1496)

def col_du_luitel():
    return french_col("Luitel",1262)

def colle_del_lys():
    return italian_col("Colle del Lys",1311)

def col_de_la_joux_plane():
    return french_col("Col de la Joux Plane",1700)

def col_de_joux_verte():
    return french_col("Col de Joux-Verte",1760)

# M
def col_de_la_madeleine():
    return french_col("Col de la Madeleine", 2000, 25.3, 6.2)

def madonna_del_ghisallo():
    return italian_col("Madonna del Ghisallo",754)

def col_de_manse():
    return french_col("Col de Manse",1268)

def meribel_les_allues():
    return french_col("Méribel-les-Allues",1750)

def col_du_mollard():
    return french_col("Col du Mollard",1638)

def col_de_la_morte():
    return french_col("Col de la Morte",1368)

def mont_cenis():
    return french_col("Mont-Cenis",2083)

def montgenevre():
    return french_col("Montgenèvre",1860)

def montoso():
    return italian_col("Montoso",1248)

def col_des_mosses():
    return swiss_col("Col des Mosses",1448)

def col_du_noyer():
    return french_col("Col du Noyer",1664)

# O
def orcieres_merlette():
    return french_col(france.orcieres_merlette().name, france.orcieres_merlette().elevation)

def col_de_palaquit():
    return french_col("Col de Palaquit",1154)

def montee_du_plateau_des_glieres():
    return french_col("Montee du plateau des Glieres", 1390, 6, 11.2)

def col_du_pre():
    return french_col("Col du Pre", 1748, 12.6, 7.7)

def pas_de_morgins():
    return french_col("Pas-de-Morgins",1369)

def passo_del_mortirolo():
    return italian_col("Passo del Mortirolo",1854)

def col_de_parmenie():
    return french_col("Col de Parménie",571)

def col_de_perty():
    return french_col("Col de Perty",1303)

def col_de_petit_saint_bernard():
    return french_col("Col de Petit-Saint-Bernard",2188)

def la_plagne():
    return french_col("La Plagne",1970)

def col_de_plainpalais():
    return french_col("Col de Plainpalais",1173)

def le_pleynet():
    return french_col("Le Pleynet",1445)

def col_de_porte():
    return french_col("Col de Porte",1326)

def pian_del_lupo():
    return italian_col("Pian del Lupo",1405)

def pra_loup():
    return french_col(france.pra_loup().name, france.pra_loup().elevation)

def prato_nevoso():
    return italian_col("Prato Nevoso", 1607)

def prapoutel_les_sept_laux():
    return french_col("Prapoutel-les-Sept-Laux",1358)

def col_des_pres():
    return french_col("Col des Prés",1135)

def plan_de_corones():
    return italian_col(italy.plan_de_corones().name, italy.plan_de_corones().elevation)

# R
def ramaz():
    return french_col("Ramaz",1619)

def restefond():
    return french_col("Restefond, Col de la Bonette",2802)

def mont_revard():
    return french_col("Mont Revard",1537)

def risoul():
    return french_col("Risoul",1855)

def col_de_romeyere():
    return french_col("Col de Romeyere",1074)

def col_de_romme():
    return french_col("Col de Romme", 1297, 8.8, 8.9)

def col_du_rousset():
    return french_col("Col du Rousset",1254)

def la_rosiere():
    return french_col("La Rosiere", 1855, 17.6, 5.8)

def la_ruchere():
    return french_col("La Ruchère",1160)

# S
def cote_de_sainte_eulalie():
    return french_col("Cote de Sainte-Eulalie", 298, 1.5, 4.9)

def saint_gervais_mont_blanc():
    return french_col("Saint-Gervais Mont-Blanc", 970)

def saint_moritz():
    return swiss_col(switzerland.saint_moritz().name, switzerland.saint_moritz().elevation)

def saint_nizier():
    return french_col("Saint-Nizier",1180)

def col_des_saisies():
    return french_col("Col des Saisies",1633)

def mont_saleve():
    return french_col("Mont Salève",1307)

def col_de_sarenne():
    return french_col("Col de Sarenne",1999)

def col_du_semnoz():
    return french_col("Col du Semnoz",1655)

def col_de_la_sentinelle():
    return french_col("Col de la Sentinelle",980)

def passo_dello_stelvio():
    return italian_col("Passo dello Stelvio",2757)

def serre_chevalier():
    return french_col(france.serre_chevalier().name, france.serre_chevalier().elevation)

def sestriere():
    return italian_col(italy.sestriere().name, italy.sestriere().elevation)

def col_de_tamie():
    return french_col("Col de Tamié",907)

def col_du_telegraphe():
    return french_col("Col du Télégraphe",1566)

def col_de_tende():
    return french_col("Col de Tende",1320)

def montee_de_tignes():
    return french_col("Montée de Tignes",2068)

def col_de_tournoi():
    return french_col("Col de Tourniol",1145)

def truc_d_arbe():
    return italian_col("Truc d'Arbe",1256)

# V
def val_d_isere():
    return french_col(france.val_d_isere().name, france.val_d_isere().elevation)

def valmorel():
    return french_col("Valmorel", 1369)

def val_thorens():
    return french_col(france.val_thorens().name, france.val_thorens().elevation)

def col_de_vars():
    return french_col("Col de Vars",2109)

def verbier():
    return swiss_col(switzerland.verbier().name, switzerland.verbier().elevation)

def verrayes():
    return italian_col("Verrayes",1017)

def verrogne():
    return italian_col("Verrogne",1582)

def villard_de_lans():
    return french_col(france.villard_de_lans().name, france.villard_de_lans().elevation)

