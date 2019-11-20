from classic_builder import LiegeBastogneLiegeBuilder

def liege_bastogne_liege_1964():
    builder = LiegeBastogneLiegeBuilder(1964, 9, 9, 120)
    return builder.build()

def liege_bastogne_liege_1965():
    builder = LiegeBastogneLiegeBuilder(1965, 6, 30, 120)
    return builder.build()

def liege_bastogne_liege_1966():
    builder = LiegeBastogneLiegeBuilder(1966, 5, 28, 168)
    return builder.build()

def liege_bastogne_liege_1967():
    builder = LiegeBastogneLiegeBuilder(1967, 5, 13, 160)
    return builder.build()

def liege_bastogne_liege_2018():
    builder = LiegeBastogneLiegeBuilder(2018, 4, 22, 258)

    builder.cote( km = 72,    name = "Cote de Bonnerue",             height = 493 )
    builder.cote( km = 109,   name = "Cote de Saint-Roch",           height = 456 )
    builder.cote( km = 152,   name = "Cote de Mont-le-Soie",         height = 558 )
    builder.cote( km = 168,   name = "Cote de Pont",                 height = 443 )
    builder.cote( km = 172,   name = "Cote de Bellevaux",            height = 421 )
    builder.cote( km = 180,   name = "Cote de la Ferme Libert",      height = 502 )
    builder.cote( km = 198,   name = "Cote du Rosier",               height = 565 )
    builder.cote( km = 211,   name = "Col du Maquisard",             height = 367 )
    builder.cote( km = 222.5, name = "Cote de la Redoute",           height = 314 )
    builder.cote( km = 239,   name = "Cote de la Roche-aux-Faucons", height = 225 )
    builder.cote( km = 252.5, name = "Cote de Saint-Nicolas",        height = 175 )

    return builder.build()
