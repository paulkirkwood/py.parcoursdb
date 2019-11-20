from berg import Berg, Pavement
from classic_builder import TourOfFlandersBuilder

def tour_of_flanders_1913():
    builder = TourOfFlandersBuilder(1913, 4, 2, 265)
    return builder.build()

def tour_of_flanders_1914():
    builder = TourOfFlandersBuilder(1914, 4, 2, 265)
    return builder.build()

def tour_of_flanders_1919():
    builder = TourOfFlandersBuilder(1919, 4, 2, 265)
    return builder.build()

def tour_of_flanders_2018():
    builder = TourOfFlandersBuilder(2018, 4, 1, 267)

    builder.pave( name = "Lippenhovestraat", length = 1.3,  km = 87 )
    builder.pave( name = "Paddestraat",      length = 2.3,  km = 89 )
    builder.pave( name = "Holleweg",         length = 0.35, km = 142 )
    builder.pave( name = "Haaghoek",         length = 2.0,  km = 148 )
    builder.pave( name = "Mariaborrestraat", length = 2.0,  km = 225 )

    #
    # Three ascents of Oude-Kwaremont
    #
    oude_kwaremont = Berg( "Oude-Kwaremont", 2.2, Pavement.Cobbles )
    builder.berg( oude_kwaremont, 121 )
    builder.berg( oude_kwaremont, 211 )
    builder.berg( oude_kwaremont, 250 )

    #
    # Two ascents of the Paterberg
    #
    paterberg = Berg( "Paterberg", 0.36, Pavement.Cobbles )
    builder.berg( paterberg, 214 )
    builder.berg( paterberg, 253 )

    #
    # One ascent of everything else
    #
    builder.asphalt_berg( name = "Kortkeer",               length = 1.0,  km = 132 )
    builder.asphalt_berg( name = "Edelare",                length = 1.0,  km = 137 )
    builder.cobbled_berg( name = "Wolvenberg",             length = 1.5,  km = 142 )
    builder.asphalt_berg( name = "Leberg",                 length = 0.95, km = 151 )
    builder.asphalt_berg( name = "Berendries",             length = 0.94, km = 155 )
    builder.asphalt_berg( name = "Tenbosse",               length = 0.45, km = 160 )
    builder.asphalt_berg( name = "Muur-Kapelmuur",         length = 0.75, km = 170 )
    builder.asphalt_berg( name = "Pottelberg",             length = 1.5,  km = 189 )
    builder.asphalt_berg( name = "Kanarieberg",            length = 1.0,  km = 195 )
    builder.cobbled_berg( name = "Koppenberg",             length = 0.6,  km = 221 )
    builder.asphalt_berg( name = "Steenbeekdries",         length = 0.6,  km = 226 )
    builder.cobbled_berg( name = "Taaienberg",             length = 0.5,  km = 229 )
    builder.cobbled_berg( name = "Kruisberg (Oudestraat)", length = 0.45, km = 240 )

    return builder.build()
