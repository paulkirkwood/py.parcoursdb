import austria 
import belgium
import croatia
import denmark
import fiume
import france
import germany
import greece
import ireland
import israel
import italy
import luxembourg
import netherlands
import monaco
import northern_ireland
import san_marino
import slovenia
import switzerland
import vatican_city
import west_germany
import yugoslavia
import mountains.alps
import mountains.dolomites
import mountains.appennines
import mountains.sciliy
from col                import ColCategory
from stage_race         import TourOfItaly
from stage_race_builder import NonConsecutiveStageRaceBuilder, TourOfItalyBuilder

def giro1909():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1909)
    builder.road_stage(5, 13, italy.milan(), italy.bologna(), 397.0)
    builder.road_stage(5, 16, italy.bologna(), italy.chieti(), 375.8)
    builder.road_stage(5, 18, italy.chieti(), italy.naples(), 242.8)
    builder.road_stage(5, 20, italy.naples(), italy.rome(), 228.1)
    builder.road_stage(5, 23, italy.rome(), italy.florence(), 346.5)
    builder.road_stage(5, 25, italy.florence(), italy.genoa(), 294.1)
    builder.road_stage(5, 27, italy.genoa(), italy.turin(), 354.9)
    builder.road_stage(5, 30, italy.turin(), italy.milan(), 206.0)
    return builder.build()

def giro1910():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1910)
    builder.road_stage(5, 18, italy.milan(), italy.udine(), 388.0)
    builder.road_stage(5, 20, italy.udine(), italy.bologna(), 322.4)
    builder.road_stage(5, 22, italy.bologna(), italy.teramo(), 345.2)
    builder.road_stage(5, 24, italy.teramo(), italy.naples(), 319.5)
    builder.road_stage(5, 26, italy.naples(), italy.rome(), 192.3)
    builder.road_stage(5, 28, italy.rome(), italy.florence(), 327.5)
    builder.road_stage(5, 30, italy.florence(), italy.genoa(), 263.5)
    builder.road_stage(6, 1, italy.genoa(), italy.mondovi(), 218.1)
    builder.road_stage(6, 2, italy.mondovi(), italy.turin(), 333.4)
    builder.road_stage(6, 5, italy.turin(), italy.milan(), 277.5)
    return builder.build()

def giro1911():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1911)
    builder.road_stage(5, 15, italy.rome(), italy.florence(), 394.1)
    builder.road_stage(5, 17, italy.florence(), italy.genoa(), 261.5)
    builder.road_stage(5, 19, italy.genoa(), italy.oneglia(), 274.9)
    builder.road_stage(5, 21, italy.oneglia(), italy.mondovi(), 190.3)
    builder.road_stage(5, 23, italy.mondovi(), italy.turin(), 302.0)
    builder.road_stage(5, 25, italy.turin(), italy.milan(), 236.2)
    builder.road_stage(5, 27, italy.milan(), italy.bologna(), 394.0)
    builder.road_stage(5, 29, italy.bologna(), italy.ancona(), 283.4)
    builder.road_stage(5, 31, italy.ancona(), italy.sulmona(), 218.7)
    builder.road_stage(6, 2, italy.sulmona(), italy.bari(), 363.1)
    builder.road_stage(6, 4, italy.bari(), italy.pompeii(), 345.2)
    builder.road_stage(6, 6, italy.naples(), italy.rome(), 266.9)
    return builder.build()

def giro1912():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1912)
    builder.road_stage(5, 19, italy.milan(), italy.padua(), 398.8)
    builder.road_stage(5, 21, italy.padua(), italy.bologna(), 328.8)
    builder.road_stage(5, 23, italy.bologna(), italy.pescara(), 362.5)
    builder.road_stage(5, 25, italy.pescara(), italy.rome(), 294.0)
    builder.road_stage(5, 27, italy.rome(), italy.florence(), 337.0)
    builder.road_stage(5, 29, italy.florence(), italy.genoa(), 267.5)
    builder.road_stage(5, 31, italy.genoa(), italy.turin(), 230.0)
    builder.road_stage(6, 2, italy.turin(), italy.milan(), 280.0)
    builder.road_stage(6, 4, italy.milan(), italy.bergamo(), 235.0)
    return builder.build()

def giro1913():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1913)
    builder.road_stage(5, 6, italy.milan(), italy.genoa(), 341.0)
    builder.road_stage(5, 8, italy.genoa(), italy.siena(), 332.0)
    builder.road_stage(5, 10, italy.siena(), italy.rome(), 317.9)
    builder.road_stage(5, 12, italy.rome(), italy.salerno(), 341.0)
    builder.road_stage(5, 14, italy.salerno(), italy.bari(), 295.6)
    builder.road_stage(5, 16, italy.bari(), italy.campobasso(), 256.0)
    builder.road_stage(5, 18, italy.campobasso(), italy.ascoli_piceno(), 313.2)
    builder.road_stage(5, 20, italy.ascoli_piceno(), italy.rovigo(), 413.8)
    builder.road_stage(5, 22, italy.rovigo(), italy.milan(), 321.5)
    return builder.build()

def giro1914():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1914)
    builder.road_stage(5, 24, italy.milan(), italy.cuneo(), 420.0)
    builder.road_stage(5, 26, italy.cuneo(), italy.lucca(), 340.5)
    builder.road_stage(5, 28, italy.lucca(), italy.rome(), 430.0)
    builder.road_stage(5, 30, italy.rome(), italy.avellino(), 365.4)
    builder.road_stage(6, 1, italy.avellino(), italy.bari(), 328.7)
    builder.road_stage(6, 3, italy.bari(), italy.l_aquila(), 428.0)
    builder.road_stage(6, 5, italy.l_aquila(), italy.lugo(), 429.1)
    builder.road_stage(6, 7, italy.lugo(), italy.milan(), 420.3)
    return builder.build()

def giro1919():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1919)
    builder.road_stage(5, 21, italy.milan(), italy.trento(), 302.8)
    builder.road_stage(5, 23, italy.trento(), italy.trieste(), 334.3)
    builder.road_stage(5, 25, italy.trieste(), italy.ferrara(), 282.0)
    builder.road_stage(5, 27, italy.ferrara(), italy.pescara(), 411.2)
    builder.road_stage(5, 29, italy.pescara(), italy.naples(), 312.5)
    builder.road_stage(5, 31, italy.naples(), italy.rome(), 203.8)
    builder.road_stage(6, 2, italy.rome(), italy.florence(), 350.8)
    builder.road_stage(6, 4, italy.florence(), italy.genoa(), 261.8)
    builder.road_stage(6, 6, italy.genoa(), italy.turin(), 248.0)
    builder.road_stage(6, 8, italy.turin(), italy.milan(), 277.0)
    return builder.build()

def giro1920():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1920)
    builder.road_stage(5, 23, italy.milan(), italy.turin(), 348.0)
    builder.road_stage(5, 25, italy.turin(), italy.lucca(), 378.0)
    builder.road_stage(5, 27, italy.lucca(), italy.rome(), 386.0)
    builder.road_stage(5, 29, italy.rome(), italy.chieti(), 234.0)
    builder.road_stage(5, 31, italy.chieti(), italy.macerata(), 236.0)
    builder.road_stage(6, 2, italy.macerata(), italy.bologna(), 282.0)
    builder.road_stage(6, 4, italy.bologna(), italy.trieste(), 349.0)
    builder.road_stage(6, 6, italy.trieste(), italy.milan(), 421.0)
    return builder.build()

def giro1921():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1921)
    builder.road_stage(5, 25, italy.milan(), italy.merano(), 333.0)
    builder.road_stage(5, 27, italy.merano(), italy.bologna(), 348.0)
    builder.road_stage(5, 29, italy.bologna(), italy.perugia(), 321.0)
    builder.road_stage(5, 31, italy.perugia(), italy.chieti(), 328.0)
    builder.road_stage(6, 2, italy.chieti(), italy.naples(), 264.0)
    builder.road_stage(6, 4, italy.naples(), italy.rome(), 299.0)
    builder.road_stage(6, 6, italy.rome(), italy.livorno(), 341.0)
    builder.road_stage(6, 8, italy.livorno(), italy.parma(), 242.0)
    builder.road_stage(6, 10, italy.parma(), italy.turin(), 320.0)
    builder.road_stage(6, 12, italy.turin(), italy.milan(), 305.0)
    return builder.build()

def giro1922():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1922)
    builder.road_stage(5, 24, italy.milan(), italy.padua(), 326.0)
    builder.road_stage(5, 26, italy.padua(), italy.portorose(), 268.0)
    builder.road_stage(5, 28, italy.portorose(), italy.bologna(), 375.0)
    builder.road_stage(5, 30, italy.bologna(), italy.pescara(), 367.0)
    builder.road_stage(6, 1, italy.pescara(), italy.naples(), 267.0)
    builder.road_stage(6, 3, italy.naples(), italy.rome(), 254.0)
    builder.road_stage(6, 5, italy.rome(), italy.florence(), 319.0)
    builder.road_stage(6, 7, italy.florence(), italy.santa_margherita_ligure(), 292.0)
    builder.road_stage(6, 9, italy.genoa(), italy.turin(), 277.0)
    builder.road_stage(6, 11, italy.turin(), italy.milan(), 348.0)
    return builder.build()

def giro1923():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1923)
    builder.road_stage(5, 23, italy.milan(), italy.turin(), 328.0)
    builder.road_stage(5, 25, italy.turin(), italy.genoa(), 312.9)
    builder.road_stage(5, 27, italy.genoa(), italy.florence(), 265.0)
    builder.road_stage(5, 29, italy.florence(), italy.rome(), 288.7)
    builder.road_stage(5, 31, italy.rome(), italy.naples(), 281.5)
    builder.road_stage(6, 2, italy.naples(), italy.chieti(), 283.1)
    builder.road_stage(6, 4, italy.chieti(), italy.bologna(), 383.0)
    builder.road_stage(6, 6, italy.bologna(), italy.trieste(), 362.2)
    builder.road_stage(6, 8, italy.trieste(), italy.mantua(), 357.0)
    builder.road_stage(6, 10, italy.mantua(), italy.milan(), 341.3)
    return builder.build()

def giro1924():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1924)
    builder.road_stage(5, 10, italy.milan(), italy.genoa(), 300.3)
    builder.road_stage(5, 12, italy.genoa(), italy.florence(), 307.9)
    builder.road_stage(5, 14, italy.florence(), italy.rome(), 284.4)
    builder.road_stage(5, 16, italy.rome(), italy.naples(), 249.3)
    builder.road_stage(5, 18, italy.potenza(), italy.taranto(), 265.3)
    builder.road_stage(5, 20, italy.taranto(), italy.foggia(), 230.3)
    builder.road_stage(5, 22, italy.foggia(), italy.l_aquila(), 304.3)
    builder.road_stage(5, 24, italy.l_aquila(), italy.perugia(), 296.0)
    builder.road_stage(5, 26, italy.perugia(), italy.bologna(), 280.7)
    builder.road_stage(5, 28, italy.bologna(), fiume.fiume(), 415.0)
    builder.road_stage(5, 30, fiume.fiume(), italy.verona(), 366.5)
    builder.road_stage(6, 1, italy.verona(), italy.milan(), 313.0)
    return builder.build()

def giro1925():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1925)
    builder.road_stage(5, 16, italy.milan(), italy.turin(), 278.1)
    builder.road_stage(5, 18, italy.turin(), italy.arenzano(), 279.2)
    builder.road_stage(5, 20, italy.arenzano(), italy.pisa(), 315.0)
    builder.road_stage(5, 22, italy.pisa(), italy.rome(), 337.1)
    builder.road_stage(5, 24, italy.rome(), italy.naples(), 260.0)
    builder.road_stage(5, 26, italy.naples(), italy.bari(), 314.2)
    builder.road_stage(5, 28, italy.bari(), italy.benevento(), 234.9)
    builder.road_stage(5, 30, italy.benevento(), italy.sulmona(), 275.0)
    builder.road_stage(6, 1, italy.sulmona(), italy.arezzo(), 376.8)
    builder.road_stage(6, 3, italy.arezzo(), italy.forli(), 224.3)
    builder.road_stage(6, 5, italy.forli(), italy.verona(), 318.0)
    builder.road_stage(6, 7, italy.verona(), italy.milan(), 307.9)
    return builder.build()

def giro1926():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1926)
    builder.road_stage(5, 15, italy.milan(), italy.turin(), 275.0)
    builder.road_stage(5, 17, italy.turin(), italy.genoa(), 250.5)
    builder.road_stage(5, 19, italy.genoa(), italy.florence(), 312.0)
    builder.road_stage(5, 21, italy.florence(), italy.rome(), 287.2)
    builder.road_stage(5, 23, italy.rome(), italy.naples(), 232.1)
    builder.road_stage(5, 25, italy.naples(), italy.foggia(), 262.9)
    builder.road_stage(5, 27, italy.foggia(), italy.sulmona(), 250.8)
    builder.road_stage(5, 29, italy.sulmona(), italy.terni(), 266.5)
    builder.road_stage(5, 31, italy.terni(), italy.bologna(), 357.8)
    builder.road_stage(6, 2, italy.bologna(), italy.udine(), 355.2)
    builder.road_stage(6, 4, italy.udine(), italy.verona(), 291.7)
    builder.road_stage(6, 6, italy.verona(), italy.milan(), 288.0)
    return builder.build()

def giro1927():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1927)
    builder.road_stage(5, 15, italy.milan(), italy.turin(), 288.0)
    builder.road_stage(5, 17, italy.turin(), italy.reggio_emilia(), 321.0)
    builder.road_stage(5, 19, italy.reggio_emilia(), italy.lucca(), 207.0)
    builder.road_stage(5, 21, italy.lucca(), italy.grosseto(), 240.0)
    builder.road_stage(5, 22, italy.grosseto(), italy.rome(), 257.6)
    builder.road_stage(5, 23, italy.rome(), italy.naples(), 256.8)
    builder.road_stage(5, 24, italy.naples(), italy.avellino(), 153.4)
    builder.road_stage(5, 26, italy.avellino(), italy.bari(), 271.8)
    builder.road_stage(5, 27, italy.bari(), italy.campobasso(), 243.6)
    builder.road_stage(5, 29, italy.campobasso(), italy.pescara(), 220.2)
    builder.road_stage(5, 30, italy.pescara(), italy.pesaro(), 218.0)
    builder.road_stage(6, 1, italy.pesaro(), italy.treviso(), 305.6)
    builder.road_stage(6, 2, italy.treviso(), italy.trieste(), 208.2)
    builder.road_stage(6, 4, italy.trieste(), italy.verona(), 275.6)
    builder.road_stage(6, 6, italy.verona(), italy.milan(), 291.5)
    return builder.build()

def giro1928():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1928)
    builder.road_stage(5, 12, italy.milan(), italy.trento(), 233.1)
    builder.road_stage(5, 14, italy.trento(), italy.forli(), 312.6)
    builder.road_stage(5, 16, italy.predappio(), italy.arezzo(), 148.0)
    builder.road_stage(5, 18, italy.arezzo(), italy.sulmona(), 327.9)
    builder.road_stage(5, 20, italy.sulmona(), italy.foggia(), 254.6)
    builder.road_stage(5, 22, italy.foggia(), italy.naples(), 248.3)
    builder.road_stage(5, 24, italy.naples(), italy.rome(), 275.0)
    builder.road_stage(5, 26, italy.rome(), italy.pistoia(), 323.0)
    builder.road_stage(5, 28, italy.pistoia(), italy.modena(), 206.0)
    builder.road_stage(5, 30, italy.modena(), italy.genoa(), 270.0)
    builder.road_stage(6, 1, italy.genoa(), italy.turin(), 195.1)
    builder.road_stage(6, 3, italy.turin(), italy.milan(), 251.0)
    return builder.build()

def giro1929():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1929)
    builder.road_stage(5, 19, italy.rome(), italy.naples(), 235.0)
    builder.road_stage(5, 21, italy.naples(), italy.foggia(), 185.0)
    builder.road_stage(5, 23, italy.foggia(), italy.lecce(), 282.0)
    builder.road_stage(5, 25, italy.lecce(), italy.potenza(), 270.0)
    builder.road_stage(5, 27, italy.potenza(), italy.cosenza(), 264.0)
    builder.road_stage(5, 29, italy.cosenza(), italy.salerno(), 295.0)
    builder.road_stage(5, 31, italy.salerno(), italy.formia(), 220.0)
    builder.road_stage(6, 2, italy.formia(), italy.rome(), 198.0)
    builder.road_stage(6, 3, italy.rome(), italy.orvieto(), 120.0)
    builder.road_stage(6, 4, italy.orvieto(), italy.siena(), 150.0)
    builder.road_stage(6, 5, italy.siena(), italy.la_spezia(), 192.0)
    builder.road_stage(6, 7, italy.la_spezia(), italy.parma(), 135.0)
    builder.road_stage(6, 8, italy.parma(), italy.alessandria(), 152.0)
    builder.road_stage(6, 9, italy.alessandria(), italy.milan(), 216.0)
    return builder.build()

def giro1930():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1930)
    builder.road_stage(5, 17, italy.messina(), italy.catania(), 174.0)
    builder.road_stage(5, 18, italy.catania(), italy.palermo(), 280.0)
    builder.road_stage(5, 20, italy.palermo(), italy.messina(), 257.0)
    builder.road_stage(5, 22, italy.reggio_calabria(), italy.catanzaro(), 173.0)
    builder.road_stage(5, 23, italy.catanzaro(), italy.cosenza(), 118.0)
    builder.road_stage(5, 25, italy.cosenza(), italy.salerno(), 292.0)
    builder.road_stage(5, 27, italy.salerno(), italy.naples(), 180.0)
    builder.road_stage(5, 28, italy.naples(), italy.rome(), 247.0)
    builder.road_stage(5, 30, italy.rome(), italy.teramo(), 203.0)
    builder.road_stage(5, 31, italy.teramo(), italy.ancona(), 185.0)
    builder.road_stage(6, 2, italy.ancona(), italy.forli(), 182.0)
    builder.road_stage(6, 3, italy.forli(), italy.rovigo(), 188.0)
    builder.road_stage(6, 5, italy.rovigo(), italy.asiago(), 150.0)
    builder.road_stage(6, 6, italy.asiago(), italy.brescia(), 186.0)
    builder.road_stage(6, 8, italy.brescia(), italy.milan(), 280.0)
    return builder.build()

def giro1931():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1931)
    builder.road_stage(5, 10, italy.milan(), italy.mantua(), 206.0)
    builder.road_stage(5, 11, italy.mantua(), italy.ravenna(), 216.0)
    builder.road_stage(5, 13, italy.ravenna(), italy.macerata(), 288.0)
    builder.road_stage(5, 15, italy.macerata(), italy.pescara(), 234.0)
    builder.road_stage(5, 17, italy.pescara(), italy.naples(), 282.0)
    builder.road_stage(5, 19, italy.naples(), italy.rome(), 256.0)
    builder.road_stage(5, 21, italy.rome(), italy.perugia(), 247.0)
    builder.road_stage(5, 23, italy.perugia(), italy.montecatini_terme(), 246.0)
    builder.road_stage(5, 25, italy.montecatini_terme(), italy.genoa(), 248.0)
    builder.road_stage(5, 27, italy.genoa(), italy.cuneo(), 263.0)
    builder.road_stage(5, 29, italy.cuneo(), italy.turin(), 252.0)
    builder.road_stage(5, 31, italy.turin(), italy.milan(), 263.0)
    return builder.build()

def giro1932():

    builder = NonConsecutiveStageRaceBuilder(TourOfItaly(), 1932)
    builder.road_stage(5, 14, italy.milan(), italy.vicenza(), 207.0)
    builder.road_stage(5, 15, italy.vicenza(), italy.udine(), 183.0)
    builder.road_stage(5, 17, italy.udine(), italy.ferrara(), 225.0)
    builder.road_stage(5, 18, italy.ferrara(), italy.rimini(), 215.0)
    builder.road_stage(5, 20, italy.rimini(), italy.teramo(), 286.0)
    builder.road_stage(5, 22, italy.teramo(), italy.lanciano(), 220.0)
    builder.road_stage(5, 24, italy.lanciano(), italy.foggia(), 280.0)
    builder.road_stage(5, 26, italy.foggia(), italy.naples(), 217.0)
    builder.road_stage(5, 28, italy.naples(), italy.rome(), 265.0)
    builder.road_stage(5, 30, italy.rome(), italy.florence(), 321.0)
    builder.road_stage(6, 1, italy.florence(), italy.genoa(), 276.0)
    builder.road_stage(6, 3, italy.genoa(), italy.turin(), 267.0)
    builder.road_stage(6, 5, italy.turin(), italy.milan(), 271.0)
    return builder.build()

def giro1933():

    builder = TourOfItalyBuilder(1933,5,6)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 169.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 216.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.pisa(), 191.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.pisa(), italy.florence(), 184.0)

    # Stage 5
    builder.road_stage(italy.florence(), italy.grosseto(), 193.0)

    # Stage 6
    builder.road_stage(italy.grosseto(), italy.rome(), 212.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(italy.rome(), italy.naples(), 228.0)

    # Stage 8
    builder.road_stage(italy.naples(), italy.foggia(), 195.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.foggia(), italy.chieti(), 248.0)

    # Stage 10
    builder.road_stage(italy.chieti(), italy.ascoli_piceno(), 158.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.ascoli_piceno(), italy.riccione(), 208.0)

    # Stage 12
    builder.road_stage(italy.riccione(), italy.bologna(), 189.0)

    # Stage 13
    builder.individual_time_trial(italy.bologna(), italy.ferrara(), 62.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(italy.ferrara(), italy.udine(), 242.0)

    # Stage 15
    builder.road_stage(italy.udine(), italy.bassano_del_grappa(), 213.0)

    # Stage 16
    builder.road_stage(italy.bassano_del_grappa(), italy.bolzano(), 148.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.bolzano(), italy.milan(), 284.0)

    return builder.build()

def giro1934():

    builder = TourOfItalyBuilder(1934,5,19)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 169.2)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 206.5)

    # Transfer day
    builder.rest_day()

    # Stage 3
    builder.road_stage(italy.genoa(), italy.livorno(), 220.5)

    # Stage 4
    builder.individual_time_trial(italy.livorno(), italy.pisa(), 45.0)

    # Stage 5
    builder.road_stage(italy.pisa(), italy.rome(), 333.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.rome(), italy.naples(), 228.0)

    # Stage 7
    builder.road_stage(italy.naples(), italy.bari(), 339.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(italy.bari(), italy.campobasso(), 245.0)

    # Stage 9
    builder.road_stage(italy.campobasso(), italy.teramo(), 283.0)

    # Stage 10
    builder.road_stage(italy.teramo(), italy.ancona(), 214.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.ancona(), italy.rimini(), 213.0)

    # Stage 12
    builder.road_stage(italy.rimini(), italy.florence(), 176.5)

    # Stage 13
    builder.road_stage(italy.florence(), italy.bologna(), 120.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.individual_time_trial(italy.bologna(), italy.ferrara(), 59.0)

    # Stage 15
    builder.road_stage(italy.ferrara(), italy.trieste(), 273.0)

    # Stage 16
    builder.road_stage(italy.trieste(), italy.bassano_del_grappa(), 273.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.bassano_del_grappa(), italy.milan(), 315.0)

    return builder.build()

def giro1935():

    builder = TourOfItalyBuilder(1935,5,18)

    # Stage 1
    builder.road_stage(italy.milan(), italy.cremona(), 165.0)

    # Stage 2
    builder.road_stage(italy.cremona(), italy.mantua(), 175.0)

    # Stage 3
    builder.road_stage(italy.mantua(), italy.rovigo(), 162.0)

    # Stage 4
    builder.road_stage(italy.rovigo(), italy.cesenatico(), 140.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.individual_time_trial(italy.cesena(), italy.riccione(), 35.0)
    builder.road_stage(italy.riccione(), italy.portocivitanova(), 136.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.portocivitanova(), italy.l_aquila(), 171.0)

    # Stage 7
    builder.road_stage(italy.l_aquila(), italy.lanciano(), 146.0)

    # Stage 8
    builder.road_stage(italy.lanciano(), italy.bari(), 308.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.bari(), italy.naples(), 333.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.naples(), italy.rome(), 250.0)

    # Stage 11
    builder.road_stage(italy.rome(), italy.florence(), 317.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.florence(), italy.montecatini_terme(), 134.0)

    # Stages 13a & 13b
    builder.enable_split_stages()
    builder.road_stage(italy.montecatini_terme(), italy.lucca(), 99.0)
    builder.individual_time_trial(italy.lucca(), italy.viareggio(), 55.0)
    builder.disable_split_stages()

    # Stage 14
    builder.road_stage(italy.viareggio(), italy.genoa(), 172.0)

    # Transfer day
    builder.rest_day()
    # Stage 15
    builder.road_stage(italy.genoa(), italy.cuneo(), 148.0)

    # Stage 16
    builder.road_stage(italy.cuneo(), italy.asti(), 91.0)

    # Stage 17
    builder.road_stage(italy.asti(), italy.turin(), 250.0)

    # Stage 18
    builder.road_stage(italy.turin(), italy.milan(), 290.0)

    return builder.build()

def giro1936():

    builder = TourOfItalyBuilder(1936,5,16)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 161.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 206.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.montecatini_terme(), 206.0)

    # Transfer day
    builder.rest_day()
    # Stage 4
    builder.road_stage(italy.montecatini_terme(), italy.grosseto(), 220.0)

    # Stage 5
    builder.road_stage(italy.grosseto(), italy.rome(), 248.0)

    # Transfer day
    builder.rest_day()
    # Stage 6
    builder.road_stage(italy.rome(), italy.naples(), 230.0)

    # Stage 7
    builder.road_stage(italy.naples(), italy.bari(), 283.0)

    # Transfer day
    builder.rest_day()
    # Stage 8
    builder.road_stage(italy.bari(), italy.campobasso(), 243.0)

    # Stage 9
    builder.road_stage(italy.campobasso(), italy.l_aquila(), 204.0)

    # Stage 10
    builder.road_stage(italy.l_aquila(), italy.rieti(), 117.0)

    # Stage 11
    builder.individual_time_trial(italy.rieti(), italy.monte_terminillo(), 20.0)

    # Stage 12
    builder.road_stage(italy.rieti(), italy.florence(), 292.0)

    # Stage 13
    builder.road_stage(italy.florence(), italy.cesenatico(), 139.0)

    # Stage 14
    builder.road_stage(italy.cesenatico(), italy.ferrara(), 155.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(italy.ferrara(), italy.padua(), 106.0)
    builder.individual_time_trial(italy.padua(), italy.venice(), 39.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.venice(), italy.legnago(), 183.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(italy.legnago(), italy.riva_del_garda(), 139.0)
    builder.road_stage(italy.riva_del_garda(), italy.gardone_riviera(), 100.0)
    builder.disable_split_stages()

    # Stage 18
    builder.road_stage(italy.gardone_riviera(), italy.salsomaggiore_terme(), 206.0)

    # Stage 19
    builder.road_stage(italy.salsomaggiore_terme(), italy.milan(), 248.0)

    return builder.build()

def giro1937():

    builder = TourOfItalyBuilder(1937,5,8)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 165.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.acqui_terme(), 148.0)

    # Stage 3
    builder.road_stage(italy.acqui_terme(), italy.genoa(), 158.0)

    # Stage 4
    builder.road_stage(italy.genoa(), italy.viareggio(), 186.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.team_time_trial(italy.viareggio(), italy.marina_di_massa(), 60.0)
    builder.road_stage(italy.marina_di_massa(), italy.livorno(), 114.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.livorno(), italy.arezzo(), 190.0)

    # Stage 7
    builder.road_stage(italy.arezzo(), italy.rieti(), 206.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.individual_time_trial(italy.rieti(), italy.monte_terminillo(), 20.0)
    builder.road_stage(italy.rieti(), italy.rome(), 152.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(italy.rome(), italy.naples(), 250.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.naples(), italy.foggia(), 166.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(italy.foggia(), italy.san_severo(), 186.0)
    builder.road_stage(italy.san_severo(), italy.campobasso(), 105.0)
    builder.disable_split_stages()

    # Stage 12
    builder.road_stage(italy.campobasso(), italy.pescara(), 258.0)

    # Stage 13
    builder.road_stage(italy.pescara(), italy.ancona(), 194.0)

    # Stage 14
    builder.road_stage(italy.ancona(), italy.forli(), 178.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.forli(), italy.vittorio_veneto(), 266.0)

    # Stage 16
    builder.road_stage(italy.vittorio_veneto(), italy.merano(), 227.0)

    # Stage 17
    builder.road_stage(italy.merano(), italy.gardone_riviera(), 190.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.gardone_riviera(), italy.san_pellegrino_terme(), 129.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(italy.san_pellegrino_terme(), italy.como(), 151.0)
    builder.road_stage(italy.como(), italy.milan(), 141.0)
    builder.disable_split_stages()

    return builder.build()

def giro1938():

    builder = TourOfItalyBuilder(1938,5,7)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 182.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.san_remo(), 204.0)

    # Stage 3
    builder.road_stage(italy.san_remo(), italy.santa_margherita_ligure(), 172.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.road_stage(italy.santa_margherita_ligure(), italy.la_spezia(), 81.0)
    builder.road_stage(italy.la_spezia(), italy.montecatini_terme(), 110.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.montecatini_terme(), italy.chianciano_terme(), 184.0)

    # Stage 6
    builder.road_stage(italy.chianciano_terme(), italy.rieti(), 160.0)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.individual_time_trial(italy.rieti(), italy.monte_terminillo(), 19.8)
    builder.road_stage(italy.rieti(), italy.rome(), 152.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(italy.rome(), italy.naples(), 234.0)

    # Transfer day
    builder.rest_day()
    # Stage 9
    builder.road_stage(italy.naples(), italy.lanciano(), 221.0)

    # Stage 10
    builder.road_stage(italy.lanciano(), italy.ascoli_piceno(), 149.0)

    # Stage 11
    builder.road_stage(italy.ascoli_piceno(), italy.ravenna(), 268.0)

    # Stage 12
    builder.road_stage(italy.ravenna(), italy.treviso(), 199.0)

    # Transfer day
    builder.rest_day()
    # Stage 13
    builder.road_stage(italy.treviso(), italy.trieste(), 207.0)

    # Stage 14
    builder.road_stage(italy.trieste(), italy.belluno(), 243.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.belluno(), italy.recoaro_terme(), 154.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.recoaro_terme(), italy.bergamo(), 272.0)

    # Stage 17
    builder.road_stage(italy.bergamo(), italy.varese(), 154.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(italy.varese(), switzerland.locarno(), 100.0)
    builder.road_stage(switzerland.locarno(), italy.milan(), 180.0)
    builder.disable_split_stages()

    return builder.build()

def giro1939():

    builder = TourOfItalyBuilder(1939,4,28)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 180.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 226.7)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.pisa(), 187.0)

    # Stage 4
    builder.road_stage(italy.pisa(), italy.grosseto(), 154.0)

    # Stage 5
    builder.road_stage(italy.grosseto(), italy.rome(), 222.0)

    # Transfer day
    builder.rest_day()

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(italy.rome(), italy.rieti(), 85.7)
    builder.individual_time_trial(italy.rieti(), italy.monte_terminillo(), 14.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(italy.rieti(), italy.pescara(), 191.3)

    # Stage 8
    builder.road_stage(italy.pescara(), italy.senigallia(), 177.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.road_stage(italy.senigallia(), italy.forli(), 116.5)
    builder.road_stage(italy.forli(), italy.florence(), 106.6)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.florence(), italy.bologna(), 120.0)

    # Stage 11
    builder.road_stage(italy.bologna(), italy.venezia(), 231.8)

    # Stage 12
    builder.road_stage(italy.venezia(), italy.trieste(), 173.8)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.individual_time_trial(italy.trieste(), italy.gorizia(), 39.8)

    # Stage 14
    builder.road_stage(italy.gorizia(), italy.cortina_d_ampezzo(), 195.0)

    # Stage 15
    builder.road_stage(italy.cortina_d_ampezzo(), italy.trento(), 256.2)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.trento(), italy.sondrio(), 166.0)

    # Stage 17
    builder.road_stage(italy.sondrio(), italy.milan(), 168.0)

    return builder.build()

def giro1940():

    builder = TourOfItalyBuilder(1940,5,17)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 180.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 226.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.pisa(), 188.0)

    # Stage 4
    builder.road_stage(italy.pisa(), italy.grosseto(), 154.0)

    # Stage 5
    builder.road_stage(italy.grosseto(), italy.rome(), 224.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.rome(), italy.naples(), 238.0)

    # Stage 7
    builder.road_stage(italy.naples(), italy.fiuggi(), 178.0)

    # Stage 8
    builder.road_stage(italy.fiuggi(), italy.terni(), 183.0)

    # Stage 9
    builder.road_stage(italy.terni(), italy.arezzo(), 183.0)

    # Stage 10
    builder.road_stage(italy.arezzo(), italy.florence(), 91.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.florence(), italy.modena(), 184.0)

    # Stage 12
    builder.road_stage(italy.modena(), italy.ferrara(), 184.0)

    # Stage 13
    builder.road_stage(italy.ferrara(), italy.treviso(), 125.0)

    # Stage 14
    builder.road_stage(italy.treviso(), italy.abbazia(), 215.0)

    # Stage 15
    builder.road_stage(italy.abbazia(), italy.trieste(), 179.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.trieste(), italy.pieve_di_cadore(), 202.0)

    # Stage 17
    builder.road_stage(italy.pieve_di_cadore(), italy.ortisei(), 110.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.ortisei(), italy.trento(), 186.0)

    # Stage 19
    builder.road_stage(italy.trento(), italy.verona(), 149.0)

    # Stage 20
    builder.road_stage(italy.verona(), italy.milan(), 180.0)

    return builder.build()

def giro1946():

    builder = TourOfItalyBuilder(1946,6,15)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 185.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 190.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.montecatini_terme(), 222.0)

    # Transfer day
    builder.rest_day()

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.individual_time_trial(italy.montecatini_terme(), italy.prato(), 30.0)
    builder.road_stage(italy.prato(), italy.bologna(), 112.0)
    builder.disable_split_stages()

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(italy.bologna(), italy.cesena(), 80.0)
    builder.road_stage(italy.cesena(), italy.ancona(), 128.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.ancona(), italy.chieti(), 170.0)

    # Stage 7
    builder.road_stage(italy.chieti(), italy.naples(), 244.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(italy.naples(), italy.rome(), 226.0)

    # Stage 9
    builder.road_stage(italy.rome(), italy.perugia(), 191.0)

    # Stage 10
    builder.road_stage(italy.perugia(), italy.florence(), 165.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.florence(), italy.rovigo(), 245.0)

    # Stage 12
    builder.road_stage(italy.rovigo(), italy.trieste(), 132.0)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.road_stage(italy.udine(), italy.auronzo_di_cadore(), 124.5)

    # Stage 14
    builder.road_stage(italy.auronzo_di_cadore(), italy.bassano_del_grappa(), 203.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.bassano_del_grappa(), italy.trento(), 186.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(italy.trento(), italy.verona(), 90.0)
    builder.road_stage(italy.verona(), italy.mantua(), 72.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(italy.mantua(), italy.milan(), 176.0)

    return builder.build()

def giro1947():

    builder = TourOfItalyBuilder(1947,5,24)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 190.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 206.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.reggio_emilia(), 220.0)

    # Stage 4
    builder.road_stage(italy.reggio_emilia(), italy.prato(), 190.0)

    # Transfer day
    builder.rest_day()

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(italy.prato(), italy.bagni_di_casciana_terme(), 84.0)
    builder.road_stage(italy.bagni_di_casciana_terme(), italy.florence(), 141.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(italy.florence(), italy.perugia(), 161.0)

    # Stage 7
    builder.road_stage(italy.perugia(), italy.rome(), 240.0)

    # Stage 8
    builder.road_stage(italy.rome(), italy.naples(), 231.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.naples(), italy.bari(), 288.0)

    # Stage 10
    builder.road_stage(italy.bari(), italy.foggia(), 288.0)

    # Stage 11
    builder.road_stage(italy.foggia(), italy.pescara(), 223.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.pescara(), italy.cesenatico(), 267.0)

    # Stage 13
    builder.road_stage(italy.cesenatico(), italy.padua(), 175.0)

    # Stage 14
    builder.road_stage(italy.padua(), italy.vittorio_veneto(), 132.0)

    # Stage 15
    builder.road_stage(italy.vittorio_veneto(), italy.pieve_di_cadore(), 200.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.pieve_di_cadore(), italy.trento(), 194.0)

    # Stage 17
    builder.road_stage(italy.trento(), italy.brescia_sant_eufemia(), 114.0)

    # Stage 18
    builder.road_stage(italy.brescia_sant_eufemia(), switzerland.lugano(), 180.0)

    # Stage 19
    builder.road_stage(switzerland.lugano(), italy.milan(), 278.0)

    return builder.build()

def giro1948():

    builder = TourOfItalyBuilder(1948,5,15)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 190.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.genoa(), 226.0)

    # Stage 3
    builder.road_stage(italy.genoa(), italy.parma(), 243.0)

    # Stage 4
    builder.road_stage(italy.parma(), italy.viareggio(), 266.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.viareggio(), italy.siena(), 165.0)

    # Stage 6
    builder.road_stage(italy.siena(), italy.rome(), 256.0)

    # Stage 7
    builder.road_stage(italy.rome(), italy.pescara(), 230.0)

    # Stage 8
    builder.road_stage(italy.pescara(), italy.bari(), 347.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.bari(), italy.naples(), 306.0)

    # Stage 10
    builder.road_stage(italy.naples(), italy.fiuggi(), 184.0)

    # Stage 11
    builder.road_stage(italy.fiuggi(), italy.perugia(), 265.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.perugia(), italy.florence(), 169.0)

    # Stage 13
    builder.road_stage(italy.florence(), italy.bologna(), 194.0)

    # Stage 14
    builder.road_stage(italy.bologna(), italy.udine(), 278.0)

    # Stage 15
    builder.road_stage(italy.udine(), italy.auronzo_di_cadore(), 125.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.auronzo_di_cadore(), italy.cortina_d_ampezzo(), 90.0)

    # Stage 17
    builder.road_stage(italy.cortina_d_ampezzo(), italy.trento(), 160.0)

    # Stage 18
    builder.road_stage(italy.trento(), italy.brescia(), 239.0)

    # Stage 19
    builder.road_stage(italy.brescia(), italy.milan(), 231.0)

    return builder.build()

def giro1949():

    builder = TourOfItalyBuilder(1949,5,21)

    # Stage 1
    builder.road_stage(italy.palermo(), italy.catania(), 261.0)

    # Stage 2
    builder.road_stage(italy.catania(), italy.messina(), 163.0)

    # Stage 3
    builder.road_stage(italy.villa_san_giovanni(), italy.cosenza(), 214.0)

    # Stage 4
    builder.road_stage(italy.cosenza(), italy.salerno(), 292.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.salerno(), italy.naples(), 161.0)

    # Stage 6
    builder.road_stage(italy.naples(), italy.rome(), 233.0)

    # Stage 7
    builder.road_stage(italy.rome(), italy.pesaro(), 298.0)

    # Stage 8
    builder.road_stage(italy.pesaro(), italy.venezia(), 273.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.venezia(), italy.udine(), 249.0)

    # Stage 10
    builder.road_stage(italy.udine(), italy.bassano_del_grappa(), 154.0)

    # Stage 11
    builder.road_stage(italy.bassano_del_grappa(), italy.bolzano(), 237.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.bolzano(), italy.modena(), 253.0)

    # Stage 13
    builder.road_stage(italy.modena(), italy.montecatini_terme(), 160.0)

    # Stage 14
    builder.road_stage(italy.montecatini_terme(), italy.genoa(), 228.0)

    # Stage 15
    builder.road_stage(italy.genoa(), italy.san_remo(), 136.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.san_remo(), italy.cuneo(), 190.0)

    # Stage 17
    builder.road_stage(italy.cuneo(), italy.pinerolo(), 254.0)

    # Stage 18
    builder.individual_time_trial(italy.pinerolo(), italy.turin(), 65.0)

    # Stage 19
    builder.road_stage(italy.turin(), italy.milan(), 267.0)

    return builder.build()

def giro1950():

    builder = TourOfItalyBuilder(1950,5,24)

    # Stage 1
    builder.road_stage(italy.milan(), italy.salsomaggiore_terme(), 225.0)

    # Stage 2
    builder.road_stage(italy.salsomaggiore_terme(), italy.florence(), 245.0)

    # Stage 3
    builder.road_stage(italy.florence(), italy.livorno(), 148.0)

    # Stage 4
    builder.road_stage(italy.livorno(), italy.genoa(), 216.0)

    # Stage 5
    builder.road_stage(italy.genoa(), italy.turin(), 216.0)

    # Stage 6
    builder.road_stage(italy.turin(), switzerland.locarno(), 220.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(switzerland.locarno(), italy.brescia(), 293.0)

    # Stage 8
    builder.road_stage(italy.brescia(), italy.vicenza(), 214.0)

    # Stage 9
    builder.road_stage(italy.vicenza(), italy.bolzano(), 2272.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.bolzano(), italy.milan(), 294.0)

    # Stage 11
    builder.road_stage(italy.milan(), italy.ferrara(), 251.0)

    # Stage 12
    builder.road_stage(italy.ferrara(), italy.rimini(), 144.0)

    # Stage 13
    builder.road_stage(italy.rimini(), italy.arezzo(), 244.0)

    # Stage 14
    builder.road_stage(italy.arezzo(), italy.perugia(), 185.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.perugia(), italy.l_aquila(), 185.0)

    # Stage 16
    builder.road_stage(italy.l_aquila(), italy.campobasso(), 203.0)

    # Stage 17
    builder.road_stage(italy.campobasso(), italy.naples(), 167.0)

    # Stage 18
    builder.road_stage(italy.naples(), italy.rome(), 230.0)

    return builder.build()

def giro1951():

    builder = TourOfItalyBuilder(1951,5,19)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 202.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.alassio(), 202.0)

    # Stage 3
    builder.road_stage(italy.alassio(), italy.genoa(), 252.0)

    # Stage 4
    builder.road_stage(italy.genoa(), italy.florence(), 265.0)

    # Stage 5
    builder.road_stage(italy.florence(), italy.perugia(), 192.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.individual_time_trial(italy.perugia(), italy.terni(), 81.0)

    # Stage 7
    builder.road_stage(italy.terni(), italy.rome(), 290.0)

    # Stage 8
    builder.road_stage(italy.rome(), italy.naples(), 234.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.foggia(), 181.0)

    # Stage 10
    builder.road_stage(italy.foggia(), italy.pescara(), 311.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.pescara(), italy.rimini(), 246.0)

    # Stage 12
    builder.individual_time_trial(italy.rimini(), san_marino.san_marino(), 24.0)

    # Stage 13
    builder.road_stage(italy.rimini(), italy.bologna(), 249.0)

    # Stage 14
    builder.road_stage(italy.bologna(), italy.brescia(), 220.0)

    # Stage 15
    builder.road_stage(italy.brescia(), italy.venice(), 188.0)

    # Stage 16
    builder.road_stage(italy.venice(), italy.trieste(), 182.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.trieste(), italy.cortina_d_ampezzo(), 255.0)

    # Stage 18
    builder.road_stage(italy.cortina_d_ampezzo(), italy.bolzano(), 242.0)

    # Stage 19
    builder.road_stage(italy.bolzano(), switzerland.saint_moritz(), 166.0)

    # Stage 20
    builder.road_stage(switzerland.saint_moritz(), italy.milan(), 172.0)

    return builder.build()

def giro1952():

    builder = TourOfItalyBuilder(1952,5,17)

    # Stage 1
    builder.road_stage(italy.milan(), italy.bologna(), 217.0)

    # Stage 2
    builder.road_stage(italy.bologna(), italy.montecatini_terme(), 197.0)

    # Stage 3
    builder.road_stage(italy.montecatini_terme(), italy.siena(), 205.0)

    # Stage 4
    builder.road_stage(italy.siena(), italy.rome(), 250.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.individual_time_trial(italy.rome(), italy.rocca_di_papa(), 35.0)

    # Stage 6
    builder.road_stage(italy.rome(), italy.naples(), 234.0)

    # Stage 7
    builder.road_stage(italy.naples(), italy.roccaraso(), 140.0)

    # Stage 8
    builder.road_stage(italy.roccaraso(), italy.ancona(), 224.0)

    # Stage 9
    builder.road_stage(italy.ancona(), italy.riccione(), 250.0)

    # Stage 10
    builder.road_stage(italy.riccione(), italy.venice(), 285.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.venice(), italy.bolzano(), 276.0)

    # Stage 12
    builder.road_stage(italy.bolzano(), italy.bergamo(), 226.0)

    # Stage 13
    builder.road_stage(italy.bergamo(), italy.como(), 143.0)

    # Stage 14
    builder.individual_time_trial(italy.erba(), italy.como(), 65.0)

    # Stage 15
    builder.road_stage(italy.como(), italy.genoa(), 247.0)

    # Stage 16
    builder.road_stage(italy.genoa(), italy.san_remo(), 141.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.san_remo(), italy.cuneo(), 190.0)

    # Stage 18
    builder.road_stage(italy.cuneo(), italy.saint_vincent(), 190.0)

    # Stage 19
    builder.road_stage(italy.saint_vincent(), italy.verbania(), 298.0)

    # Stage 20
    builder.road_stage(italy.verbania(), italy.milan(), 147.0)

    return builder.build()

def giro1953():

    builder = TourOfItalyBuilder(1953,5,12)

    # Stage 1
    builder.road_stage(italy.milan(), italy.abano_terme(), 263.0)

    # Stage 2
    builder.road_stage(italy.abano_terme(), italy.rimini(), 278.0)

    # Stage 3
    builder.road_stage(italy.rimini(), italy.san_benedetto_del_tronto(), 182.0)

    # Stage 4
    builder.road_stage(italy.san_benedetto_del_tronto(), italy.roccaraso(), 171.0)

    # Stage 5
    builder.road_stage(italy.roccaraso(), italy.naples(), 149.0)

    # Stage 6
    builder.road_stage(italy.naples(), italy.rome(), 285.0)

    # Stages 7a &7b
    builder.enable_split_stages()
    builder.road_stage(italy.rome(), italy.grosseto(), 178.0)
    builder.individual_time_trial(italy.grosseto(), italy.follonica(), 48.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(italy.follonica(), italy.pisa(), 114.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.pisa(), italy.modena(), 189.0)

    # Stage 10
    builder.out_and_back_team_time_trial(italy.modena(), 30.0)

    # Stage 11
    builder.road_stage(italy.modena(), italy.genoa(), 278.0)

    # Stage 12
    builder.road_stage(italy.genoa(), italy.bordighera(), 256.0)

    # Stage 13
    builder.road_stage(italy.bordighera(), italy.turin(), 242.0)

    # Stage 14
    builder.road_stage(italy.turin(), italy.san_pellegrino_terme(), 232.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.san_pellegrino_terme(), italy.riva_del_garda(), 279.0)

    # Stage 16
    builder.road_stage(italy.riva_del_garda(), italy.vicenza(), 166.0)

    # Stage 17
    builder.road_stage(italy.vicenza(), italy.auronzo_di_cadore(), 186.0)

    # Stage 18
    builder.road_stage(italy.auronzo_di_cadore(), italy.bolzano(), 164.0)

    # Stage 19
    builder.road_stage(italy.bolzano(), italy.bormio(), 125.0)

    # Stage 20
    builder.road_stage(italy.bormio(), italy.milan(), 220.0)

    return builder.build()

def giro1954():

    builder = TourOfItalyBuilder(1954,5,21)

    # Stage 1
    builder.out_and_back_team_time_trial(italy.palermo(), 36.0)

    # Stage 2
    builder.road_stage(italy.palermo(), italy.taormina(), 280.0)

    # Stage 3
    builder.road_stage(italy.reggio_calabria(), italy.catanzaro(), 172.0)

    # Stage 4
    builder.road_stage(italy.catanzaro(), italy.bari(), 352.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.bari(), italy.naples(), 279.0)

    # Stage 6
    builder.road_stage(italy.naples(), italy.l_aquila(), 252.0)

    # Stage 7
    builder.road_stage(italy.l_aquila(), italy.rome(), 150.0)

    # Stage 8
    builder.road_stage(italy.rome(), italy.chianciano_terme(), 195.0)

    # Stage 9
    builder.road_stage(italy.chianciano_terme(), italy.florence(), 180.0)

    # Stage 10
    builder.road_stage(italy.florence(), italy.cesenatico(), 211.0)

    # Stage 11
    builder.road_stage(italy.cesenatico(), italy.abetone(), 230.0)

    # Stage 12
    builder.road_stage(italy.abetone(), italy.genoa(), 251.0)

    # Stage 13
    builder.road_stage(italy.genoa(), italy.turin(), 211.0)

    # Stage 14
    builder.road_stage(italy.turin(), italy.brescia(), 240.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.individual_time_trial(italy.gardone_riviera(), italy.riva_del_garda(), 42.0)

    # Stage 16
    builder.road_stage(italy.riva_del_garda(), italy.abano_terme(), 131.0)

    # Stage 17
    builder.road_stage(italy.abano_terme(), italy.padua(), 105.0)

    # Stage 18
    builder.road_stage(italy.padua(), italy.grado(), 177.0)

    # Stage 19
    builder.mountain_stage(italy.grado())
    builder.summit_finish(mountains.dolomites.san_martino_di_castrozza(), ColCategory.C2, 247.0)

    # Stage 20
    builder.road_stage(mountains.dolomites.san_martino_di_castrozza(), italy.bolzano(), 152.0)

    # Stage 21
    builder.road_stage(italy.bolzano(), switzerland.saint_moritz(), 222.0)

    # Stage 22
    builder.road_stage(switzerland.saint_moritz(), italy.milan(), 222.0)

    return builder.build()

def giro1955():

    builder = TourOfItalyBuilder(1955,5,14)

    # Stage 1
    builder.road_stage(italy.milan(), italy.turin(), 163.0)

    # Stage 2
    builder.road_stage(italy.turin(), france.cannes(), 243.0)

    # Stage 3
    builder.road_stage(france.cannes(), italy.san_remo(), 123.0)

    # Stage 4
    builder.road_stage(italy.san_remo(), italy.acqui_terme(), 192.0)

    # Stage 5
    builder.road_stage(italy.acqui_terme(), italy.genoa(), 170.0)

    # Stage 6
    builder.team_time_trial(italy.genoa(), italy.lido_d_albaro(), 18.0)

    # Stage 7
    builder.road_stage(italy.genoa(), italy.viareggio(), 164.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(italy.viareggio(), italy.perugia(), 260.0)

    # Stage 9
    builder.road_stage(italy.perugia(), italy.rome(), 174.0)

    # Stage 10
    builder.criterium(italy.frascati(), 207.0)

    # Stage 11
    builder.road_stage(italy.rome(), italy.naples(), 242.0)

    # Stage 12
    builder.road_stage(italy.naples(), italy.scanno(), 216.0)

    # Stage 13
    builder.road_stage(italy.scanno(), italy.ancona(), 251.0)

    # Stage 14
    builder.road_stage(italy.ancona(), italy.pineta_di_cervia(), 173.0)

    # Stage 15
    builder.individual_time_trial(italy.pineta_di_cervia(), italy.ravenna(), 50.0)

    # Stage 16
    builder.road_stage(italy.ravenna(), italy.lido_di_jesolo(), 245.0)

    # Stage 17
    builder.road_stage(italy.lido_di_jesolo(), italy.trieste(), 150.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.trieste(), italy.cortina_d_ampezzo(), 236.0)

    # Stage 19
    builder.road_stage(italy.cortina_d_ampezzo(), italy.trento(), 227.0)

    # Stage 20
    builder.road_stage(italy.trento(), italy.san_pellegrino_terme(), 216.0)

    # Stage 21
    builder.road_stage(italy.san_pellegrino_terme(), italy.milan(), 141.0)

    return builder.build()

def giro1956():

    builder = TourOfItalyBuilder(1956,5,19)

    # Stage 1
    builder.road_stage(italy.milan(), italy.alessandria(), 210.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(italy.alessandria(), italy.genoa(), 96.0)
    builder.out_and_back_team_time_trial(italy.circuito_di_lido_d_albaro(), 12.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(italy.genoa(), italy.salice_terme(), 152.0)

    # Stage 4
    builder.road_stage(italy.voghera(), italy.mantua(), 198.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(italy.mantua(), italy.rimini(), 228.0)
    builder.out_and_back_individual_time_trial(san_marino.san_marino(), 13.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(italy.rimini(), italy.pescara(), 245.0)

    # Stage 7
    builder.road_stage(italy.pescara(), italy.campobasso(), 205.0)

    # Stage 8
    builder.road_stage(italy.campobasso(), italy.salerno(), 156.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.rome(), italy.grosseto(), 198.0)

    # Stage 10
    builder.road_stage(italy.grosseto(), italy.livorno(), 230.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.individual_time_trial(italy.livorno(), italy.lucca(), 45.0)

    # Stage 12
    builder.road_stage(italy.lucca(), italy.bologna(), 168.0)

    # Stage 13
    builder.individual_time_trial(italy.bologna(), italy.madonna_di_san_luca(), 3.0)

    # Stage 14
    builder.road_stage(italy.bologna(), italy.rapallo(), 271.0)

    # Stage 15
    builder.road_stage(italy.rapallo(), italy.lecco(), 278.0)

    # Stage 16
    builder.road_stage(italy.lecco(), italy.sondrio(), 98.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.sondrio(), italy.merano(), 163.0)

    # Stage 18
    builder.road_stage(italy.merano(), italy.monte_bondone(), 242.0)

    # Stage 19
    builder.road_stage(italy.trento(), italy.san_pellegrino_terme(), 191.0)

    # Stage 20
    builder.road_stage(italy.san_pellegrino_terme(), italy.milan(), 113.0)

    return builder.build()

def giro1957():

    builder = TourOfItalyBuilder(1957,5,18)

    # Stage 1
    builder.road_stage(italy.milan(), italy.verona(), 191.0)

    # Stage 2
    builder.individual_time_trial(italy.verona(), italy.bosco_chiesanuova(), 28.0)

    # Stage 3
    builder.road_stage(italy.verona(), italy.ferrara(), 169.0)

    # Stage 4
    builder.road_stage(italy.ferrara(), italy.cattolica(), 190.0)

    # Stage 5
    builder.road_stage(italy.cattolica(), italy.loreto(), 235.0)

    # Stage 6
    builder.road_stage(italy.loreto(), italy.terni(), 175.0)

    # Stage 7
    builder.road_stage(italy.terni(), italy.pescara(), 221.0)

    # Stage 8
    builder.road_stage(italy.pescara(), italy.naples(), 250.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.frascati(), 220.0)

    # Stage 10
    builder.road_stage(italy.rome(), italy.siena(), 227.0)

    # Stage 11
    builder.road_stage(italy.siena(), italy.montecatini_terme(), 230.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.individual_time_trial(italy.montecatini(), italy.forte_dei_marmi(), 58.0)

    # Stage 13
    builder.road_stage(italy.forte_dei_marmi(), italy.genoa(), 163.0)

    # Stage 14
    builder.road_stage(italy.genoa(), italy.saint_vincent(), 235.0)

    # Stage 15
    builder.road_stage(italy.saint_vincent(), switzerland.sion(), 134.0)

    # Stage 16
    builder.road_stage(switzerland.sion(), italy.campo_dei_fiori(), 229.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(italy.varese(), italy.como(), 82.0)
    builder.criterium(italy.como(), 34.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.como(), italy.monte_bondone(), 242.0)

    # Stage 19
    builder.road_stage(italy.trento(), italy.levico_terme(), 199.0)

    # Stage 20
    builder.road_stage(italy.levico_terme(), italy.abano_terme(), 157.0)

    # Stage 21
    builder.road_stage(italy.abano_terme(), italy.milan(), 257.0)

    return builder.build()

def giro1958():

    builder = TourOfItalyBuilder(1958,5,18)

    # Stage 1
    builder.road_stage(italy.milan(), italy.varese(), 178.0)

    # Stage 2
    builder.individual_time_trial(italy.varese(), italy.comerio(), 26.0)

    # Stage 3
    builder.road_stage(italy.varese(), italy.saint_vincent(), 187.0)

    # Stage 4
    builder.road_stage(italy.saint_vincent(), italy.collina_di_superga(), 132.0)

    # Stage 5
    builder.road_stage(italy.turin(), italy.mondovi(), 193.0)

    # Stage 6
    builder.road_stage(italy.mondovi(), italy.chiavari(), 258.0)

    # Stage 7
    builder.road_stage(italy.chiavari(), italy.forte_dei_marmi(), 115.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.out_and_back_individual_time_trial(italy.viareggio(), 59.1)

    # Stage 9
    builder.road_stage(italy.florence(), italy.viterbo(), 215.0)

    # Stage 10
    builder.road_stage(italy.viterbo(), italy.rome(), 155.0)

    # Stage 11
    builder.road_stage(italy.rome(), italy.scanno(), 225.0)

    # Stage 12
    builder.road_stage(italy.scanno(), italy.san_benedetto_del_tronto(), 211.0)

    # Stage 13
    builder.road_stage(italy.san_benedetto_del_tronto(), italy.cattolica(), 192.0)

    # Stage 14
    builder.out_and_back_individual_time_trial(san_marino.san_marino(), 12.0)

    # Stage 15
    builder.road_stage(italy.cesena(), italy.bosco_chiesanuova(), 249.0)

    # Stage 16
    builder.road_stage(italy.verona(), italy.levico_terme(), 200.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.levico_terme(), italy.bolzano(), 198.0)

    # Stage 18
    builder.road_stage(italy.bolzano(), italy.trento(), 183.0)

    # Stage 19
    builder.road_stage(italy.trento(), italy.gardone_riviera(), 176.0)

    # Stage 20
    builder.road_stage(italy.salo(), italy.milan(), 177.0)

    return builder.build()

def giro1959():

    builder = TourOfItalyBuilder(1959,5,16)

    # Stage 1
    builder.road_stage(italy.milan(), italy.salsomaggiore_terme(), 135.0)

    # Stage 2
    builder.out_and_back_individual_time_trial(italy.salsomaggiore_terme(), 22.0)

    # Stage 3
    builder.road_stage(italy.salsomaggiore_terme(), italy.abetone(), 180.0)

    # Stage 4
    builder.road_stage(italy.abetone(), italy.arezzo(), 178.0)

    # Stage 5
    builder.road_stage(italy.arezzo(), italy.rome(), 243.0)

    # Stage 6
    builder.road_stage(italy.rome(), italy.naples(), 213.0)

    # Stage 7
    builder.individual_time_trial(italy.ercolano(), italy.mount_vesuvius(), 8.0)

    # Stage 8
    builder.out_and_back_individual_time_trial(italy.ischia(), 31.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.vasto(), 206.0)

    # Stage 10
    builder.road_stage(italy.vasto(), italy.teramo(), 148.0)

    # Stage 11
    builder.road_stage(italy.ascoli_piceno(), italy.rimini(), 245.0)

    # Stage 12
    builder.road_stage(italy.rimini(), san_marino.san_marino(), 141.0)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.road_stage(italy.rimini(), italy.verona(), 233.0)

    # Stage 14
    builder.road_stage(italy.verona(), italy.rovereto(), 143.0)

    # Stage 15
    builder.road_stage(italy.trento(), italy.bolzano(), 198.0)

    # Stage 16
    builder.road_stage(italy.bolzano(), italy.san_pellegrino_terme(), 245.0)

    # Stage 17
    builder.road_stage(italy.san_pellegrino_terme(), italy.genoa(), 241.0)

    # Stage 18
    builder.road_stage(italy.genoa(), italy.turin(), 180.0)

    # Stage 19
    builder.individual_time_trial(italy.turin(), italy.susa(), 51.0)

    # Stage 20
    builder.road_stage(italy.turin(), italy.saint_vincent(), 100.0)

    # Stage 21
    builder.road_stage(italy.aosta(), italy.courmayeur(), 296.0)

    # Stage 22
    builder.road_stage(italy.courmayeur(), italy.milan(), 220.0)

    return builder.build()

def giro1960():

    builder = TourOfItalyBuilder(1960,5,19)

    # Stage 1
    builder.road_stage(italy.rome(), italy.naples(), 212.0)

    # Stage 2
    builder.out_and_back_individual_time_trial(italy.sorrento(), 25.0)

    # Stage 3
    builder.road_stage(italy.sorrento(), italy.campobasso(), 186.0)

    # Stage 4
    builder.road_stage(italy.campobasso(), italy.pescara(), 192.0)

    # Stage 5
    builder.road_stage(italy.pescara(), italy.rieti(), 218.0)

    # Stage 6
    builder.road_stage(italy.terni(), italy.rimini(), 230.0)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(italy.igea_marina(), 5.0)
    builder.road_stage(italy.bellaria(), italy.forli(), 81.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(italy.forli(), italy.livorno(), 206.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.road_stage(italy.livorno(), italy.carrara(), 93.0)
    builder.individual_time_trial(italy.carrara(), italy.cave_di_carrara(), 2.2)
    builder.disable_split_stages()

    # Stage 10
    builder.road_stage(italy.carrara(), italy.sestri_levante(), 171.0)

    # Stage 11
    builder.road_stage(italy.sestri_levante(), italy.asti(), 180.0)

    # Stage 12
    builder.mountain_stage(italy.asti())
    builder.summit_finish(mountains.alps.cervinia(), ColCategory.C1, 176.0)

    # Stage 13
    builder.road_stage(italy.saint_vincent(), italy.milan(), 225.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.individual_time_trial(italy.seregno(), italy.lecco(), 68.0)

    # Stage 15
    builder.road_stage(italy.lecco(), italy.verona(), 150.0)

    # Stage 16
    builder.road_stage(italy.verona(), italy.treviso(), 110.0)

    # Stage 17
    builder.road_stage(italy.treviso(), italy.trieste(), 147.0)

    # Stage 18
    builder.road_stage(italy.trieste(), italy.belluno(), 240.0)

    # Stage 19
    builder.road_stage(italy.belluno(), italy.trento(), 110.0)

    # Stage 20
    builder.road_stage(italy.trento(), italy.bormio(), 229.0)

    # Stage 21
    builder.road_stage(italy.bormio(), italy.milan(), 225.0)

    return builder.build()

def giro1961():

    builder = TourOfItalyBuilder(1961,5,20)

    # Stage 1
    builder.criterium(italy.turin(), 115.0)

    # Stage 2
    builder.road_stage(italy.turin(), italy.san_remo(), 185.0)

    # Stage 3
    builder.road_stage(italy.san_remo(), italy.genoa(), 149.0)

    # Stage 4
    builder.criterium(italy.cagliari(), 118.0)

    # Stage 5
    builder.road_stage(italy.marsala(), italy.palermo(), 144.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.palermo(), italy.milazzo(), 224.0)

    # Stage 7
    builder.road_stage(italy.reggio_calabria(), italy.cosenza(), 221.0)

    # Stage 8
    builder.road_stage(italy.cosenza(), italy.taranto(), 237.0)

    # Stage 9
    builder.individual_time_trial(italy.castellana_grotte(), italy.bari(), 53.0)

    # Stage 10
    builder.road_stage(italy.bari(), italy.potenza(), 140.0)

    # Stage 11
    builder.road_stage(italy.potenza(), italy.teano(), 252.0)

    # Stage 12
    builder.road_stage(italy.gaeta(), italy.rome(), 149.0)

    # Stage 13
    builder.road_stage(italy.mentana(), italy.castelfidardo(), 279.0)

    # Stage 14
    builder.road_stage(italy.ancona(), italy.florence(), 250.0)

    # Stage 15
    builder.road_stage(italy.florence(), italy.modena(), 178.0)

    # Stage 16
    builder.road_stage(italy.modena(), italy.vicenza(), 207.0)

    # Stage 17
    builder.road_stage(italy.vicenza(), italy.trieste(), 204.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.trieste(), italy.vittorio_veneto(), 161.0)

    # Stage 19
    builder.road_stage(italy.vittorio_veneto(), italy.trento(), 249.0)

    # Stage 20
    builder.road_stage(italy.trento(), italy.bormio(), 275.0)

    # Stage 21
    builder.road_stage(italy.bormio(), italy.milan(), 214.0)

    return builder.build()

def giro1962():

    builder = TourOfItalyBuilder(1962,5,19)

    # Stage 1
    builder.road_stage(italy.milan(), italy.tabiano_terme(), 185.0)

    # Stage 2
    builder.road_stage(italy.salsomaggiore_terme(), italy.sestri_levante(), 158.0)

    # Stage 3
    builder.road_stage(italy.sestri_levante(), italy.panicagliora_marliana(), 225.0)

    # Stage 4
    builder.road_stage(italy.montecatini_terme(), italy.perugia(), 248.0)

    # Stage 5
    builder.road_stage(italy.perugia(), italy.rieti(), 258.0)

    # Stage 6
    builder.road_stage(italy.rieti(), italy.fiuggi(), 193.0)

    # Stage 7
    builder.road_stage(italy.fiuggi(), italy.montevergine_di_mercogliano(), 224.0)

    # Stage 8
    builder.road_stage(italy.avellino(), italy.foggia(), 110.0)

    # Stage 9
    builder.road_stage(italy.foggia(), italy.chieti(), 205.0)

    # Stage 10
    builder.road_stage(italy.chieti(), italy.fano(), 218.0)

    # Stage 11
    builder.road_stage(italy.fano(), italy.castrocaro_terme(), 170.0)

    # Stage 12
    builder.road_stage(italy.forli(), italy.lignano_sabbiadoro(), 298.0)

    # Stage 13
    builder.road_stage(italy.lignano_sabbiadoro(), italy.nevegal(), 173.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.mountain_stage(italy.belluno())
    builder.summit_finish(mountains.dolomites.passo_rolle(), ColCategory.C2, 160.0)

    # Stage 15
    builder.mountain_stage(italy.moena())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 215.0)

    # Stage 16
    builder.road_stage(mountains.alps.aprica(), italy.pian_del_resinelli(), 123.0)

    # Stage 17
    builder.road_stage(italy.lecco(), italy.casale_monferrato(), 194.0)

    # Stage 18
    builder.road_stage(italy.casale_monferrato(), italy.frabosa_soprana(), 232.0)

    # Stage 19
    builder.road_stage(italy.frabosa_soprana(), italy.saint_vincent(), 193.0)

    # Stage 20
    builder.criterium(italy.saint_vincent(), 238.0)

    # Stage 21
    builder.road_stage(italy.saint_vincent(), italy.milan(), 160.0)

    return builder.build()

def giro1963():

    builder = TourOfItalyBuilder(1963,5,19)

    # Stage 1
    builder.road_stage(italy.naples(), italy.potenza(), 182.0)

    # Stage 2
    builder.road_stage(italy.potenza(), italy.bari(), 185.0)

    # Stage 3
    builder.road_stage(italy.bari(), italy.campobasso(), 252.0)

    # Stage 4
    builder.road_stage(italy.campobasso(), italy.pescara(), 213.0)

    # Stage 5
    builder.road_stage(italy.pescara(), italy.viterbo(), 263.0)

    # Stage 6
    builder.road_stage(italy.bolsena(), italy.arezzo(), 192.0)

    # Stage 7
    builder.road_stage(italy.arezzo(), italy.riolo_terme(), 173.0)

    # Stage 8
    builder.road_stage(italy.riolo_terme(), italy.salsomaggiore_terme(), 203.0)

    # Stage 9
    builder.road_stage(italy.salsomaggiore_terme(), italy.la_spezia(), 173.0)

    # Stage 10
    builder.road_stage(italy.la_spezia(), italy.asti(), 225.0)

    # Stage 11
    builder.road_stage(italy.asti(), italy.santuario_di_oropa(), 130.0)

    # Stage 12
    builder.road_stage(italy.biella(), switzerland.leukerbad(), 214.0)

    # Stage 13
    builder.road_stage(switzerland.leukerbad(), italy.saint_vincent(), 152.0)

    # Stage 14
    builder.road_stage(italy.saint_vincent(), italy.cremona(), 260.0)

    # Stage 15
    builder.road_stage(italy.mantua(), italy.treviso(), 155.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.out_and_back_individual_time_trial(italy.treviso(), 56.0)

    # Stage 17
    builder.road_stage(italy.treviso(), italy.gorizia(), 213.0)

    # Stage 18
    builder.road_stage(italy.gorizia(), italy.belluno_nevegal(), 248.0)

    # Stage 19
    builder.road_stage(italy.belluno(), italy.moena(), 198.0)

    # Stage 20
    builder.road_stage(italy.moena(), italy.lumezzane(), 240.0)

    # Stage 21
    builder.road_stage(italy.brescia(), italy.milan(), 136.0)

    return builder.build()

def giro1964():

    builder = TourOfItalyBuilder(1964,5,16)

    # Stage 1
    builder.road_stage(italy.bolzano(), italy.riva_del_garda(), 173.0)

    # Stage 2
    builder.road_stage(italy.riva_del_garda(), italy.brescia(), 146.0)

    # Stage 3
    builder.road_stage(italy.brescia(), italy.san_pellegrino_terme(), 193.0)

    # Stage 4
    builder.road_stage(italy.san_pellegrino_terme(), italy.parma(), 189.0)

    # Stage 5
    builder.individual_time_trial(italy.parma(), italy.busseto(), 50.0)

    # Stage 6
    builder.road_stage(italy.parma(), italy.verona(), 100.0)

    # Stage 7
    builder.road_stage(italy.verona(), italy.lavarone(), 168.0)

    # Stage 8
    builder.road_stage(italy.lavarone(), italy.pedavena(), 183.0)

    # Stage 9
    builder.road_stage(italy.feltre(), italy.marina_di_ravenna(), 260.0)

    # Stage 10
    builder.road_stage(italy.marina_di_ravenna(), san_marino.san_marino(), 135.0)

    # Stage 11
    builder.road_stage(italy.rimini(), italy.san_benedetto_del_tronto(), 185.0)

    # Stage 12
    builder.road_stage(italy.san_benedetto_del_tronto(), italy.roccaraso(), 257.0)

    # Stage 13
    builder.road_stage(italy.roccaraso(), italy.caserta(), 188.0)

    # Stage 14
    builder.road_stage(italy.caserta(), italy.castel_gandolfo(), 210.0)

    # Stage 15
    builder.road_stage(italy.rome(), italy.montepulciano(), 214.0)

    # Stage 16
    builder.road_stage(italy.montepulciano(), italy.livorno(), 199.0)

    # Stage 17
    builder.road_stage(italy.livorno(), italy.santa_margherita_ligure(), 210.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.santa_margherita_ligure(), italy.alessandria(), 205.0)

    # Stage 19
    builder.road_stage(italy.alessandria(), italy.cuneo(), 205.0)

    # Stage 20
    builder.road_stage(italy.cuneo(), italy.pinerolo(), 254.0)

    # Stage 21
    builder.road_stage(italy.turin(), italy.biella(), 200.0)

    # Stage 22
    builder.road_stage(italy.biella(), italy.milan(), 146.0)

    return builder.build()

def giro1965():

    builder = TourOfItalyBuilder(1965,5,15)

    # Stage 1
    builder.road_stage(san_marino.san_marino(), italy.perugia(), 198.0)

    # Stage 2
    builder.road_stage(italy.perugia(), italy.l_aquila(), 180.0)

    # Stage 3
    builder.road_stage(italy.l_aquila(), italy.rocca_di_cambio(), 199.0)

    # Stage 4
    builder.road_stage(italy.rocca_di_cambio(), italy.benevento(), 239.0)

    # Stage 5
    builder.road_stage(italy.benevento(), italy.avellino(), 175.0)

    # Stage 6
    builder.road_stage(italy.avellino(), italy.potenza(), 161.0)

    # Stage 7
    builder.road_stage(italy.potenza(), italy.maratea(), 164.0)

    # Stage 8
    builder.road_stage(italy.maratea(), italy.catanzaro(), 103.0)

    # Stage 9
    builder.road_stage(italy.catanzaro(), italy.reggio_calabria(), 161.0)

    # Stage 10
    builder.road_stage(italy.messina(), italy.palermo(), 260.0)

    # Stage 11
    builder.road_stage(italy.palermo(), italy.agrigento(), 146.0)

    # Stage 12
    builder.road_stage(italy.agrigento(), italy.siracusa(), 230.0)

    # Stage 13
    builder.individual_time_trial(italy.catania(), italy.taormina(), 50.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(italy.milan(), italy.novi_ligure(), 100.0)

    # Stage 15
    builder.road_stage(italy.novi_ligure(), italy.diano_marina(), 223.0)

    # Stage 16
    builder.road_stage(italy.diano_marina(), italy.turin(), 205.0)

    # Stage 17
    builder.road_stage(italy.turin(), italy.biandronno(), 163.0)

    # Stage 18
    builder.road_stage(italy.biandronno(), switzerland.saas_fee(), 178.0)

    # Stage 19
    builder.road_stage(switzerland.saas_fee(), italy.madesimo(), 282.0)

    # Stage 20
    builder.mountain_stage(italy.madesimo())
    builder.summit_finish(mountains.alps.passo_dello_stelvio(), ColCategory.C1, 160.0)

    # Stage 21
    builder.road_stage(italy.bormio(), italy.brescia(), 179.0)

    # Stage 22
    builder.road_stage(italy.brescia(), italy.florence(), 295.0)

    return builder.build()

def giro1966():

    builder = TourOfItalyBuilder(1966,5,18)

    # Stage 1
    builder.road_stage(monaco.monte_carlo(), italy.diano_marina(), 149.0)

    # Stage 2
    builder.road_stage(italy.imperia(), italy.monesi(), 60.0)

    # Stage 3
    builder.road_stage(italy.diano_marina(), italy.genoa(), 120.0)

    # Stage 4
    builder.road_stage(italy.genoa(), italy.viareggio(), 241.0)

    # Stage 5
    builder.road_stage(italy.viareggio(), italy.chianciano_terme(), 222.0)

    # Stage 6
    builder.road_stage(italy.chianciano_terme(), italy.rome(), 226.0)

    # Stage 7
    builder.road_stage(italy.rome(), italy.rocca_di_cambio(), 158.0)

    # Stage 8
    builder.road_stage(italy.rocca_di_cambio(), italy.naples(), 238.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.campobasso(), 210.0)

    # Stage 10
    builder.road_stage(italy.campobasso(), italy.guilianova(), 221.0)

    # Stage 11
    builder.road_stage(italy.guilianova(), italy.cesenatico(), 229.0)

    # Stage 12
    builder.road_stage(italy.cesenatico(), italy.reggio_emilia(), 206.0)

    # Stage 13
    builder.out_and_back_individual_time_trial(italy.parma(), 46.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(italy.parma(), italy.arona(), 267.0)

    # Stage 15
    builder.road_stage(italy.arona(), italy.brescia(), 196.0)

    # Stage 16
    builder.road_stage(italy.brescia(), italy.bezzecca(), 143.0)

    # Stage 17
    builder.road_stage(italy.riva_del_garda(), italy.levico_terme(), 239.0)

    # Stage 18
    builder.road_stage(italy.levico_terme(), italy.bolzano(), 137.0)

    # Stage 19
    builder.road_stage(italy.bolzano(), italy.moena(), 100.0)

    # Stage 20
    builder.road_stage(italy.moena(), italy.belluno(), 215.0)

    # Stage 21
    builder.road_stage(italy.belluno(), italy.vittorio_veneto(), 181.0)

    # Stage 22
    builder.road_stage(italy.vittorio_veneto(), italy.trieste(), 172.0)

    return builder.build()

def giro1967():

    builder = TourOfItalyBuilder(1967,5,20)

    # Stage 1
    builder.road_stage(italy.treviglio(), italy.alessandria(), 135.0)

    # Stage 2
    builder.road_stage(italy.alessandria(), italy.la_spezia(), 223.0)

    # Stage 3
    builder.road_stage(italy.la_spezia(), italy.prato(), 205.0)

    # Stage 4
    builder.road_stage(italy.florence(), italy.chianciano_terme(), 155.0)

    # Stage 5
    builder.road_stage(italy.rome(), italy.naples(), 220.0)

    # Stage 6
    builder.criterium(italy.palermo(), 63.0)

    # Stage 7
    builder.road_stage(italy.catania(), italy.etna(), 169.0)

    # Stage 8
    builder.road_stage(italy.reggio_calabria(), italy.cosenza(), 218.0)

    # Stage 9
    builder.road_stage(italy.cosenza(), italy.taranto(), 202.0)

    # Stage 10
    builder.road_stage(italy.bari(), italy.potenza(), 145.0)

    # Stage 11
    builder.road_stage(italy.potenza(), italy.salerno(), 160.0)

    # Stage 12
    builder.road_stage(italy.caserta(), italy.blockhaus(), 220.0)

    # Stage 13
    builder.road_stage(italy.chieti(), italy.riccione(), 253.0)

    # Stage 14
    builder.road_stage(italy.riccione(), italy.lido_degli_estensi(), 94.0)

    # Stage 15
    builder.road_stage(italy.lido_degli_estensi(), italy.mantua(), 164.0)

    # Stage 16
    builder.individual_time_trial(italy.mantua(), italy.verona(), 45.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.verona(), italy.vicenza(), 140.0)

    # Stage 18
    builder.road_stage(italy.vicenza(), italy.udine(), 167.0)

    # Stage 19
    builder.road_stage(italy.udine(), italy.tre_cime_di_lavaredo(), 170.0)

    # Stage 20
    builder.road_stage(italy.cortina_d_ampezzo(), italy.trento(), 235.0)

    # Stage 21
    builder.road_stage(italy.trento(), italy.tirano(), 153.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.mountain_stage(italy.tirano())
    builder.summit_finish(mountains.alps.madonna_del_ghisallo(), ColCategory.C3, 137.0)
    builder.road_stage(mountains.alps.madonna_del_ghisallo(), italy.milan(), 68.0)
    builder.disable_split_stages()

    return builder.build()

def giro1968():

    builder = TourOfItalyBuilder(1968,5,20)

    # Prologue
    builder.out_and_back_prologue(italy.campione_d_italia(), 5.7)
    # Stage 1
    builder.road_stage(italy.campione_d_italia(), italy.novara(), 128.0)

    # Stage 2
    builder.road_stage(italy.novara(), italy.saint_vincent(), 189.0)

    # Stage 3
    builder.road_stage(italy.saint_vincent(), italy.alba(), 168.0)

    # Stage 4
    builder.road_stage(italy.alba(), italy.san_remo(), 162.0)

    # Stage 5
    builder.criterium(italy.san_remo(), 149.0)

    # Stage 6
    builder.road_stage(italy.san_remo(), italy.alessandria(), 223.0)

    # Stage 7
    builder.road_stage(italy.alessandria(), italy.piacenza(), 174.0)

    # Stage 8
    builder.road_stage(italy.san_giorgio_piacentino(), italy.brescia(), 225.0)

    # Stage 9
    builder.road_stage(italy.brescia(), italy.lido_di_caldonazzo(), 210.0)

    # Stage 10
    builder.mountain_stage(italy.trento())
    builder.summit_finish(mountains.dolomites.monte_grappa(), ColCategory.C1, 136.0)

    # Stage 11
    builder.road_stage(italy.bassano_del_grappa(), italy.trieste(), 197.0)

    # Stage 12
    builder.road_stage(italy.gorizia(), italy.tre_cime_di_lavaredo(), 213.0)

    # Stage 13
    builder.road_stage(italy.cortina_d_ampezzo(), italy.vittorio_veneto(), 163.0)

    # Stage 14
    builder.road_stage(italy.vittorio_veneto(), italy.marina_romea(), 199.0)

    # Stage 15
    builder.road_stage(italy.ravenna(), italy.imola(), 141.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.individual_time_trial(italy.cesenatico(), san_marino.san_marino(), 49.3)

    # Stage 17
    builder.road_stage(san_marino.san_marino(), italy.foligno(), 196.0)

    # Stage 18
    builder.road_stage(italy.foligno(), italy.abbadia_san_salvatore(), 166.0)

    # Stage 19
    builder.road_stage(italy.abbadia_san_salvatore(), italy.rome(), 181.0)

    # Stage 20
    builder.road_stage(italy.rome(), italy.rocca_di_cambio(), 215.0)

    # Stage 21
    builder.road_stage(italy.rocca_di_cambio(), italy.blockhaus(), 198.0)

    # Stage 22
    builder.road_stage(italy.chieti(), italy.naples(), 235.0)

    return builder.build()

def giro1969():

    builder = TourOfItalyBuilder(1969,5,16)

    # Stage 1
    builder.road_stage(italy.garda(), italy.brescia(), 142.0)

    # Stage 2
    builder.road_stage(italy.brescia(), italy.mirandola(), 180.0)

    # Stage 3
    builder.road_stage(italy.mirandola(), italy.montecatini_terme(), 188.0)

    # Stage 4
    builder.out_and_back_individual_time_trial(italy.montecatini_terme(), 21.0)

    # Stage 5
    builder.road_stage(italy.montecatini_terme(), italy.follonica(), 194.0)

    # Stage 6
    builder.road_stage(italy.follonica(), italy.viterbo(), 198.0)

    # Stage 7
    builder.road_stage(italy.viterbo(), italy.terracina(), 206.0)

    # Stage 8
    builder.road_stage(italy.terracina(), italy.naples(), 133.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.potenza(), 173.0)

    # Stage 10
    builder.road_stage(italy.potenza(), italy.campitello_matese(), 254.0)

    # Stage 11
    builder.road_stage(italy.campitello_matese(), italy.scanno(), 165.0)

    # Stage 12
    builder.road_stage(italy.scanno(), italy.silvi_marina(), 180.0)

    # Stage 13
    builder.road_stage(italy.silvi_marina(), italy.senigallia(), 166.0)

    # Stage 14
    builder.road_stage(italy.senigallia(), san_marino.san_marino(), 185.0)

    # Stage 15
    builder.individual_time_trial(italy.cesenatico(), san_marino.san_marino(), 49.3)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.parma(), italy.savona(), 234.0)

    # Stage 17
    builder.road_stage(italy.celle_ligure(), italy.pavia(), 182.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(italy.pavia(), italy.zingonia(), 115.0)
    builder.road_stage(italy.zingonia(), italy.san_pellegrino_terme(), 100.0)
    builder.disable_split_stages()

    # Stage 19
    builder.road_stage(italy.san_pellegrino_terme(), italy.folgaria(), 248.0)

    # Stage 20
    builder.road_stage(italy.trento(), italy.marmolada(), 230.0)

    # Stage 21
    builder.road_stage(italy.rocca_pietore(), italy.cavalese(), 131.0)

    # Stage 22
    builder.road_stage(italy.cavalese(), italy.folgarida(), 150.0)

    # Stage 23
    builder.road_stage(italy.folgarida(), italy.milan(), 257.0)

    return builder.build()

def giro1970():

    builder = TourOfItalyBuilder(1970,5,18)

    # Stage 1
    builder.road_stage(italy.san_pellegrino_terme(), italy.biandronno(), 115.0)

    # Stage 2
    builder.road_stage(italy.comerio(), italy.saint_vincent(), 164.0)

    # Stage 3
    builder.road_stage(italy.saint_vincent(), italy.aosta(), 162.0)

    # Stage 4
    builder.road_stage(italy.saint_vincent(), italy.lodi(), 205.0)

    # Stage 5
    builder.road_stage(italy.lodi(), italy.zingonia(), 155.0)

    # Stage 6
    builder.road_stage(italy.zingonia(), italy.malcesine(), 212.0)

    # Stage 7
    builder.road_stage(italy.malcesine(), italy.brentonico(), 130.0)

    # Stage 8
    builder.road_stage(italy.rovereto(), italy.bassano_del_grappa(), 130.0)

    # Stage 9
    builder.individual_time_trial(italy.bassano_del_grappa(), italy.treviso(), 56.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.terracina(), italy.rivisondoli(), 172.0)

    # Stage 11
    builder.road_stage(italy.rivisondoli(), italy.francavilla_al_mare(), 180.0)

    # Stage 12
    builder.road_stage(italy.francavilla_al_mare(), italy.loreto(), 175.0)

    # Stage 13
    builder.road_stage(italy.loreto(), italy.faenza(), 188.0)

    # Stage 14
    builder.road_stage(italy.faenza(), italy.casciana_terme(), 218.0)

    # Stage 15
    builder.road_stage(italy.casciana_terme(), italy.mirandola(), 215.0)

    # Stage 16
    builder.road_stage(italy.mirandola(), italy.lido_di_jesolo(), 195.0)

    # Stage 17
    builder.road_stage(italy.lido_di_jesolo(), italy.arta_terme(), 165.0)

    # Stage 18
    builder.road_stage(italy.arta_terme(), italy.marmolada(), 180.0)

    # Stage 19
    builder.road_stage(italy.rocca_pietore(), italy.dobbiaco(), 120.0)

    # Stage 20
    builder.road_stage(italy.dobbiaco(), italy.bolzano(), 155.0)

    return builder.build()

def giro1971():

    builder = TourOfItalyBuilder(1971,5,20)

    # Prologue team time trial
    builder.prologue_team_time_trial(italy.lecce(), italy.brindisi(), 62.2)
    # Stage 1
    builder.road_stage(italy.brindisi(), italy.bari(), 175.0)

    # Stage 2
    builder.road_stage(italy.bari(), italy.potenza(), 260.0)

    # Stage 3
    builder.road_stage(italy.potenza(), italy.benevento(), 177.0)

    # Stage 4
    builder.road_stage(italy.benevento(), italy.pescasseroli(), 203.0)

    # Stage 5
    builder.road_stage(italy.pescasseroli(), italy.gran_sasso_d_italia(), 198.0)

    # Stage 6
    builder.road_stage(italy.l_aquila(), italy.orvieto(), 163.0)

    # Stage 7
    builder.road_stage(italy.orvieto(), italy.san_vincenzo(), 220.0)

    # Stage 8
    builder.road_stage(italy.san_vincenzo(), italy.casciana_terme(), 203.0)

    # Stage 9
    builder.road_stage(italy.casciana_terme(), italy.forte_dei_marmi(), 141.0)

    # Stage 10
    builder.criterium(italy.forte_dei_marmi(), 141.0)

    # Stage 11
    builder.road_stage(italy.sestola(), italy.mantua(), 199.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.individual_time_trial(italy.desenzano_del_garda(), italy.serniga_di_salo(), 28.0)

    # Stage 13
    builder.road_stage(italy.salo(), italy.sottomarina_di_chioggia(), 218.0)

    # Stage 14
    builder.road_stage(italy.chioggia(), italy.bibione(), 170.0)

    # Stage 15
    builder.road_stage(italy.bibione(), yugoslavia.ljubljana(), 201.0)

    # Stage 16
    builder.road_stage(yugoslavia.ljubljana(), italy.tarvisio(), 100.0)

    # Stage 17
    builder.road_stage(italy.tarvisio(), austria.grossglockner(), 206.0)

    # Stage 18
    builder.road_stage(austria.lienz(), italy.falcade(), 195.0)

    # Stage 19
    builder.road_stage(italy.falcade(), italy.ponte_di_legno(), 182.0)

    # Stages 20a & 20b
    builder.enable_split_stages()
    builder.road_stage(italy.ponte_di_legno(), italy.lainate(), 185.0)
    builder.individual_time_trial(italy.lainate(), italy.milan(), 20.0)
    builder.disable_split_stages()

    return builder.build()

def giro1972():

    builder = TourOfItalyBuilder(1972,5,21)

    # Stage 1
    builder.road_stage(italy.venice(), italy.ravenna(), 196.0)

    # Stage 2
    builder.road_stage(italy.ravenna(), italy.fermo(), 212.0)

    # Stage 3
    builder.road_stage(italy.porto_san_giorgio(), italy.francavilla_al_mare(), 205.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.road_stage(italy.francavilla_al_mare(), italy.blockhaus(), 48.0)
    builder.road_stage(italy.blockhaus(), italy.foggia(), 210.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(italy.foggia(), italy.montesano_sulla_marcellana(), 238.0)

    # Stage 6
    builder.road_stage(italy.montesano_sulla_marcellana(), italy.cosenza(), 190.0)

    # Stage 7
    builder.road_stage(italy.cosenza(), italy.catanzaro(), 151.0)

    # Stage 8
    builder.road_stage(italy.catanzaro(), italy.reggio_calabria(), 160.0)

    # Stage 9
    builder.criterium(italy.messina(), 110.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.rome(), italy.monte_argentario(), 166.0)

    # Stage 11
    builder.road_stage(italy.monte_argentario(), italy.forte_dei_marmi(), 242.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(italy.forte_dei_marmi(), 20.0)
    builder.out_and_back_individual_time_trial(italy.forte_dei_marmi(), 20.0)
    builder.disable_split_stages()

    # Stage 13
    builder.road_stage(italy.forte_dei_marmi(), italy.savona(), 200.0)

    # Stage 14
    builder.mountain_stage(italy.savona())
    builder.summit_finish(mountains.alps.monte_jafferau(), ColCategory.C1, 256.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.criterium(italy.parabiago(), 168.0)

    # Stage 16
    builder.road_stage(italy.parabiago(), italy.livigno(), 256.0)

    # Stage 17
    builder.mountain_stage(italy.livigno())
    builder.summit_finish(mountains.alps.passo_dello_stelvio(), ColCategory.C1, 88.0)

    # Stage 18
    builder.road_stage(italy.sulden(), italy.asiago(), 223.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(italy.asiago(), italy.arco(), 163.0)
    builder.out_and_back_individual_time_trial(italy.arco(), 18.0)
    builder.disable_split_stages()

    # Stage 20
    builder.road_stage(italy.arco(), italy.milan(), 185.0)

    return builder.build()

def giro1973():

    builder = TourOfItalyBuilder(1973,5,18)

    # Prologue
    builder.prologue_two_man_team_time_trial(belgium.verviers(), 5.2)

    # Stage 1
    builder.road_stage(belgium.verviers(), west_germany.cologne(), 137.0)

    # Stage 2
    builder.road_stage(west_germany.cologne(), luxembourg.luxembourg_city(), 227.0)

    # Stage 3
    builder.road_stage(luxembourg.luxembourg_city(), france.strasbourg(), 239.0)

    # Stage 4
    builder.road_stage(switzerland.geneva(), italy.aosta(), 163.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.saint_vincent(), italy.milan(), 173.0)

    # Stage 6
    builder.road_stage(italy.milan(), italy.iseo(), 144.0)

    # Stage 7
    builder.road_stage(italy.iseo(), italy.lido_delle_nazioni(), 248.0)

    # Stage 8
    builder.road_stage(italy.lido_delle_nazioni(), italy.monte_carpegna(), 156.0)

    # Stage 9
    builder.road_stage(italy.carpegna(), italy.alba_adriatica(), 243.0)

    # Stage 10
    builder.road_stage(italy.alba_adriatica(), italy.lanciano(), 174.0)

    # Stage 11
    builder.road_stage(italy.lanciano(), italy.benevento(), 230.0)

    # Stage 12
    builder.road_stage(italy.benevento(), italy.fiuggi(), 236.0)

    # Stage 13
    builder.road_stage(italy.fiuggi(), italy.bolsena(), 215.0)

    # Stage 14
    builder.road_stage(italy.bolsena(), italy.florence(), 202.0)

    # Stage 15
    builder.road_stage(italy.florence(), italy.forte_dei_marmi(), 150.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.out_and_back_individual_time_trial(italy.forte_dei_marmi(), 37.0)

    # Stage 17
    builder.road_stage(italy.forte_dei_marmi(), italy.verona(), 244.0)

    # Stage 18
    builder.road_stage(italy.verona(), italy.andalo(), 173.0)

    # Stage 19
    builder.road_stage(italy.andalo(), italy.auronzo_di_cadore(), 208.0)

    # Stage 20
    builder.road_stage(italy.auronzo_di_cadore(), italy.trieste(), 197.0)

    return builder.build()

def giro1974():

    builder = TourOfItalyBuilder(1974,5,16)

    # Stage 1
    builder.road_stage(vatican_city.vatican_city(), italy.formia(), 164.0)

    # Stage 2
    builder.road_stage(italy.formia(), italy.pompeii(), 121.0)

    # Stage 3
    builder.road_stage(italy.pompeii(), italy.sorrento(), 137.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.sorrento(), italy.sapri(), 208.0)

    # Stage 5
    builder.road_stage(italy.sapri(), italy.taranto(), 215.0)

    # Stage 6
    builder.road_stage(italy.taranto(), italy.foggia(), 206.0)

    # Stage 7
    builder.road_stage(italy.foggia(), italy.chieti(), 257.0)

    # Stage 8
    builder.road_stage(italy.chieti(), italy.macerata(), 150.0)

    # Stage 9
    builder.road_stage(italy.macerata(), italy.carpegna(), 191.0)

    # Stage 10
    builder.road_stage(italy.macerata(), italy.carpegna(), 191.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(italy.modena(), italy.il_ciocco(), 153.0)
    builder.road_stage(italy.il_ciocco(), italy.forte_dei_marmi(), 62.0)
    builder.disable_split_stages()

    # Stage 12
    builder.out_and_back_individual_time_trial(italy.forte_dei_marmi(), 40.0)

    # Stage 13
    builder.road_stage(italy.forte_dei_marmi(), italy.pietra_ligure(), 231.0)

    # Stage 14
    builder.road_stage(italy.pietra_ligure(), italy.san_remo(), 189.0)

    # Stage 15
    builder.road_stage(italy.san_remo(), italy.valenza(), 206.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.valenza(), italy.monte_generoso(), 158.0)

    # Stage 17
    builder.road_stage(italy.como(), italy.iseo(), 158.0)

    # Stage 18
    builder.road_stage(italy.iseo(), italy.sella_valsugana(), 190.0)

    # Stage 19
    builder.road_stage(italy.borgo_valsugana(), italy.pordenone(), 146.0)

    # Stage 20
    builder.road_stage(italy.pordenone(), italy.tre_cime_di_lavaredo(), 163.0)

    # Stage 21
    builder.road_stage(italy.misurina(), italy.bassano_del_grappa(), 194.0)

    # Stage 22
    builder.road_stage(italy.bassano_del_grappa(), italy.milan(), 257.0)

    return builder.build()

def giro1975():

    builder = TourOfItalyBuilder(1975,5,17)

    # Stage 1
    builder.road_stage(italy.milan(), italy.fiorano_modenese(), 177.0)

    # Stage 2
    builder.road_stage(italy.modena(), italy.ancona(), 249.0)

    # Stage 3
    builder.road_stage(italy.ancona(), italy.prati_di_tivo(), 175.0)

    # Stage 4
    builder.road_stage(italy.teramo(), italy.campobasso(), 258.0)

    # Stage 5
    builder.road_stage(italy.campobasso(), italy.bari(), 224.0)

    # Stage 6
    builder.road_stage(italy.bari(), italy.castrovillari(), 213.0)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.road_stage(italy.castrovillari(), italy.padula(), 123.0)
    builder.road_stage(italy.padula(), italy.potenza(), 80.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(italy.potenza(), italy.sorrento(), 220.0)

    # Stage 9
    builder.road_stage(italy.sorrento(), italy.frosinone(), 222.0)

    # Stage 10
    builder.road_stage(italy.frosinone(), italy.tivoli(), 176.0)

    # Stage 11
    builder.road_stage(italy.rome(), italy.orvieto(), 158.0)

    # Stage 12
    builder.road_stage(italy.chianciano_terme(), italy.forte_dei_marmi(), 232.0)

    # Stage 13
    builder.out_and_back_individual_time_trial(italy.forte_dei_marmi(), 38.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.out_and_back_individual_time_trial(italy.il_ciocco(), 13.0)

    # Stage 15
    builder.road_stage(italy.il_ciocco(), italy.arenzano(), 203.0)

    # Stage 16
    builder.road_stage(italy.arenzano(), italy.orta_san_giulio(), 193.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(italy.orta_san_giulio(), italy.pontoglio(), 167.0)
    builder.road_stage(italy.pontoglio(), italy.monte_maddalena(), 46.0)
    builder.disable_split_stages()

    # Stage 18
    builder.road_stage(italy.brescia(), italy.baselga_di_pine(), 223.0)

    # Stage 19
    builder.road_stage(italy.baselga_di_pine(), italy.pordenone(), 175.0)

    # Stage 20
    builder.road_stage(italy.pordenone(), italy.alleghe(), 197.0)

    # Stage 21
    builder.mountain_stage(italy.alleghe())
    builder.summit_finish(mountains.alps.passo_dello_stelvio(), ColCategory.C1, 186.0)

    return builder.build()

def giro1976():

    builder = TourOfItalyBuilder(1976,5,21)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.criterium(italy.catania(), 64.0)
    builder.road_stage(italy.catania(), italy.siracusa(), 78.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(italy.siracusa(), italy.caltanissetta(), 210.0)

    # Stage 3
    builder.road_stage(italy.caltanissetta(), italy.palermo(), 163.0)

    # Stage 4
    builder.road_stage(italy.cefalu(), italy.messina(), 192.0)

    # Stage 5
    builder.road_stage(italy.reggio_calabria(), italy.cosenza(), 220.0)

    # Stage 6
    builder.road_stage(italy.cosenza(), italy.matera(), 207.0)

    # Stage 7
    builder.out_and_back_individual_time_trial(italy.ostuni(), 37.0)

    # Stage 8
    builder.road_stage(italy.selva_di_fasano(), italy.lago_laceno(), 256.0)

    # Stage 9
    builder.road_stage(italy.bagnoli_irpino(), italy.roccaraso(), 204.0)

    # Stage 10
    builder.road_stage(italy.roccaraso(), italy.terni(), 203.0)

    # Stage 11
    builder.road_stage(italy.terni(), italy.gabicce_mare(), 222.0)

    # Stage 12
    builder.road_stage(italy.gabicce_mare(), italy.porretta_terme(), 215.0)

    # Stage 13
    builder.road_stage(italy.porretta_terme(), italy.il_ciocco(), 146.0)

    # Stage 14
    builder.road_stage(italy.il_ciocco(), italy.varazze(), 227.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.varazze(), italy.ozegna(), 216.0)

    # Stage 16
    builder.road_stage(italy.castellamonte(), italy.arosio(), 258.0)

    # Stage 17
    builder.road_stage(italy.arosio(), italy.verona(), 196.0)

    # Stage 18
    builder.road_stage(italy.verona(), italy.longarone(), 174.0)

    # Stage 19
    builder.road_stage(italy.longarone(), italy.vajolet_towers(), 132.0)

    # Stage 20
    builder.road_stage(italy.vigo_di_fassa(), italy.terme_di_comano(), 170.0)

    # Stage 21
    builder.road_stage(italy.terme_di_comano(), italy.bergamo(), 238.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(italy.arcore(), 28.0)
    builder.criterium(italy.milan(), 106.0)
    builder.disable_split_stages()

    return builder.build()

def giro1977():

    builder = TourOfItalyBuilder(1977,5,20)

    # Prologue
    builder.prologue(italy.bacoli(), italy.monte_di_procida(), 7.0)

    # Stage 1
    builder.road_stage(italy.lago_miseno(), italy.avellino(), 159.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(italy.avellino(), italy.foggia(), 118.0)
    builder.criterium(italy.foggia(), 65.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(italy.foggia(), italy.isernia(), 166.0)

    # Stage 4
    builder.road_stage(italy.isernia(), italy.pescara(), 228.0)

    # Stage 5
    builder.road_stage(italy.pescara(), italy.monteluco_di_spoleto(), 215.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(italy.spoleto(), italy.gabicce_mare(), 185.0)
    builder.criterium(italy.gabicce_mare(), 70.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(italy.gabicce_mare(), italy.forli(), 163.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(italy.forli(), italy.circuito_del_mugello(), 103.0)
    builder.criterium(italy.circuito_del_mugello(), 79.0)
    builder.disable_split_stages()

    # Stage 9
    builder.individual_time_trial(italy.lucca(), italy.pisa(), 25.0)

    # Stage 10
    builder.road_stage(italy.pisa(), italy.salsomaggiore_terme(), 205.0)

    # Stage 11
    builder.road_stage(italy.salsomaggiore_terme(), italy.santa_margherita_ligure(), 198.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.santa_margherita_ligure(), italy.san_giacomo_di_roburent(), 160.0)

    # Stage 13
    builder.road_stage(italy.mondovi(), italy.varzi(), 192.0)

    # Stage 14
    builder.road_stage(italy.voghera(), italy.vicenza(), 247.0)

    # Stage 15
    builder.road_stage(italy.vicenza(), italy.trieste(), 223.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(italy.trieste(), italy.gemona_del_friuli(), 107.0)
    builder.road_stage(italy.gemona_del_friuli(), italy.conegliano(), 116.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(italy.conegliano(), italy.cortina_d_ampezzo(), 220.0)

    # Stage 18
    builder.road_stage(italy.cortina_d_ampezzo(), italy.pinzolo(), 223.0)

    # Stage 19
    builder.road_stage(italy.pinzolo(), italy.san_pellegrino_terme(), 205.0)

    # Stage 20
    builder.road_stage(italy.san_pellegrino_terme(), italy.varese(), 138.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.binago(), 29.0)

    # Stage 22
    builder.criterium(italy.milan(), 122.0)

    return builder.build()

def giro1978():

    builder = TourOfItalyBuilder(1978,5,7)

    # Prologue
    builder.out_and_back_prologue(italy.saint_vincent(), 2.0)
    # Stage 1
    builder.road_stage(italy.saint_vincent(), italy.novi_ligure(), 175.0)

    # Stage 2
    builder.road_stage(italy.novi_ligure(), italy.la_spezia(), 195.0)

    # Stage 3
    builder.road_stage(italy.la_spezia(), italy.cascina(), 183.0)

    # Stage 4
    builder.individual_time_trial(italy.larciano(), italy.pistoia(), 25.0)

    # Stage 5
    builder.road_stage(italy.prato(), italy.cattolica(), 200.0)

    # Stage 6
    builder.road_stage(italy.cattolica(), italy.silvi_marina(), 218.0)

    # Stage 7
    builder.road_stage(italy.silvi_marina(), italy.benevento(), 242.0)

    # Stage 8
    builder.road_stage(italy.benevento(), italy.ravello(), 175.0)

    # Stage 9
    builder.road_stage(italy.amalfi(), italy.latina(), 248.0)

    # Stage 10
    builder.road_stage(italy.latina(), italy.lago_di_piediluco(), 220.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(italy.terni(), italy.assisi(), 74.0)
    builder.road_stage(italy.assisi(), italy.siena(), 145.0)
    builder.disable_split_stages()

    # Stage 12
    builder.road_stage(italy.poggibonsi(), italy.monte_trebbio(), 204.0)

    # Stage 13
    builder.road_stage(italy.modigiliana(), italy.padua(), 183.0)

    # Stage 14
    builder.out_and_back_individual_time_trial(italy.venice(), 12.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.treviso(), italy.canazei(), 234.0)

    # Stage 16
    builder.individual_time_trial(italy.mazzin(), italy.cavalese(), 48.0)

    # Stage 17
    builder.road_stage(italy.cavalese(), italy.monte_bondone(), 205.0)

    # Stage 18
    builder.road_stage(italy.mezzolombardo(), italy.sarezzo(), 245.0)

    # Stage 19
    builder.road_stage(italy.brescia(), italy.inverigo(), 175.0)

    # Stage 20
    builder.road_stage(italy.inverigo(), italy.milan(), 220.0)

    return builder.build()

def giro1979():

    builder = TourOfItalyBuilder(1979,5,17)

    # Prologue
    builder.out_and_back_prologue(italy.florence(), 2.0)
    # Stage 1
    builder.road_stage(italy.florence(), italy.perugia(), 156.0)

    # Stage 2
    builder.road_stage(italy.perugia(), italy.castel_gandolfo(), 204.0)

    # Stage 3
    builder.individual_time_trial(italy.caserta(), italy.naples(), 31.0)

    # Stage 4
    builder.road_stage(italy.caserta(), italy.potenza(), 210.0)

    # Stage 5
    builder.road_stage(italy.potenza(), italy.vieste(), 223.0)

    # Stage 6
    builder.road_stage(italy.vieste(), italy.chieti(), 260.0)

    # Stage 7
    builder.road_stage(italy.chieti(), italy.pesaro(), 252.0)

    # Stage 8
    builder.individual_time_trial(italy.rimini(), san_marino.san_marino(), 28.0)

    # Stage 9
    builder.road_stage(san_marino.san_marino(), italy.pistoia(), 248.0)

    # Stage 10
    builder.individual_time_trial(italy.lerici(), italy.portovenere(), 25.0)

    # Stage 11
    builder.road_stage(italy.la_spezia(), italy.voghera(), 212.0)

    # Stage 12
    builder.road_stage(italy.alessandria(), italy.saint_vincent(), 204.0)

    # Stage 13
    builder.road_stage(italy.aosta(), italy.meda(), 229.0)

    # Stage 14
    builder.road_stage(italy.meda(), italy.bosco_chiesanuova(), 212.0)

    # Stage 15
    builder.road_stage(italy.verona(), italy.treviso(), 121.0)

    # Stage 16
    builder.road_stage(italy.treviso(), italy.pieve_di_cadore(), 195.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.pieve_di_cadore(), italy.trento(), 194.0)

    # Stage 18
    builder.road_stage(italy.trento(), italy.barzio(), 245.0)

    # Stage 19
    builder.individual_time_trial(italy.cesano_maderno(), italy.milan(), 44.0)

    return builder.build()

def giro1980():

    builder = TourOfItalyBuilder(1980,5,15)

    # Prologue
    builder.out_and_back_prologue(italy.genoa(), 7.0)
    # Stage 1
    builder.road_stage(italy.genoa(), italy.imperia(), 123.0)

    # Stage 2
    builder.road_stage(italy.imperia(), italy.turin(), 179.0)

    # Stage 3
    builder.road_stage(italy.turin(), italy.parma(), 243.0)

    # Stage 4
    builder.road_stage(italy.parma(), italy.marina_di_pisa(), 193.0)

    # Stage 5
    builder.individual_time_trial(italy.pontedera(), italy.pisa(), 36.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.rio_marina(), italy.portoferraio(), 126.0)

    # Stage 7
    builder.road_stage(italy.castiglione_della_pescaia(), italy.orvieto(), 200.0)

    # Stage 8
    builder.road_stage(italy.orvieto(), italy.fiuggi(), 216.0)

    # Stage 9
    builder.road_stage(italy.fiuggi(), italy.sorrento(), 247.0)

    # Stage 10
    builder.road_stage(italy.sorrento(), italy.palinuro(), 177.0)

    # Stage 11
    builder.road_stage(italy.palinuro(), italy.campotenese(), 145.0)

    # Stage 12
    builder.road_stage(italy.villapiana_lido(), italy.campi_salentina(), 203.0)

    # Stage 13
    builder.road_stage(italy.campi_salentina(), italy.barletta(), 220.0)

    # Stage 14
    builder.road_stage(italy.foggia(), italy.roccaraso(), 186.0)

    # Stage 15
    builder.road_stage(italy.roccaraso(), italy.termamo(), 194.0)

    # Stage 16
    builder.road_stage(italy.giulianova(), italy.gatteo_a_mare(), 229.0)

    # Stage 17
    builder.road_stage(italy.gatteo_a_mare(), italy.sirmione(), 237.0)

    # Stage 18
    builder.road_stage(italy.sirmione(), italy.zoldo_alto(), 239.0)

    # Stage 19
    builder.road_stage(italy.longarone(), italy.cles(), 241.0)

    # Stage 20
    builder.road_stage(italy.cles(), italy.sondrio(), 221.0)

    # Stage 21
    builder.individual_time_trial(italy.saronno(), italy.turbigo(), 50.0)

    # Stage 22
    builder.criterium(italy.milan(), 114.0)

    return builder.build()

def giro1981():

    builder = TourOfItalyBuilder(1981,5,13)

    # Prologue
    builder.out_and_back_prologue(italy.trieste(), 6.6)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(italy.trieste(), italy.bibione(), 100.0)
    builder.team_time_trial(italy.lignano_sabbiadoro(), italy.bibione(), 15.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(italy.bibione(), italy.ferrara(), 211.0)

    # Stage 3
    builder.road_stage(italy.bologna(), italy.recanati(), 255.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.recanati(), italy.lanciano(), 214.0)

    # Stage 5
    builder.road_stage(italy.marina_di_san_vito(), italy.rodi_garganico(), 180.0)

    # Stage 6
    builder.road_stage(italy.rodi_garganico(), italy.bari(), 225.0)

    # Stage 7
    builder.road_stage(italy.bari(), italy.potenza(), 143.0)

    # Stage 8
    builder.road_stage(italy.sala_consilina(), italy.cosenza(), 202.0)

    # Stage 9
    builder.road_stage(italy.cosenza(), italy.reggio_calabria(), 231.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.rome(), italy.cascia(), 166.0)

    # Stage 11
    builder.road_stage(italy.cascia(), italy.arezzo(), 199.0)

    # Stage 12
    builder.road_stage(italy.arezzo(), italy.livorno(), 224.0)

    # Stage 13
    builder.individual_time_trial(italy.empoli(), italy.montecatini_terme(), 35.0)

    # Stage 14
    builder.road_stage(italy.montecatini_terme(), italy.salsomaggiore_terme(), 224.0)

    # Stage 15
    builder.road_stage(italy.salsomaggiore_terme(), italy.pavia(), 198.0)

    # Stage 16
    builder.road_stage(italy.milan(), italy.mantua(), 178.0)

    # Stage 17
    builder.road_stage(italy.mantua(), italy.borno(), 215.0)

    # Stage 18
    builder.road_stage(italy.borno(), italy.dimaro(), 127.0)

    # Transfer day
    builder.rest_day()

    # Stage 19
    builder.road_stage(italy.dimaro(), italy.san_vigillo_di_marebbe(), 208.0)

    # Stage 20
    builder.road_stage(italy.san_vigillo_di_marebbe(), italy.tre_cime_di_lavaredo(), 100.0)

    # Stage 21
    builder.road_stage(italy.auronzo_di_cadore(), italy.arzignano(), 197.0)

    # Stage 22
    builder.individual_time_trial(italy.soave(), italy.verona(), 42.0)

    return builder.build()

def giro1982():

    builder = TourOfItalyBuilder(1982,5,13)

    # Prologue
    builder.out_and_back_prologue(italy.milan(), 16.0)
    # Stage 1
    builder.road_stage(italy.parma(), italy.viareggio(), 174.0)

    # Stage 2
    builder.road_stage(italy.viareggio(), italy.cortona(), 233.0)

    # Stage 3
    builder.individual_time_trial(italy.perugia(), italy.assisi(), 37.0)

    # Stage 4
    builder.road_stage(italy.assisi(), italy.rome(), 169.0)

    # Stage 5
    builder.road_stage(italy.rome(), italy.caserta(), 213.0)

    # Stage 6
    builder.road_stage(italy.caserta(), italy.castellammare_di_stabia(), 130.0)

    # Stage 7
    builder.road_stage(italy.castellammare_di_stabia(), italy.diamante(), 226.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(italy.taormina(), italy.agrigento(), 248.0)

    # Stage 9
    builder.road_stage(italy.agrigento(), italy.palermo(), 151.0)

    # Stage 10
    builder.road_stage(italy.cefalu(), italy.messina(), 197.0)

    # Stage 11
    builder.road_stage(italy.palmi(), italy.camigliatello_silano(), 229.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.cava_de_tirreni(), italy.campitello_matese(), 171.0)

    # Stage 13
    builder.road_stage(italy.campitello_matese(), italy.pescara(), 164.0)

    # Stage 14
    builder.road_stage(italy.pescara(), italy.urbino(), 248.0)

    # Stage 15
    builder.road_stage(italy.urbino(), italy.comacchio(), 190.0)

    # Stage 16
    builder.mountain_stage(italy.comacchio())
    builder.summit_finish(mountains.dolomites.san_martino_di_castrozza(), ColCategory.C2, 243.0)

    # Stage 17
    builder.road_stage(italy.fiera_di_primiero(), italy.boario_terme(), 235.0)

    # Stage 18
    builder.road_stage(italy.piancogno(), italy.montecampione(), 85.0)

    # Stage 19
    builder.road_stage(italy.boario_terme(), italy.vigevano(), 162.0)

    # Stage 20
    builder.road_stage(italy.vigevano(), italy.cuneo(), 177.0)

    # Stage 21
    builder.road_stage(italy.cuneo(), italy.pinerolo(), 254.0)

    # Stage 22
    builder.individual_time_trial(italy.pinerolo(), italy.turin(), 42.5)

    return builder.build()

def giro1983():

    builder = TourOfItalyBuilder(1983,5,12)

    # Prologue
    builder.out_and_back_prologue(italy.brescia(), 8.0)
    # Stage 1
    builder.team_time_trial(italy.brescia(), italy.mantua(), 70.0)

    # Stage 2
    builder.road_stage(italy.mantua(), italy.comacchio(), 192.0)

    # Stage 3
    builder.road_stage(italy.comacchio(), italy.fano(), 148.0)

    # Stage 4
    builder.road_stage(italy.pesaro(), italy.todi(), 187.0)

    # Stage 5
    builder.road_stage(italy.terni(), italy.vasto(), 269.0)

    # Stage 6
    builder.road_stage(italy.vasto(), italy.campitello_matese(), 145.0)

    # Stage 7
    builder.road_stage(italy.campitello_matese(), italy.salerno(), 216.0)

    # Stage 8
    builder.road_stage(italy.salerno(), italy.terracina(), 212.0)

    # Stage 9
    builder.road_stage(italy.terracina(), italy.montefiascone(), 225.0)

    # Stage 10
    builder.road_stage(italy.montefiascone(), italy.bibbiena(), 232.0)

    # Stage 11
    builder.road_stage(italy.bibbiena(), italy.pietrasanta(), 202.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.pietrasanta(), italy.reggio_emilia(), 180.0)

    # Stage 13
    builder.individual_time_trial(italy.reggio_emilia(), italy.parma(), 38.0)

    # Stage 14
    builder.road_stage(italy.parma(), italy.savona(), 243.0)

    # Stage 15
    builder.road_stage(italy.savona(), italy.orta_san_giulio(), 219.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(italy.orta_san_giulio(), italy.milan(), 110.0)
    builder.road_stage(italy.milan(), italy.bergamo(), 100.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(italy.bergamo(), italy.colli_di_san_fermo(), 91.0)

    # Stage 18
    builder.road_stage(italy.sarnico(), italy.vicenza(), 178.0)

    # Transfer day
    builder.rest_day()

    # Stage 19
    builder.road_stage(italy.vicenza(), italy.selva_di_val_gardena(), 224.0)

    # Stage 20
    builder.road_stage(italy.selva_di_val_gardena(), italy.arabba(), 169.0)

    # Stage 21
    builder.road_stage(italy.arabba(), italy.gorizia(), 232.0)

    # Stage 22
    builder.individual_time_trial(italy.gorizia(), italy.udine(), 40.0)

    return builder.build()

def giro1984():

    builder = TourOfItalyBuilder(1984,5,17)

    # Prologue
    builder.out_and_back_prologue(italy.lucca(), 5.0)
    # Stage 1
    builder.team_time_trial(italy.lucca(), italy.marina_di_pietrasanta(), 55.0)

    # Stage 2
    builder.road_stage(italy.marina_di_pietrasanta(), italy.firenze(), 127.0)

    # Stage 3
    builder.road_stage(italy.bologna(), italy.madonna_di_san_luca(), 110.0)

    # Stage 4
    builder.road_stage(italy.bologna(), italy.numana(), 238.0)

    # Stage 5
    builder.road_stage(italy.numana(), italy.blockhaus(), 194.0)

    # Stage 6
    builder.road_stage(italy.chieti(), italy.foggia(), 193.0)

    # Stage 7
    builder.road_stage(italy.foggia(), italy.marconia_di_pisticci(), 226.0)

    # Stage 8
    builder.road_stage(italy.policoro(), italy.agropoli(), 228.0)

    # Stage 9
    builder.road_stage(italy.agropoli(), italy.cava_de_tirreni(), 104.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.cava_de_tirreni(), italy.isernia(), 209.0)

    # Stage 11
    builder.road_stage(italy.isernia(), italy.rieti(), 243.0)

    # Stage 12
    builder.road_stage(italy.rieti(), italy.citta_di_castello(), 175.0)

    # Stage 13
    builder.road_stage(italy.citta_di_castello(), italy.lerici(), 269.0)

    # Stage 14
    builder.road_stage(italy.lerici(), italy.alessandria(), 204.0)

    # Stage 15
    builder.individual_time_trial(italy.certosa_di_pavia(), italy.milan(), 38.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.alessandria(), italy.bardonecchia(), 198.0)

    # Stage 17
    builder.road_stage(italy.bardonecchia(), italy.lecco(), 249.0)

    # Stage 18
    builder.road_stage(italy.lecco(), italy.merano(), 252.0)

    # Stage 19
    builder.road_stage(italy.merano(), italy.selva_di_val_gardena(), 74.0)

    # Stage 20
    builder.road_stage(italy.selva_di_val_gardena(), italy.arabba(), 169.0)

    # Stage 21
    builder.road_stage(italy.arabba(), italy.treviso(), 208.0)

    # Stage 22
    builder.individual_time_trial(italy.soave(), italy.verona(), 42.0)

    return builder.build()

def giro1985():

    builder = TourOfItalyBuilder(1985,5,16)

    # Prologue
    builder.out_and_back_prologue(italy.verona(), 6.6)
    # Stage 1
    builder.road_stage(italy.verona(), italy.busto_arsizio(), 218.0)

    # Stage 2
    builder.team_time_trial(italy.busto_arsizio(), italy.milan(), 38.0)

    # Stage 3
    builder.road_stage(italy.milan(), italy.pinzolo(), 190.0)

    # Stage 4
    builder.road_stage(italy.pinzolo(), italy.selva_di_val_gardena(), 237.0)

    # Stage 5
    builder.road_stage(italy.selva_di_val_gardena(), italy.vittorio_veneto(), 225.0)

    # Stage 6
    builder.road_stage(italy.vittorio_veneto(), italy.cervia(), 237.0)

    # Stage 7
    builder.road_stage(italy.cervia(), italy.jesi(), 185.0)

    # Transfer day
    builder.rest_day()

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.criterium(italy.foggia(), 45.0)
    builder.road_stage(italy.foggia(), italy.matera(), 167.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(italy.matera(), italy.crotone(), 237.0)

    # Stage 10
    builder.road_stage(italy.crotone(), italy.paola(), 203.0)

    # Stage 11
    builder.road_stage(italy.paola(), italy.salerno(), 240.0)

    # Stage 12
    builder.individual_time_trial(italy.capua(), italy.maddaloni(), 38.0)

    # Stage 13
    builder.road_stage(italy.maddaloni(), italy.frosinone(), 154.0)

    # Stage 14
    builder.road_stage(italy.frosinone(), italy.gran_sasso_d_italia(), 195.0)

    # Stage 15
    builder.road_stage(italy.l_aquila(), italy.perugia(), 208.0)

    # Stage 16
    builder.road_stage(italy.perugia(), italy.cecina(), 217.0)

    # Stage 17
    builder.road_stage(italy.cecina(), italy.modena(), 248.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(italy.monza(), italy.domodossola(), 128.0)

    # Stage 19
    builder.road_stage(italy.domodossola(), italy.saint_vincent(), 247.0)

    # Stage 20
    builder.road_stage(italy.saint_vincent(), italy.valnontey_di_cogne(), 58.0)

    # Stage 21
    builder.road_stage(italy.saint_vincent(), italy.genoa(), 229.0)

    # Stage 22
    builder.individual_time_trial(italy.lido_di_camaiore(), italy.lucca(), 48.0)

    return builder.build()

def giro1986():

    builder = TourOfItalyBuilder(1986,5,12)

    # Prologue & Stage 1
    builder.enable_morning_stage()
    builder.out_and_back_prologue(italy.palermo(), 1.0)
    builder.road_stage(italy.palermo(), italy.sciacca(), 140.0)

    # Stage 2
    builder.road_stage(italy.sciacca(), italy.catania(), 259.0)

    # Stage 3
    builder.team_time_trial(italy.catania(), italy.taormina(), 50.0)

    # Stage 4
    builder.road_stage(italy.villa_san_giovanni(), italy.nicotera(), 115.0)

    # Stage 5
    builder.road_stage(italy.nicotera(), italy.cosenza(), 194.0)

    # Stage 6
    builder.road_stage(italy.cosenza(), italy.potenza(), 251.0)

    # Stage 7
    builder.road_stage(italy.potenza(), italy.baia_domizia(), 257.0)

    # Stage 8
    builder.road_stage(italy.cellole(), italy.avezzano(), 160.0)

    # Stage 9
    builder.road_stage(italy.avezzano(), italy.rieti(), 172.0)

    # Stage 10
    builder.road_stage(italy.rieti(), italy.pesaro(), 238.0)

    # Stage 11
    builder.road_stage(italy.pesaro(), italy.castiglione_del_lago(), 207.0)

    # Stage 12
    builder.individual_time_trial(italy.sinalunga(), italy.siena(), 46.0)

    # Stage 13
    builder.road_stage(italy.siena(), italy.sarzana(), 175.0)

    # Stage 14
    builder.road_stage(italy.savona(), italy.sauze_d_oulx(), 236.0)

    # Stage 15
    builder.road_stage(italy.sauze_d_oulx(), italy.erba(), 260.0)

    # Stage 16
    builder.road_stage(italy.erba(), italy.foppolo(), 143.0)

    # Stage 17
    builder.road_stage(italy.foppolo(), italy.piacenza(), 186.0)

    # Stage 18
    builder.individual_time_trial(italy.piacenza(), italy.cremona(), 36.0)

    # Stage 19
    builder.road_stage(italy.cremona(), italy.peio(), 211.0)

    # Stage 20
    builder.road_stage(italy.peio(), italy.bassano_del_grappa(), 179.0)

    # Stage 21
    builder.road_stage(italy.bassano_del_grappa(), italy.bolzano(), 234.0)

    # Stage 22
    builder.criterium(italy.merano(), 108.6)

    return builder.build()

def giro1987():

    builder = TourOfItalyBuilder(1987,5,21)

    # Prologue
    builder.out_and_back_prologue(italy.san_remo(), 4.0)

    # Stage 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(italy.san_remo(), italy.san_romolo(), 31.0)
    builder.individual_time_trial(italy.poggio_di_san_remo(), italy.san_remo(), 8.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(italy.imperia(), italy.borgo_val_di_taro(), 242.0)

    # Stage 3
    builder.team_time_trial(italy.lerici(), italy.camaiore(), 43.0)

    # Stage 4
    builder.road_stage(italy.camaiore(), italy.montalcino(), 203.0)

    # Stage 5
    builder.road_stage(italy.montalcino(), italy.terni(), 208.0)

    # Stage 6
    builder.road_stage(italy.terni(), italy.monte_terminillo(), 134.0)

    # Stage 7
    builder.road_stage(italy.rieti(), italy.roccaraso(), 205.0)

    # Stage 8
    builder.road_stage(italy.roccaraso(), italy.san_giorgio_del_sannio(), 168.0)

    # Stage 9
    builder.road_stage(italy.san_giorgio_del_sannio(), italy.bari(), 257.0)

    # Stage 10
    builder.road_stage(italy.bari(), italy.termoli(), 210.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.guilianova(), italy.osimo(), 245.0)

    # Stage 12
    builder.road_stage(italy.osimo(), italy.bellaria(), 197.0)

    # Stage 13
    builder.individual_time_trial(italy.rimini(), san_marino.san_marino(), 46.0)

    # Stage 14
    builder.road_stage(san_marino.san_marino(), italy.lido_di_jesolo(), 260.0)

    # Stage 15
    builder.road_stage(italy.lido_di_jesolo(), italy.sappada(), 224.0)

    # Stage 16
    builder.road_stage(italy.sappada(), italy.canazei(), 211.0)

    # Stage 17
    builder.road_stage(italy.canazei(), italy.riva_del_garda(), 206.0)

    # Stage 18
    builder.road_stage(italy.riva_del_garda(), italy.trescore_balneario(), 213.0)

    # Stage 19
    builder.road_stage(italy.trescore_balneario(), italy.madesimo(), 160.0)

    # Stage 20
    builder.road_stage(italy.madesimo(), italy.como(), 156.0)

    # Stage 21
    builder.road_stage(italy.como(), italy.pila(), 252.0)

    # Stage 22
    builder.individual_time_trial(italy.aosta(), italy.saint_vincent(), 32.0)

    return builder.build()

def giro1988():

    builder = TourOfItalyBuilder(1988,5,23)

    # Stage 1
    builder.out_and_back_individual_time_trial(italy.urbino(), 9.0)

    # Stage 2
    builder.road_stage(italy.urbino(), italy.ascoli_piceno(), 230.0)

    # Stage 3
    builder.road_stage(italy.ascoli_piceno(), italy.vasto(), 184.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.road_stage(italy.vasto(), italy.rodi_garganico(), 123.0)
    builder.team_time_trial(italy.rodi_garganico(), italy.vieste(), 40.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(italy.vieste(), italy.santa_maria_capua_vetere(), 260.0)

    # Stage 6
    builder.road_stage(italy.santa_maria_capua_vetere(), italy.campitello_matese(), 137.0)

    # Stage 7
    builder.road_stage(italy.campitello_matese(), italy.avezzano(), 178.0)

    # Stage 8
    builder.road_stage(italy.avezzano(), italy.chianciano_terme(), 251.0)

    # Stage 9
    builder.road_stage(italy.pienza(), italy.marina_di_massa(), 235.0)

    # Stage 10
    builder.road_stage(italy.carrara(), italy.salsomaggiore_terme(), 190.0)

    # Stage 11
    builder.road_stage(italy.parma(), italy.colle_don_bosco(), 229.0)

    # Stage 12
    builder.road_stage(italy.novara(), italy.selvino(), 205.0)

    # Stage 13
    builder.road_stage(italy.bergamo(), italy.chiesa_in_valmalenco(), 129.0)

    # Stage 14
    builder.road_stage(italy.chiesa_in_valmalenco(), italy.bormio(), 120.0)

    # Stage 15
    builder.road_stage(italy.spondigna(), italy.merano2000(), 83.0)

    # Stage 16
    builder.road_stage(italy.merano(), austria.innsbruck(), 176.0)

    # Stage 17
    builder.road_stage(austria.innsbruck(), italy.borgo_valsugana(), 221.0)

    # Stage 18
    builder.individual_time_trial(italy.levico_terme(), italy.valico_del_vetriolo(), 18.0)

    # Stage 19
    builder.road_stage(italy.borgo_valsugana(), italy.arta_terme(), 223.0)

    # Stage 20
    builder.road_stage(italy.arta_terme(), italy.lido_di_jesolo(), 212.0)

    # Stages 21a & 21b
    builder.enable_split_stages()
    builder.road_stage(italy.lido_di_jesolo(), italy.vittorio_veneto(), 73.0)
    builder.out_and_back_individual_time_trial(italy.vittorio_veneto(), 43.0)
    builder.disable_split_stages()

    return builder.build()

def giro1989():

    builder = TourOfItalyBuilder(1989,5,21)

    # Stage 1
    builder.road_stage(italy.taormina(), italy.catania(), 123.0)

    # Stage 2
    builder.mountain_stage(italy.catania())
    builder.summit_finish(mountains.sciliy.mount_etna(), ColCategory.C1, 132)

    # Stage 3
    builder.team_time_trial(italy.villafranca(), italy.messina(), 32.5)

    # Stage 4
    builder.road_stage(italy.scilla(), italy.cosenza(), 204.0)

    # Stage 5
    builder.road_stage(italy.cosenza(), italy.potenza(), 275.0)

    # Stage 6
    builder.road_stage(italy.potenza(), italy.campobasso(), 223.0)

    # Stage 7
    builder.road_stage(italy.isernia(), italy.rome(), 208.0)

    # Stage 8
    builder.road_stage(italy.rome(), italy.gran_sasso_d_italia(), 179.0)

    # Stage 9
    builder.road_stage(italy.l_aquila(), italy.gubbio(), 221.0)

    # Stage 10
    builder.individual_time_trial(italy.pesaro(), italy.riccione(), 36.8)

    # Stage 11
    builder.road_stage(italy.riccione(), italy.mantua(), 148.0)

    # Stage 12
    builder.road_stage(italy.mantua(), italy.mira(), 148.0)

    # Stage 13
    builder.road_stage(italy.padua(), italy.auronzo_di_cadore(), 207.0)

    # Stage 14
    builder.road_stage(italy.auronzo_di_cadore(), italy.corvara(), 131.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(italy.corvara(), italy.trento(), 131.0)
    builder.criterium(italy.trento(), 83.2)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(italy.trento(), italy.santa_caterina_di_valfurva(), 208.0)

    # Stage 17
    builder.road_stage(italy.sondrio(), italy.meda(), 137.0)

    # Stage 18
    builder.individual_time_trial(switzerland.mendrisio(), switzerland.monte_generoso(), 10.7)

    # Stage 19
    builder.road_stage(italy.meda(), italy.tortona(), 198.0)

    # Stage 20
    builder.road_stage(italy.voghera(), italy.la_spezia(), 220.0)

    # Stage 21
    builder.road_stage(italy.la_spezia(), italy.prato(), 216.0)

    # Stage 22
    builder.individual_time_trial(italy.prato(), italy.florence(), 53.0)

    return builder.build()

def giro1990():

    builder = TourOfItalyBuilder(1990,5,18)

    # Prologue
    builder.out_and_back_prologue(italy.bari(), 13.0)
    # Stage 1
    builder.road_stage(italy.bari(), italy.sala_consilina(), 239.0)

    # Stage 2
    builder.road_stage(italy.sala_consilina(), italy.mount_vesuvius(), 190.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.road_stage(italy.ercolano(), italy.nola(), 31.0)
    builder.road_stage(italy.nola(), italy.sora(), 164.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(italy.sora(), italy.teramo(), 233.0)

    # Stage 5
    builder.road_stage(italy.teramo(), italy.fabriano(), 200.0)

    # Stage 6
    builder.road_stage(italy.fabriano(), italy.vallombrosa(), 197.0)

    # Stage 7
    builder.road_stage(italy.reggello(), italy.marina_di_pietrasanta(), 188.0)

    # Stage 8
    builder.road_stage(italy.la_spezia(), italy.langhirano(), 176.0)

    # Stage 9
    builder.individual_time_trial(italy.grinzane_cavour(), italy.cuneo(), 68.0)

    # Stage 10
    builder.road_stage(italy.cuneo(), italy.lodi(), 241.0)

    # Stage 11
    builder.road_stage(italy.brescia(), italy.baselga_di_pine(), 241.0)

    # Stage 12
    builder.road_stage(italy.baselga_di_pine(), italy.udine(), 224.0)

    # Stage 13
    builder.criterium(austria.klagenfurt(), 164.0)

    # Stage 14
    builder.road_stage(austria.velden_am_worther(), italy.dobbiaco(), 226.0)

    # Stage 15
    builder.mountain_stage(italy.dobbiaco())
    builder.summit_finish(mountains.dolomites.passo_pordoi(), ColCategory.C1, 171.0)

    # Stage 16
    builder.mountain_stage(italy.moena())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 223.0)

    # Stage 17
    builder.road_stage(mountains.alps.aprica(), italy.gallarate(), 180.0)

    # Stage 18
    builder.individual_time_trial(italy.gallarate(), italy.sacro_monte_di_varese(), 39.0)

    # Stage 19
    builder.criterium(italy.milan(), 90.0)

    return builder.build()

def giro1991():

    builder = TourOfItalyBuilder(1991,5,26)

    # Stage 1
    builder.criterium(italy.olbia(), 193.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(italy.olbia(), italy.sassari(), 127.0)
    builder.out_and_back_individual_time_trial(italy.sassari(), 7.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(italy.sassari(), italy.cagliari(), 231.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.criterium(italy.sorrento(), 170.0)

    # Stage 5
    builder.road_stage(italy.sorrento(), italy.scanno(), 246.0)

    # Stage 6
    builder.road_stage(italy.scanno(), italy.rieti(), 205.0)

    # Stage 7
    builder.road_stage(italy.rieti(), italy.citta_di_castello(), 174.0)

    # Stage 8
    builder.road_stage(italy.citta_di_castello(), italy.prato(), 169.0)

    # Stage 9
    builder.road_stage(italy.prato(), italy.felino(), 229.0)

    # Stage 10
    builder.individual_time_trial(italy.collecchio(), italy.langhirano(), 43.0)

    # Stage 11
    builder.road_stage(italy.sala_baganza(), italy.savona(), 223.0)

    # Stage 12
    builder.road_stage(italy.savona(), italy.pian_del_re(), 182.0)

    # Stage 13
    builder.mountain_stage(italy.savigliano())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 192.0)

    # Stage 14
    builder.road_stage(italy.turin(), italy.morbegno(), 239.0)

    # Stage 15
    builder.mountain_stage(italy.morbegno())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 132.0)

    # Stage 16
    builder.road_stage(italy.tirano(), italy.selva_di_val_gardena(), 220.0)

    # Stage 17
    builder.mountain_stage(italy.selva_di_val_gardena())
    builder.summit_finish(mountains.dolomites.passo_pordoi(), ColCategory.C1, 169.0)

    # Stage 18
    builder.road_stage(italy.pozza_di_fassa(), italy.castelfranco_veneto(), 165.0)

    # Stage 19
    builder.road_stage(italy.castelfranco_veneto(), italy.brescia(), 185.0)

    # Stage 20
    builder.individual_time_trial(italy.brescia(), italy.casteggio(), 66.0)

    # Stage 21
    builder.road_stage(italy.pavia(), italy.milan(), 153.0)

    return builder.build()

def giro1992():

    builder = TourOfItalyBuilder(1992,5,24)

    # Stage 1
    builder.out_and_back_individual_time_trial(italy.genoa(), 8.0)

    # Stage 2
    builder.road_stage(italy.genoa(), italy.uliveto_terme(), 194.0)

    # Stage 3
    builder.road_stage(italy.uliveto_terme(), italy.arezzo(), 174.0)

    # Stage 4
    builder.individual_time_trial(italy.arezzo(), italy.sansepolcro(), 38.0)

    # Stage 5
    builder.road_stage(italy.sansepolcro(), italy.porto_sant_elpidio(), 198.0)

    # Stage 6
    builder.road_stage(italy.porto_sant_elpidio(), italy.sulmona(), 223.0)

    # Stage 7
    builder.road_stage(italy.roccaraso(), italy.melfi(), 232.0)

    # Stage 8
    builder.road_stage(italy.melfi(), italy.aversa(), 184.0)

    # Stage 9
    builder.road_stage(italy.aversa(), italy.latina(), 165.0)

    # Stage 10
    builder.road_stage(italy.latina(), italy.monte_terminillo(), 196.0)

    # Stage 11
    builder.road_stage(italy.montepulciano(), italy.imola(), 233.0)

    # Stage 12
    builder.road_stage(italy.imola(), italy.bassano_del_grappa(), 233.0)

    # Stage 13
    builder.road_stage(italy.bassano_del_grappa(), italy.corvara(), 204.0)

    # Stage 14
    builder.road_stage(italy.corvara(), italy.monte_bondone(), 205.0)

    # Stage 15
    builder.road_stage(italy.riva_del_garda(), italy.palazzolo_sull_oglio(), 171.0)

    # Stage 16
    builder.road_stage(italy.palazzolo_sull_oglio(), italy.sondrio(), 166.0)

    # Stage 17
    builder.road_stage(italy.sondrio(), italy.vercelli(), 203.0)

    # Stage 18
    builder.road_stage(italy.vercelli(), italy.pian_del_re(), 200.0)

    # Stage 19
    builder.road_stage(italy.saluzzo(), italy.pila(), 260.0)

    # Stage 20
    builder.road_stage(italy.saint_vincent(), italy.verbania(), 201.0)

    # Stage 21
    builder.road_stage(italy.verbania(), italy.vigevano(), 95.0)

    # Stage 22
    builder.individual_time_trial(italy.vigevano(), italy.milan(), 66.0)

    return builder.build()

def giro1993():

    builder = TourOfItalyBuilder(1993,5,23)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(italy.porto_azzurro(), italy.porteferraio(), 85.0)
    builder.out_and_back_individual_time_trial(italy.porteferraio(), 9.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(italy.grosseto(), italy.rieti(), 224.0)

    # Stage 3
    builder.road_stage(italy.rieti(), italy.scanno(), 153.0)

    # Stage 4
    builder.road_stage(italy.lago_di_scanno(), italy.marcianise(), 179.0)

    # Stage 5
    builder.road_stage(italy.paestum(), italy.terme_luigiane(), 210.0)

    # Stage 6
    builder.road_stage(italy.villafranca_tirrena(), italy.messina(), 130.0)

    # Stage 7
    builder.road_stage(italy.capo_d_orlando(), italy.agrigento(), 240.0)

    # Stage 8
    builder.road_stage(italy.agrigento(), italy.palermo(), 140.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(italy.montelibretti(), italy.fabriano(), 216.0)

    # Stage 10
    builder.out_and_back_individual_time_trial(italy.senigallia(), 28.0)

    # Stage 11
    builder.road_stage(italy.senigallia(), italy.dozza(), 184.0)

    # Stage 12
    builder.road_stage(italy.dozza(), italy.asiago(), 239.0)

    # Stage 13
    builder.road_stage(italy.asiago(), italy.corvara(), 220.0)

    # Stage 14
    builder.criterium(italy.corvara(), 245.0)

    # Stage 15
    builder.road_stage(italy.corvara(), italy.lumezzane(), 263.0)

    # Stage 16
    builder.road_stage(italy.lumezzane(), italy.borgo_val_di_taro(), 181.0)

    # Stage 17
    builder.road_stage(italy.varazze(), italy.pontechianale(), 223.0)

    # Stage 18
    builder.road_stage(italy.sampeyre(), italy.fossano(), 150.0)

    # Stage 19
    builder.mountain_time_trial(italy.pinerolo())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 55.0)

    # Stage 20
    builder.road_stage(italy.turin(), italy.santuario_di_oropa(), 162.0)

    # Stage 21
    builder.road_stage(italy.biella(), italy.milan(), 166.0)

    return builder.build()

def giro1994():

    builder = TourOfItalyBuilder(1994,5,22)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.criterium(italy.bologna(), 86.0)
    builder.out_and_back_individual_time_trial(italy.bologna(), 7.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(italy.bologna(), italy.osimo(), 232.0)

    # Stage 3
    builder.road_stage(italy.osimo(), italy.loreto_aprutino(), 185.0)

    # Stage 4
    builder.road_stage(italy.montesilvano(), italy.campitello_matese(), 204.0)

    # Stage 5
    builder.road_stage(italy.campobasso(), italy.melfi(), 158.0)

    # Stage 6
    builder.road_stage(italy.potenza(), italy.caserta(), 215.0)

    # Stage 7
    builder.criterium(italy.fiuggi(), 119.0)

    # Stage 8
    builder.individual_time_trial(italy.grosseto(), italy.follonica(), 44.0)

    # Stage 9
    builder.road_stage(italy.castiglione_della_pescaia(), italy.pontedera(), 153.0)

    # Stage 10
    builder.criterium(italy.marostica(), 115.0)

    # Stage 11
    builder.road_stage(italy.marostica(), italy.bibione(), 165.0)

    # Stage 12
    builder.road_stage(italy.bibione(), slovenia.kranj(), 204.0)

    # Stage 13
    builder.road_stage(slovenia.kranj(), austria.lienz(), 231.0)

    # Stage 14
    builder.road_stage(austria.lienz(), italy.merano(), 235.0)

    # Stage 15
    builder.mountain_stage(italy.merano())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 195.0)

    # Stage 16
    builder.road_stage(italy.sondrio(), italy.stradella(), 220.0)

    # Stage 17
    builder.road_stage(italy.santa_maria_della_versa(), italy.lavagna(), 190.0)

    # Stage 18
    builder.individual_time_trial(italy.chiavari(), italy.passo_del_bocco(), 35.0)

    # Stage 19
    builder.road_stage(italy.lavagna(), italy.bra(), 212.0)

    # Stage 20
    builder.mountain_stage(italy.cuneo())
    builder.summit_finish(mountains.alps.les_deux_alpes(), ColCategory.C1, 206.0)

    # Stage 21
    builder.mountain_stage(mountains.alps.les_deux_alpes())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 121.0)

    # Stage 22
    builder.road_stage(italy.turin(), italy.milan(), 198.0)

    return builder.build()

def giro1995():

    builder = TourOfItalyBuilder(1995,5,13)

    # Stage 1
    builder.road_stage(italy.perugia(), italy.terni(), 205.0)

    # Stage 2
    builder.individual_time_trial(italy.foligno(), italy.assisi(), 19.0)

    # Stage 3
    builder.road_stage(italy.spoleto(), italy.marotta(), 161.0)

    # Stage 4
    builder.road_stage(italy.mondolfo(), italy.loreto(), 192.0)

    # Stage 5
    builder.road_stage(italy.porto_recanati(), italy.tortoreto(), 182.0)

    # Stage 6
    builder.road_stage(italy.trani(), italy.taranto(), 165.0)

    # Stage 7
    builder.road_stage(italy.taranto(), italy.terme_luigiane(), 216.0)

    # Stage 8
    builder.road_stage(italy.acquappesa(), italy.massiccio_del_sirino(), 209.0)

    # Stage 9
    builder.road_stage(italy.terme_la_calda(), italy.salerno(), 165.0)

    # Stage 10
    builder.individual_time_trial(italy.telese_terme(), italy.maddaloni(), 42.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(italy.pietrasanta(), italy.il_ciocco(), 175.0)

    # Stage 12
    builder.road_stage(italy.borgo_a_mozzano(), italy.cento(), 195.0)

    # Stage 13
    builder.road_stage(italy.pieve_di_cento(), italy.rovereto(), 218.0)

    # Stage 14
    builder.road_stage(italy.trento(), italy.schnals(), 240.0)

    # Stage 15
    builder.road_stage(italy.schnals(), switzerland.lenzerheide(), 185.0)

    # Stage 16
    builder.road_stage(switzerland.lenzerheide(), italy.treviglio(), 224.0)

    # Stage 17
    builder.individual_time_trial(italy.cenate_sotto(), italy.selvino(), 43.0)

    # Stage 18
    builder.road_stage(italy.stradella(), italy.sanctuario_di_vicoforte(), 221.0)

    # Stage 19
    builder.road_stage(italy.mondovi(), italy.pontechianale(), 130.0)

    # Stage 20
    builder.road_stage(france.briancon(), italy.gressoney_saint_jean(), 208.0)

    # Stage 21
    builder.road_stage(italy.pont_saint_martin(), italy.luino(), 190.0)

    # Stage 22
    builder.road_stage(italy.luino(), italy.milan(), 148.0)

    return builder.build()

def giro1996():

    builder = TourOfItalyBuilder(1996,5,18)

    # Stage 1
    builder.criterium(greece.athens(), 170.0)

    # Stage 2
    builder.road_stage(greece.eleusis(), greece.naupactus(), 235.0)

    # Stage 3
    builder.road_stage(greece.missolonghi(), greece.ioannina(), 199.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.criterium(italy.ostuni(), 147.0)

    # Stage 5
    builder.road_stage(italy.metaponto(), italy.crotone(), 196.0)

    # Stage 6
    builder.road_stage(italy.crotone(), italy.catanzaro(), 176.0)

    # Stage 7
    builder.road_stage(italy.amantea(), italy.massiccio_del_sirino(), 164.0)

    # Stage 8
    builder.road_stage(italy.polla(), italy.naples(), 135.0)

    # Stage 9
    builder.road_stage(italy.naples(), italy.fiuggi(), 184.0)

    # Stage 10
    builder.road_stage(italy.arezzo(), italy.prato(), 164.0)

    # Stage 11
    builder.road_stage(italy.prato(), italy.marino_di_massa(), 130.0)

    # Stage 12
    builder.road_stage(italy.aulla(), italy.loano(), 195.0)

    # Stage 13
    builder.mountain_stage(italy.loano())
    builder.summit_finish(mountains.alps.prato_nevoso(), ColCategory.C1, 115.0)

    # Stage 14
    builder.road_stage(italy.sanctuario_di_vicoforte(), france.briancon(), 202.0)

    # Stage 15
    builder.road_stage(france.briancon(), italy.aosta(), 235.0)

    # Stage 16
    builder.road_stage(italy.aosta(), switzerland.lausanne(), 180.0)

    # Stage 17
    builder.road_stage(switzerland.lausanne(), italy.biella(), 236.0)

    # Stage 18
    builder.road_stage(italy.meda(), italy.vicenza(), 216.0)

    # Stage 19
    builder.individual_time_trial(italy.vicenza(), italy.marostica(), 62.0)

    # Stage 20
    builder.mountain_stage(italy.marostica())
    builder.summit_finish(mountains.dolomites.passo_pordoi(), ColCategory.C1, 220.0)

    # Stage 21
    builder.mountain_stage(italy.cavalese())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 250.0)

    # Stage 22
    builder.road_stage(italy.sondrio(), italy.milan(), 176.0)

    return builder.build()

def giro1997():

    builder = TourOfItalyBuilder(1997,5,17)

    # Stage 1
    builder.criterium(italy.venezia(), 128.0)

    # Stage 2
    builder.road_stage(italy.mestre(), italy.cervia(), 211.0)

    # Stage 3
    builder.individual_time_trial(italy.santarcangelo_di_romagna(), san_marino.san_marino(), 18.0)

    # Stage 4
    builder.road_stage(san_marino.san_marino(), italy.arezzo(), 156.0)

    # Stage 5
    builder.road_stage(italy.arezzo(), italy.monte_terminillo(), 215.0)

    # Stage 6
    builder.road_stage(italy.rieti(), italy.lanciano(), 210.0)

    # Stage 7
    builder.road_stage(italy.lanciano(), italy.mondragone(), 210.0)

    # Stage 8
    builder.road_stage(italy.mondragone(), italy.cava_de_tirreni(), 212.0)

    # Stage 9
    builder.road_stage(italy.cava_de_tirreni(), italy.castrovillari(), 232.0)

    # Stage 10
    builder.road_stage(italy.castrovillari(), italy.taranto(), 195.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.criterium(italy.lido_di_camaiore(), 155.0)

    # Stage 12
    builder.road_stage(italy.la_spezia(), italy.varazze(), 214.0)

    # Stage 13
    builder.road_stage(italy.varazze(), italy.cuneo(), 150.0)

    # Stage 14
    builder.road_stage(italy.racconigi(), italy.breuil_cervinia(), 240.0)

    # Stage 15
    builder.road_stage(italy.verres(), italy.borgomanero(), 173.0)

    # Stage 16
    builder.road_stage(italy.borgomanero(), italy.dalmine(), 158.0)

    # Stage 17
    builder.road_stage(italy.dalmine(), italy.verona(), 200.0)

    # Stage 18
    builder.individual_time_trial(italy.baselga_di_pine(), italy.cavalese(), 40.0)

    # Stage 19
    builder.road_stage(italy.predazzo(), italy.pfalzen(), 222.0)

    # Stage 20
    builder.road_stage(italy.bruneck(), italy.passo_del_tonale(), 176.0)

    # Stage 21
    builder.road_stage(italy.male(), italy.edolo(), 238.0)

    # Stage 22
    builder.road_stage(italy.boario_terme(), italy.milan(), 165.0)

    return builder.build()

def giro1998():

    builder = TourOfItalyBuilder(1998,5,16)

    # Prologue
    builder.out_and_back_prologue(france.nice(), 8.0)
    # Stage 1
    builder.road_stage(france.nice(), italy.cuneo(), 159.0)

    # Stage 2
    builder.road_stage(italy.alba(), italy.imperia(), 160.0)

    # Stage 3
    builder.road_stage(italy.rapallo(), italy.forte_dei_marmi(), 196.0)

    # Stage 4
    builder.road_stage(italy.viareggio(), italy.monte_argentario(), 239.0)

    # Stage 5
    builder.road_stage(italy.orbetello(), italy.frascati(), 206.0)

    # Stage 6
    builder.road_stage(italy.maddaloni(), italy.laga_laceno(), 158.0)

    # Stage 7
    builder.road_stage(italy.montella(), italy.matera(), 238.0)

    # Stage 8
    builder.road_stage(italy.matera(), italy.lecce(), 191.0)

    # Stage 9
    builder.road_stage(italy.foggia(), italy.vasto(), 167.0)

    # Stage 10
    builder.road_stage(italy.vasto(), italy.macerata(), 212.0)

    # Stage 11
    builder.road_stage(italy.macerata(), san_marino.san_marino(), 220.0)

    # Stage 12
    builder.road_stage(san_marino.san_marino(), italy.carpi(), 202.0)

    # Stage 13
    builder.road_stage(italy.carpi(), italy.schio(), 166.0)

    # Stage 14
    builder.road_stage(italy.schio(), italy.piancavallo(), 165.0)

    # Stage 15
    builder.out_and_back_individual_time_trial(italy.trieste(), 40.0)

    # Stage 16
    builder.road_stage(italy.udine(), italy.asiago(), 227.0)

    # Stage 17
    builder.road_stage(italy.asiago(), italy.selva(), 217.0)

    # Stage 18
    builder.road_stage(italy.selva(), italy.passo_di_pampeagno(), 115.0)

    # Stage 19
    builder.road_stage(italy.cavalese(), italy.plan_di_montecampione(), 239.0)

    # Stage 20
    builder.road_stage(italy.darfo_boario_terme(), switzerland.mendrisio(), 137.0)

    # Stage 21
    builder.individual_time_trial(switzerland.mendrisio(), switzerland.lugano(), 34.0)

    # Stage 22
    builder.road_stage(switzerland.lugano(), italy.milan(), 173.0)

    return builder.build()

def giro1999():

    builder = TourOfItalyBuilder(1999,5,15)

    # Stage 1
    builder.road_stage(italy.agrigento(), italy.modica(), 175.0)

    # Stage 2
    builder.road_stage(italy.noto(), italy.catania(), 133.0)

    # Stage 3
    builder.road_stage(italy.catania(), italy.messina(), 176.0)

    # Stage 4
    builder.road_stage(italy.vibo_valentia(), italy.terme_luigiane(), 186.0)

    # Stage 5
    builder.road_stage(italy.terme_luigiane(), italy.massiccio_del_sirino(), 144.0)

    # Stage 6
    builder.road_stage(italy.lauria(), italy.foggia(), 257.0)

    # Stage 7
    builder.road_stage(italy.foggia(), italy.lanciano(), 153.0)

    # Stage 8
    builder.road_stage(italy.pescara(), italy.gran_sasso_d_italia(), 253.0)

    # Stage 9
    builder.out_and_back_individual_time_trial(italy.ancona(), 32.0)

    # Stage 10
    builder.road_stage(italy.ancona(), italy.sansepolcro(), 189.0)

    # Stage 11
    builder.road_stage(italy.sansepolcro(), italy.cesenatico(), 125.0)

    # Stage 12
    builder.road_stage(italy.cesenatico(), italy.sassuolo(), 168.0)

    # Stage 13
    builder.road_stage(italy.sassuolo(), italy.rapallo(), 243.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(italy.bra(), italy.borgo_san_dalmazzo(), 187.0)

    # Stage 15
    builder.road_stage(italy.racconigi(), italy.santuario_di_oropa(), 160.0)

    # Stage 16
    builder.road_stage(italy.biella(), italy.lumezzane(), 232.0)

    # Stage 17
    builder.road_stage(italy.lumezzane(), italy.castelfranco_veneto(), 215.0)

    # Stage 18
    builder.out_and_back_individual_time_trial(italy.treviso(), 45.0)

    # Stage 19
    builder.road_stage(italy.castelfranco_veneto(), italy.alpe_di_pampeago(), 166.0)

    # Stage 20
    builder.road_stage(italy.predazzo(), italy.madonna_di_campiglio(), 175.0)

    # Stage 21
    builder.mountain_stage(italy.madonna_di_campiglio())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 190.0)

    # Stage 22
    builder.road_stage(italy.darfo_boario_terme(), italy.milan(), 170.0)

    return builder.build()

def giro2000():

    builder = TourOfItalyBuilder(2000,5,13)

    # Prologue
    builder.out_and_back_prologue(italy.rome(), 4.6)
    # Stage 1
    builder.road_stage(italy.rome(), italy.terracina(), 125.0)

    # Stage 2
    builder.road_stage(italy.terracina(), italy.maddaloni(), 225.0)

    # Stage 3
    builder.road_stage(italy.paestum(), italy.scalea(), 177.0)

    # Stage 4
    builder.road_stage(italy.scalea(), italy.matera(), 233.0)

    # Stage 5
    builder.road_stage(italy.matera(), italy.peschici(), 232.0)

    # Stage 6
    builder.road_stage(italy.peschici(), italy.vasto(), 160.0)

    # Stage 7
    builder.road_stage(italy.vasto(), italy.teramo(), 182.0)

    # Stage 8
    builder.road_stage(italy.corinaldo(), italy.prato(), 265.0)

    # Stage 9
    builder.road_stage(italy.prato(), italy.abetone(), 138.0)

    # Stage 10
    builder.road_stage(italy.san_marcello_pistoiese(), italy.padua(), 253.0)

    # Stage 11
    builder.individual_time_trial(italy.lignano_sabbiadoro(), italy.bibione(), 45.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(italy.bibione(), italy.feltre(), 184.0)

    # Stage 13
    builder.road_stage(italy.feltre(), italy.selva(), 186.0)

    # Stage 14
    builder.road_stage(italy.selva(), italy.bormio(), 203.0)

    # Stage 15
    builder.road_stage(italy.bormio(), italy.brescia(), 180.0)

    # Stage 16
    builder.road_stage(italy.brescia(), italy.meda(), 102.0)

    # Stage 17
    builder.road_stage(italy.meda(), italy.genoa(), 236.0)

    # Stage 18
    builder.mountain_stage(italy.genoa())
    builder.summit_finish(mountains.alps.prato_nevoso(), ColCategory.C1, 173.0)

    # Stage 19
    builder.road_stage(italy.saluzzo(), france.briancon(), 176.0)

    # Stage 20
    builder.mountain_time_trial(france.briancon())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 32.0)

    # Stage 21
    builder.road_stage(italy.turin(), italy.milan(), 189.0)

    return builder.build()

def giro2001():

    builder = TourOfItalyBuilder(2001,5,19)

    # Prologue
    builder.prologue(italy.montesilvano(), italy.pescara(), 7.0)
    # Stage 1
    builder.road_stage(italy.guilianova(), italy.francavilla_al_mare(), 205.0)

    # Stage 2
    builder.road_stage(italy.fossacesia(), italy.lucera(), 163.0)

    # Stage 3
    builder.road_stage(italy.lucera(), italy.potenza(), 149.0)

    # Stage 4
    builder.road_stage(italy.potenza(), italy.mercogliano(), 169.0)

    # Stage 5
    builder.road_stage(italy.avellino(), italy.nettuno(), 229.0)

    # Stage 6
    builder.road_stage(italy.nettuno(), italy.rieti(), 152.0)

    # Stage 7
    builder.road_stage(italy.rieti(), italy.montevarchi(), 239.0)

    # Stage 8
    builder.road_stage(italy.montecatini_terme(), italy.reggio_emilia(), 185.0)

    # Stage 9
    builder.road_stage(italy.reggio_emilia(), italy.rovigo(), 140.0)

    # Stage 10
    builder.road_stage(italy.lido_di_jesolo(), slovenia.ljubljana(), 212.0)

    # Stage 11
    builder.road_stage(slovenia.bled(), italy.gorizia(), 187.0)

    # Stage 12
    builder.road_stage(italy.gradisca_d_isonzo(), italy.montebelluna(), 139.0)

    # Stage 13
    builder.mountain_stage(italy.montebelluna())
    builder.summit_finish(mountains.dolomites.passo_pordoi(), ColCategory.C1, 225.0)

    # Stage 14
    builder.road_stage(italy.cavalese(), italy.arco(), 160.0)

    # Stage 15
    builder.individual_time_trial(italy.sirmione(), italy.salo(), 55.0)

    # Stage 16
    builder.road_stage(italy.erbusco(), italy.parma(), 142.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.criterium(italy.san_remo(), 123.0)

    # Stage 18
    builder.road_stage(italy.imperia(), italy.sant_anna_di_vinadio(), 230.0)

    # Stage 19
    builder.road_stage(italy.alba(), italy.busto_arsizio(), 163.0)

    # Stage 20
    builder.road_stage(italy.busto_arsizio(), italy.arona(), 181.0)

    # Stage 21
    builder.road_stage(italy.arona(), italy.milan(), 125.0)

    return builder.build()

def giro2002():

    builder = TourOfItalyBuilder(2002,5,11)

    # Prologue
    builder.out_and_back_prologue(netherlands.groningen(), 6.5)

    # Stage 1
    builder.road_stage(netherlands.groningen(), germany.munster(), 215.0)

    # Stage 2
    builder.road_stage(germany.cologne(), belgium.ans(), 209.0)

    # Stage 3
    builder.road_stage(belgium.verviers(), luxembourg.esch_sur_alzette(), 206.0)

    # Stage 4
    builder.road_stage(luxembourg.esch_sur_alzette(), france.strasbourg(), 232.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(italy.fossano(), italy.limone_piemonte(), 150.0)

    # Stage 6
    builder.road_stage(italy.cuneo(), italy.varazze(), 190.0)

    # Stage 7
    builder.road_stage(italy.viareggio(), italy.lido_di_camaiore(), 159.0)

    # Stage 8
    builder.road_stage(italy.capannori(), italy.orvieto(), 237.0)

    # Stage 9
    builder.road_stage(italy.tivoli(), italy.caserta(), 41.0)

    # Stage 10
    builder.road_stage(italy.maddaloni(), italy.benevento(), 118.0)

    # Stage 11
    builder.road_stage(italy.benevento(), italy.campitello_matese(), 140.0)

    # Stage 12
    builder.road_stage(italy.campobasso(), italy.chieti(), 200.0)

    # Stage 13
    builder.road_stage(italy.chieti(), italy.san_giacomo_di_valle_castellana(), 190.0)

    # Stage 14
    builder.out_and_back_individual_time_trial(italy.numana(), 30.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(italy.terme_euganee(), italy.conegliano(), 156.0)

    # Stage 16
    builder.road_stage(italy.conegliano(), italy.corvara(), 163.0)

    # Stage 17
    builder.road_stage(italy.corvara(), italy.folgaria(), 222.0)

    # Stage 18
    builder.road_stage(italy.rovereto(), italy.brescia(), 143.0)

    # Stage 19
    builder.individual_time_trial(italy.cambiago(), italy.monticello_brianza(), 46.0)

    # Stage 20
    builder.road_stage(italy.cantu(), italy.milan(), 141.0)

    return builder.build()

def giro2003():

    builder = TourOfItalyBuilder(2003,5,10)

    # Stage 1
    builder.criterium(italy.lecce(), 201.0)

    # Stage 2
    builder.road_stage(italy.copertino(), italy.matera(), 177.0)

    # Stage 3
    builder.road_stage(italy.policoro(), italy.term_luigiane(), 145.0)

    # Stage 4
    builder.road_stage(italy.term_luigiane(), italy.vibo_valentia(), 170.0)

    # Stage 5
    builder.road_stage(italy.messina(), italy.catania(), 176.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(italy.maddaloni(), italy.avezzano(), 222.0)

    # Stage 7
    builder.road_stage(italy.avezzano(), italy.monte_terminillo(), 146.0)

    # Stage 8
    builder.road_stage(italy.rieti(), italy.arezzo(), 214.0)

    # Stage 9
    builder.road_stage(italy.arezzo(), italy.montecatini_terme(), 160.0)

    # Stage 10
    builder.road_stage(italy.montecatini_terme(), italy.faenza(), 202.0)

    # Stage 11
    builder.road_stage(italy.faenza(), italy.san_dona_di_piave(), 222.0)

    # Stage 12
    builder.mountain_stage(italy.san_dona_di_piave())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 185.0)

    # Stage 13
    builder.road_stage(italy.pordenone(), italy.marostica(), 149.0)

    # Stage 14
    builder.road_stage(italy.marostica(), italy.alpe_di_pampeago(), 162.0)

    # Stage 15
    builder.individual_time_trial(italy.merano(), italy.bolzano(), 42.5)

    # Stage 16
    builder.road_stage(italy.arco(), italy.pavia(), 207.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.salice_terme(), italy.asti(), 117.0)

    # Stage 18
    builder.road_stage(italy.sanuario_di_vicoforte(), italy.chianale(), 174.0)

    # Stage 19
    builder.road_stage(italy.canelli(), italy.cascata_del_toce(), 239.0)

    # Stage 20
    builder.road_stage(italy.cannobio(), italy.cantu(), 133.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.milan(), 33.0)

    return builder.build()

def giro2004():

    builder = TourOfItalyBuilder(2004,5,8)

    # Prologue
    builder.out_and_back_prologue(italy.genoa(), 6.9)
    # Stage 1
    builder.road_stage(italy.genoa(), italy.alba(), 143.0)

    # Stage 2
    builder.road_stage(italy.novi_ligure(), italy.pontremoli(), 184.0)

    # Stage 3
    builder.road_stage(italy.pontremoli(), italy.corno_alle_scale(), 191.0)

    # Stage 4
    builder.road_stage(italy.porretta_terme(), italy.civitella_di_val_di_chiana(), 184.0)

    # Stage 5
    builder.road_stage(italy.civitella_di_val_di_chiana(), italy.spoleto(), 177.0)

    # Stage 6
    builder.road_stage(italy.spoleto(), italy.valmontone(), 164.0)

    # Stage 7
    builder.road_stage(italy.frosinone(), italy.montevergine_di_mercogliano(), 214.0)

    # Stage 8
    builder.road_stage(italy.giffoni_valle_piana(), italy.policoro(), 214.0)

    # Stage 9
    builder.road_stage(italy.policoro(), italy.carovigno(), 142.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.porto_sant_elpidio(), italy.ascoli_piceno(), 146.0)

    # Stage 11
    builder.road_stage(italy.porto_sant_elpidio(), italy.cesena(), 228.0)

    # Stage 12
    builder.road_stage(italy.cesena(), italy.treviso(), 210.0)

    # Stage 13
    builder.out_and_back_individual_time_trial(italy.trieste(), 52.0)

    # Stage 14
    builder.road_stage(italy.trieste(), croatia.pula(), 175.0)

    # Stage 15
    builder.road_stage(croatia.porec(), italy.san_vendemiano(), 234.0)

    # Stage 16
    builder.road_stage(italy.san_vendemiano(), italy.pfalzen(), 217.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.bruneck(), italy.fondo_sarnonico(), 153.0)

    # Stage 18
    builder.road_stage(italy.cles(), italy.bormio2000(), 118.0)

    # Stage 19
    builder.road_stage(italy.bormio(), italy.presolana(), 122.0)

    # Stage 20
    builder.road_stage(italy.clusone(), italy.milan(), 149.0)

    return builder.build()

def giro2005():

    builder = TourOfItalyBuilder(2005,5,7)

    # Prologue
    builder.out_and_back_prologue(italy.reggio_calabria(), 1.1)
    # Stage 1
    builder.road_stage(italy.reggio_calabria(), italy.tropea(), 208.0)

    # Stage 2
    builder.road_stage(italy.catanzaro_lido(), italy.santa_maria_del_cedro(), 182.0)

    # Stage 3
    builder.road_stage(italy.diamante(), italy.giffoni_valle_piana(), 205.0)

    # Stage 4
    builder.road_stage(italy.giffoni_valle_piana(), italy.frosinone(), 211.0)

    # Stage 5
    builder.road_stage(italy.celano(), italy.l_aquila(), 223.0)

    # Stage 6
    builder.road_stage(italy.viterbo(), italy.marina_di_grosseto(), 153.0)

    # Stage 7
    builder.road_stage(italy.grosseto(), italy.pistoia(), 211.0)

    # Stage 8
    builder.individual_time_trial(italy.lamporecchio(), italy.florence(), 45.0)

    # Stage 9
    builder.road_stage(italy.florence(), italy.ravenna(), 139.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.ravenna(), italy.rossanto_veneto(), 212.0)

    # Stage 11
    builder.road_stage(italy.marostica(), italy.zoldo_alto(), 150.0)

    # Stage 12
    builder.road_stage(italy.alleghe(), italy.rovereto(), 178.0)

    # Stage 13
    builder.road_stage(italy.mezzocorona(), italy.urtijei(), 218.0)

    # Stage 14
    builder.road_stage(italy.neumarkt(), italy.livigno(), 210.0)

    # Stage 15
    builder.road_stage(italy.villa_di_tirano(), italy.lissone(), 154.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.lissone(), italy.varazze(), 210.0)

    # Stage 17
    builder.road_stage(italy.varazze(), italy.limone_piemonte(), 194.0)

    # Stage 18
    builder.individual_time_trial(italy.chieri(), italy.turin(), 34.0)

    # Stage 19
    builder.mountain_stage(italy.savigliano())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 190.0)

    # Stage 20
    builder.road_stage(italy.albese_con_cassano(), italy.milan(), 119.0)

    return builder.build()

def giro2006():

    builder = TourOfItalyBuilder(2006,5,6)

    # Stage 1
    builder.out_and_back_individual_time_trial(belgium.seraing(), 6.2)

    # Stage 2
    builder.road_stage(belgium.mons(), belgium.charleroi(), 197.0)

    # Stage 3
    builder.road_stage(belgium.perwez(), belgium.namur(), 202.0)

    # Stage 4
    builder.road_stage(belgium.wanze(), belgium.hotton(), 193.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.team_time_trial(italy.piacenza(), italy.cremona(), 38.0)

    # Stage 6
    builder.road_stage(italy.busseto(), italy.forli(), 227.0)

    # Stage 7
    builder.road_stage(italy.cesena(), italy.saltara(), 236.0)

    # Stage 8
    builder.road_stage(italy.civitanova_marche(), italy.maielletta(), 171.0)

    # Stage 9
    builder.road_stage(italy.francavilla_al_mare(), italy.termoli(), 121.0)

    # Stage 10
    builder.road_stage(italy.termoli(), italy.peschici(), 187.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.out_and_back_individual_time_trial(italy.pontedera(), 50.0)

    # Stage 12
    builder.road_stage(italy.livorno(), italy.sestri_levante(), 171.0)

    # Stage 13
    builder.road_stage(italy.alessandria(), italy.la_thuile(), 218.0)

    # Stage 14
    builder.road_stage(italy.aosta(), italy.domodossola(), 223.0)

    # Stage 15
    builder.road_stage(italy.mergozzo(), italy.brescia(), 189.0)

    # Stage 16
    builder.road_stage(italy.rovato(), italy.trento(), 173.0)

    # Stage 17
    builder.road_stage(italy.tramin(), italy.plan_de_corones(), 133.0)

    # Stage 18
    builder.road_stage(italy.sillian(), italy.gemona_del_friuli(), 210.0)

    # Stage 19
    builder.road_stage(italy.pordenone(), italy.passo_di_san_pellegrino(), 224.0)

    # Stage 20
    builder.mountain_stage(italy.trento())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 211.0)

    # Stage 21
    builder.road_stage(italy.museo_del_ghisallo(), italy.milan(), 140.0)

    return builder.build()

def giro2007():

    builder = TourOfItalyBuilder(2007,5,12)

    # Stage 1
    builder.team_time_trial(italy.caprera(), italy.la_maddalena(), 25.6)

    # Stage 2
    builder.road_stage(italy.tempio_pausania(), italy.bosa(), 205.0)

    # Stage 3
    builder.road_stage(italy.barumini(), italy.cagliari(), 181.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.salerno(), italy.montevergine_di_mercogliano(), 153.0)

    # Stage 5
    builder.road_stage(italy.teano(), italy.frascati(), 173.0)

    # Stage 6
    builder.road_stage(italy.tivoli(), italy.spoleto(), 177.0)

    # Stage 7
    builder.road_stage(italy.spoleto(), italy.scarperia(), 254.0)

    # Stage 8
    builder.road_stage(italy.barberino_di_mugello(), italy.fiorano_modenese(), 200.0)

    # Stage 9
    builder.road_stage(italy.reggio_emilia(), italy.lido_di_camaiore(), 177.0)

    # Stage 10
    builder.road_stage(italy.camaiore(), italy.santuario_nostra_signora_della_guardia(), 250.0)

    # Stage 11
    builder.road_stage(italy.serraville_scrivia(), italy.pinerolo(), 198.0)

    # Stage 12
    builder.road_stage(italy.scalenghe(), france.briancon(), 163.0)

    # Stage 13
    builder.individual_time_trial(italy.biella(), italy.santuario_di_oropa(), 12.6)

    # Stage 14
    builder.road_stage(italy.cantu(), italy.bergamo(), 192.0)

    # Stage 15
    builder.road_stage(italy.trento(), italy.tre_cime_di_lavaredo(), 184.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.agordo(), austria.lienz(), 189.0)

    # Stage 17
    builder.mountain_stage(austria.lienz())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 142.0)

    # Stage 18
    builder.road_stage(italy.udine(), italy.riese_pio_x(), 203.0)

    # Stage 19
    builder.road_stage(italy.treviso(), italy.terme_di_comano(), 179.0)

    # Stage 20
    builder.individual_time_trial(italy.bardolino(), italy.verona(), 43.0)

    # Stage 21
    builder.road_stage(italy.vestone(), italy.milan(), 185.0)

    return builder.build()

def giro2008():

    builder = TourOfItalyBuilder(2008,5,10)

    # Stage 1
    builder.out_and_back_team_time_trial(italy.palermo(), 23.6)

    # Stage 2
    builder.road_stage(italy.cefalu(), italy.agrigento(), 207.0)

    # Stage 3
    builder.road_stage(italy.catania(), italy.milazzo(), 221.0)

    # Stage 4
    builder.road_stage(italy.pizzo_calabro(), italy.catanzaro_lungomare(), 183.0)

    # Stage 5
    builder.road_stage(italy.belvedere_marittimo(), italy.contursi_terme(), 203.0)

    # Stage 6
    builder.road_stage(italy.potenza(), italy.peschici(), 231.6)

    # Stage 7
    builder.road_stage(italy.vasto(), italy.pescocostanzo(), 180.0)

    # Stage 8
    builder.road_stage(italy.rivisondoli(), italy.tivoli(), 208.0)

    # Stage 9
    builder.road_stage(italy.civitavecchia(), italy.san_vincenzo(), 218.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.individual_time_trial(italy.pesaro(), italy.urbino(), 39.4)

    # Stage 11
    builder.road_stage(italy.urbania(), italy.cesena(), 199.0)

    # Stage 12
    builder.road_stage(italy.forli(), italy.carpi(), 172.0)

    # Stage 13
    builder.road_stage(italy.modena(), italy.cittadella(), 177.0)

    # Stage 14
    builder.road_stage(italy.verona(), italy.alpe_di_pampeago(), 195.0)

    # Stage 15
    builder.road_stage(italy.arabba(), italy.passo_fedaia(), 153.0)

    # Stage 16
    builder.individual_time_trial(italy.san_vigillo_di_marebbe(), italy.plan_de_corones(), 12.8)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.sondrio(), switzerland.locarno(), 146.0)

    # Stage 18
    builder.road_stage(switzerland.mendrisio(), italy.varese(), 147.0)

    # Stage 19
    builder.road_stage(italy.legnago(), italy.presolana(), 238.0)

    # Stage 20
    builder.road_stage(italy.rovetta(), italy.tirano(), 224.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.milan(), 28.5)

    return builder.build()

def giro2009():

    builder = TourOfItalyBuilder(2009,5,9)

    # Stage 1
    builder.out_and_back_team_time_trial(italy.venice_lido(), 20.5)

    # Stage 2
    builder.road_stage(italy.jesolo(), italy.trieste(), 156.0)

    # Stage 3
    builder.road_stage(italy.grado(), italy.valdobbiadene(), 198.0)

    # Stage 4
    builder.mountain_stage(italy.padua())
    builder.summit_finish(mountains.dolomites.san_martino_di_castrozza(), ColCategory.C2, 162.0)

    # Stage 5
    builder.road_stage(mountains.dolomites.san_martino_di_castrozza(), italy.alpe_di_siusi(), 125.0)

    # Stage 6
    builder.road_stage(italy.brixen(), austria.mayrhofen(), 248.0)

    # Stage 7
    builder.road_stage(austria.innsbruck(), italy.chiavenna(), 244.0)

    # Stage 8
    builder.road_stage(italy.morbegno(), italy.bergamo(), 209.0)

    # Stage 9
    builder.criterium(italy.milan(), 165.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.cuneo(), italy.pinerolo(), 262.0)

    # Stage 11
    builder.road_stage(italy.turin(), italy.arenzano(), 214.0)

    # Stage 12
    builder.individual_time_trial(italy.sestri_levante(), italy.riomaggiore(), 60.6)

    # Stage 13
    builder.road_stage(italy.lido_di_camaiore(), italy.florence(), 176.0)

    # Stage 14
    builder.road_stage(italy.campi_bisenzio(), italy.bologna(), 172.0)

    # Stage 15
    builder.road_stage(italy.forli(), italy.faenza(), 161.0)

    # Stage 16
    builder.road_stage(italy.pergola(), italy.monte_petrano(), 237.0)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(italy.chieti(), italy.blockhaus(), 83.0)

    # Stage 18
    builder.road_stage(italy.sulmona(), italy.benevento(), 182.0)

    # Stage 19
    builder.road_stage(italy.avellino(), italy.mount_vesuvius(), 164.0)

    # Stage 20
    builder.road_stage(italy.naples(), italy.anagi(), 203.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.rome(), 14.4)

    return builder.build()

def giro2010():

    builder = TourOfItalyBuilder(2010,5,8)

    # Stage 1
    builder.out_and_back_individual_time_trial(netherlands.amsterdam(), 8.4)

    # Stage 2
    builder.road_stage(netherlands.amsterdam(), netherlands.utrecht(), 209.0)

    # Stage 3
    builder.road_stage(netherlands.amsterdam(), netherlands.middleburg(), 224.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.team_time_trial(italy.savigliano(), italy.cuneo(), 32.5)

    # Stage 5
    builder.road_stage(italy.novara(), italy.novi_ligure(), 168.0)

    # Stage 6
    builder.road_stage(italy.fidenza(), italy.marina_di_carrara(), 166.0)

    # Stage 7
    builder.road_stage(italy.carrara(), italy.montalcino(), 215.0)

    # Stage 8
    builder.road_stage(italy.chianciano(), italy.monte_terminillo(), 189.0)

    # Stage 9
    builder.road_stage(italy.frosinone(), italy.cava_de_tirreni(), 188.0)

    # Stage 10
    builder.road_stage(italy.avellino(), italy.bitonto(), 220.0)

    # Stage 11
    builder.road_stage(italy.lucera(), italy.l_aquila(), 256.0)

    # Stage 12
    builder.road_stage(italy.citta_sant_angelo(), italy.porto_recanati(), 191.0)

    # Stage 13
    builder.road_stage(italy.porto_recanati(), italy.cesenatico(), 222.0)

    # Stage 14
    builder.mountain_stage(italy.ferrara())
    builder.summit_finish(italy.asolo_monte_grappa(), ColCategory.C1, 201.0)

    # Stage 15
    builder.mountain_stage(italy.mestre())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 161.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.individual_time_trial(italy.mareo(), italy.plan_de_corones(), 12.9)

    # Stage 17
    builder.road_stage(italy.bruneck(), italy.peio_terme(), 173.0)

    # Stage 18
    builder.road_stage(italy.levico_terme(), italy.brescia(), 151.0)

    # Stage 19
    builder.mountain_stage(italy.brescia())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 195.0)

    # Stage 20
    builder.road_stage(italy.bormio(), italy.passo_del_tonale(), 178.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.verona(), 15.3)

    return builder.build()

def giro2011():

    builder = TourOfItalyBuilder(2011,5,7)

    # Stage 1
    builder.team_time_trial(italy.veneria_reale(), italy.turin(), 19.3)

    # Stage 2
    builder.road_stage(italy.alba(), italy.parma(), 244.0)

    # Stage 3
    builder.road_stage(italy.reggio_emilia(), italy.rapallo(), 173.0)

    # Stage 4
    builder.road_stage(italy.quarto_dei_mille(), italy.livorno(), 216.0)

    # Stage 5
    builder.road_stage(italy.piombino(), italy.orvieto(), 191.0)

    # Stage 6
    builder.road_stage(italy.orvieto(), italy.fiuggi(), 216.0)

    # Stage 7
    builder.road_stage(italy.maddaloni(), italy.montevergine_di_mercogliano(), 110.0)

    # Stage 8
    builder.road_stage(italy.sapri(), italy.tropea(), 217.0)

    # Stage 9
    builder.road_stage(italy.messina(), italy.etna(), 169.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.termoli(), italy.teramo(), 159.0)

    # Stage 11
    builder.road_stage(italy.teramo(), italy.castelfidardo(), 142.0)

    # Stage 12
    builder.road_stage(italy.castelfidardo(), italy.ravenna(), 184.0)

    # Stage 13
    builder.road_stage(italy.spilimbergo(), austria.grossglockner(), 167.0)

    # Stage 14
    builder.mountain_stage(austria.lienz())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 170.0)

    # Stage 15
    builder.road_stage(italy.conegliano(), italy.gardeccia_val_di_fassa(), 229.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.individual_time_trial(italy.belluno(), italy.nevegal(), 12.7)

    # Stage 17
    builder.road_stage(italy.feltre(), italy.tirano(), 230.0)

    # Stage 18
    builder.road_stage(italy.morbegno(), italy.san_pellegrino_terme(), 151.0)

    # Stage 19
    builder.road_stage(italy.bergamo(), italy.macugnaga(), 209.0)

    # Stage 20
    builder.mountain_stage(italy.verbania())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 242.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.milan(), 26.0)

    return builder.build()

def giro2012():

    builder = TourOfItalyBuilder(2012,5,5)

    # Stage 1
    builder.out_and_back_individual_time_trial(denmark.herning(), 8.7)

    # Stage 2
    builder.criterium(denmark.herning(), 206.0)

    # Stage 3
    builder.criterium(denmark.horsens(), 190.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.out_and_back_team_time_trial(italy.verona(), 33.2)

    # Stage 5
    builder.road_stage(italy.modena(), italy.fano(), 209.0)

    # Stage 6
    builder.road_stage(italy.urbino(), italy.porto_sant_elpidio(), 210.0)

    # Stage 7
    builder.road_stage(italy.recanati(), italy.rocca_di_cambio(), 205.0)

    # Stage 8
    builder.road_stage(italy.sulmona(), italy.lago_laceno(), 229.0)

    # Stage 9
    builder.road_stage(italy.san_giorgio_del_sannio(), italy.frosinone(), 166.0)

    # Stage 10
    builder.road_stage(italy.civitavecchia(), italy.assisi(), 186.0)

    # Stage 11
    builder.road_stage(italy.assisi(), italy.montecatini_terme(), 255.0)

    # Stage 12
    builder.road_stage(italy.seravezza(), italy.sestri_levante(), 155.0)

    # Stage 13
    builder.road_stage(italy.savona(), italy.cervere(), 121.0)

    # Stage 14
    builder.mountain_stage(italy.cherasco())
    builder.summit_finish(mountains.alps.cervinia(), ColCategory.C1, 206.0)

    # Stage 15
    builder.road_stage(italy.busto_arsizio(), italy.lecco_pian_dei_resinelli(), 169.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.limone_sul_garda(), italy.pfalzen(), 173.0)

    # Stage 17
    builder.road_stage(italy.pfalzen(), italy.cortina_d_ampezzo(), 186.0)

    # Stage 18
    builder.road_stage(italy.san_vito_di_cadore(), italy.vedelago(), 149.0)

    # Stage 19
    builder.road_stage(italy.treviso(), italy.alpe_di_pampeago(), 198.0)

    # Stage 20
    builder.mountain_stage(italy.caldes_val_di_sole())
    builder.summit_finish(mountains.alps.passo_dello_stelvio(), ColCategory.C1, 219.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.milan(), 28.2)

    return builder.build()

def giro2013():

    builder = TourOfItalyBuilder(2013,5,4)

    # Stage 1
    builder.criterium(italy.naples(), 130.0)

    # Stage 2
    builder.team_time_trial(italy.ischia(), italy.forio(), 17.4)

    # Stage 3
    builder.road_stage(italy.sorrento(), italy.marina_di_ascea(), 222.0)

    # Stage 4
    builder.road_stage(italy.policastro_bussentino(), italy.serra_san_bruno(), 246.0)

    # Stage 5
    builder.road_stage(italy.cosenza(), italy.matera(), 203.0)

    # Stage 6
    builder.road_stage(italy.mola_di_bari(), italy.margherita_di_savoia(), 169.0)

    # Stage 7
    builder.road_stage(italy.san_salvo(), italy.pescara(), 177.0)

    # Stage 8
    builder.individual_time_trial(italy.gabicce_mare(), italy.saltara(), 54.8)

    # Stage 9
    builder.road_stage(italy.sansepolcro(), italy.florence(), 170.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.cordenons(), italy.altopiano_del_montasio(), 167.0)

    # Stage 11
    builder.road_stage(italy.cave_del_predil(), italy.erto_e_casso(), 182.0)

    # Stage 12
    builder.road_stage(italy.longarne(), italy.treviso(), 134.0)

    # Stage 13
    builder.road_stage(italy.busseto(), italy.cherasco(), 254.0)

    # Stage 14
    builder.road_stage(italy.cervere(), italy.bardonecchia(), 180.0)

    # Stage 15
    builder.road_stage(italy.cesana_torinese(), italy.col_du_galibier_valloire(), 149.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(france.valloire(), italy.ivrea(), 238.0)

    # Stage 17
    builder.road_stage(italy.caravaggio(), italy.vicenza(), 214.0)

    # Stage 18
    builder.individual_time_trial(italy.mori(), italy.polsa(), 20.6)

    # Stage 19
    builder.road_stage(italy.ponte_di_legno(), italy.martell(), 139.0)

    # Stage 20
    builder.road_stage(italy.schlanders(), italy.tre_cime_di_lavaredo(), 203.0)

    # Stage 21
    builder.road_stage(italy.riese_pio_x(), italy.brescia(), 197.0)

    return builder.build()

def giro2014():

    builder = TourOfItalyBuilder(2014,5,9)

    # Stage 1
    builder.out_and_back_team_time_trial(northern_ireland.belfast(), 21.7)

    # Stage 2
    builder.criterium(northern_ireland.belfast(), 219.0)

    # Stage 3
    builder.road_stage(northern_ireland.armagh(), ireland.dublin(), 187.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.giovinazzo(), italy.bari(), 112.0)

    # Stage 5
    builder.road_stage(italy.taranto(), italy.viggiano(), 203.0)

    # Stage 6
    builder.road_stage(italy.sassono(), italy.montecassino(), 257.0)

    # Stage 7
    builder.road_stage(italy.frosinone(), italy.foligno(), 211.0)

    # Stage 8
    builder.road_stage(italy.foligno(), italy.montecopiolo(), 179.0)

    # Stage 9
    builder.road_stage(italy.lugo(), italy.sestola(), 172.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.modena(), italy.salsomaggiore_terme(), 173.0)

    # Stage 11
    builder.road_stage(italy.collecchio(), italy.savona(), 249.0)

    # Stage 12
    builder.individual_time_trial(italy.barbaresco(), italy.barolo(), 41.9)

    # Stage 13
    builder.road_stage(italy.fossano(), italy.rivarolo_canavese(), 157.0)

    # Stage 14
    builder.road_stage(italy.agile(), italy.oropa(), 164.0)

    # Stage 15
    builder.road_stage(italy.valdengo(), italy.montecampione(), 225.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.ponte_di_legno(), italy.val_martello(), 139.0)

    # Stage 17
    builder.road_stage(italy.sarnonico(), italy.vittorio_veneto(), 208.0)

    # Stage 18
    builder.road_stage(italy.belluno(), italy.rifugio_panarotta(), 171.0)

    # Stage 19
    builder.individual_time_trial(italy.bassano_del_grappa(), italy.cima_grappa(), 26.8)

    # Stage 20
    builder.mountain_stage(italy.maniago())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 167.0)

    # Stage 21
    builder.road_stage(italy.gemona_del_friuli(), italy.trieste(), 172.0)

    return builder.build()

def giro2015():

    builder = TourOfItalyBuilder(2015,5,9)

    # Stage 1
    builder.team_time_trial(italy.san_lorenzo_al_mare(), italy.san_remo(), 17.6)

    # Stage 2
    builder.road_stage(italy.albenga(), italy.genoa(), 177.0)

    # Stage 3
    builder.road_stage(italy.rapallo(), italy.sestri_levante(), 136.0)

    # Stage 4
    builder.road_stage(italy.chiavari(), italy.la_spezia(), 150.0)

    # Stage 5
    builder.road_stage(italy.la_spezia(), italy.abetone(), 152.0)

    # Stage 6
    builder.road_stage(italy.montecatini_terme(), italy.castiglione_della_pescaia(), 183.0)

    # Stage 7
    builder.road_stage(italy.grosseto(), italy.fiuggi(), 264.0)

    # Stage 8
    builder.road_stage(italy.fiuggi(), italy.campitello_matese(), 186.0)

    # Stage 9
    builder.road_stage(italy.benevento(), italy.san_giorgio_del_sannio(), 224.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.civitanova_marche(), italy.forli(), 200.0)

    # Stage 11
    builder.road_stage(italy.forli(), italy.imola_autodromo_enzo_e_dino_ferrari(), 153.0)

    # Stage 12
    builder.road_stage(italy.imola(), italy.vicenza_monte_berico(), 190.0)

    # Stage 13
    builder.road_stage(italy.montecchio_maggiore(), italy.jesolo(), 147.0)

    # Stage 14
    builder.individual_time_trial(italy.treviso(), italy.valdobbiadene(), 59.4)

    # Stage 15
    builder.road_stage(italy.marostica(), italy.madonna_di_campiglio(), 165.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.mountain_stage(italy.pinzolo())
    builder.summit_finish(mountains.alps.aprica(), ColCategory.C3, 174.0)

    # Stage 17
    builder.road_stage(italy.tirano(), switzerland.lugano(), 134.0)

    # Stage 18
    builder.road_stage(switzerland.melide(), italy.verbania(), 170.0)

    # Stage 19
    builder.mountain_stage(italy.gravellona_toce())
    builder.summit_finish(mountains.alps.cervinia(), ColCategory.C1, 236.0)

    # Stage 20
    builder.mountain_stage(italy.saint_vincent())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 196.0)

    # Stage 21
    builder.road_stage(italy.turin(), italy.milan(), 185.0)

    return builder.build()

def giro2016():

    builder = TourOfItalyBuilder(2016,5,6)

    # Stage 1
    builder.out_and_back_individual_time_trial(netherlands.apeldoorn(), 9.8)

    # Stage 2
    builder.road_stage(netherlands.arnhem(), netherlands.nijmegen(), 190.0)

    # Stage 3
    builder.road_stage(netherlands.nijmegen(), netherlands.arnhem(), 190.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.catanzaro(), italy.praia_a_mare(), 200.0)

    # Stage 5
    builder.road_stage(italy.praia_a_mare(), italy.benevento(), 233.0)

    # Stage 6
    builder.road_stage(italy.ponte(), italy.roccaraso_aremogna(), 157.0)

    # Stage 7
    builder.road_stage(italy.sulmona(), italy.foligno(), 211.0)

    # Stage 8
    builder.road_stage(italy.foligno(), italy.arezzo(), 186.0)

    # Stage 9
    builder.out_and_back_individual_time_trial(italy.chianti_classico_stage(), 40.5)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.campi_bisenzio(), italy.sestola(), 219.0)

    # Stage 11
    builder.road_stage(italy.modena(), italy.asolo(), 227.0)

    # Stage 12
    builder.road_stage(italy.noale(), italy.bibione(), 182.0)

    # Stage 13
    builder.road_stage(italy.palmanova(), italy.cividale_del_fruili(), 170.0)

    # Stage 14
    builder.road_stage(italy.alpago(), italy.corvara(), 210.0)

    # Stage 15
    builder.individual_time_trial(italy.castelrotto(), italy.alpe_di_siusi_seiseralm(), 10.8)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.bressanone(), italy.andalo(), 132.0)

    # Stage 17
    builder.road_stage(italy.molveno(), italy.cassano_d_adda(), 196.0)

    # Stage 18
    builder.road_stage(italy.muggio(), italy.pinerolo(), 244.0)

    # Stage 19
    builder.mountain_stage(italy.pinerolo())
    builder.summit_finish(mountains.alps.risoul(), ColCategory.C1, 162.0)

    # Stage 20
    builder.road_stage(france.guillestre(), italy.sant_anna_di_vinadio(), 134.0)

    # Stage 21
    builder.road_stage(italy.cuneo(), italy.torino(), 163.0)

    return builder.build()

def giro2017():

    builder = TourOfItalyBuilder(2017,5,5)

    # Stage 1
    builder.road_stage(italy.alghero(), italy.olbia(), 206.0)

    # Stage 2
    builder.road_stage(italy.olbia(), italy.tortoli(), 221.0)

    # Stage 3
    builder.road_stage(italy.tortoli(), italy.cagliari(), 148.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.cefalu(), italy.etna(), 181.0)

    # Stage 5
    builder.road_stage(italy.pedara(), italy.messina(), 159.0)

    # Stage 6
    builder.road_stage(italy.reggio_calabria(), italy.terme_luigiane(), 217.0)

    # Stage 7
    builder.road_stage(italy.castrovillari(), italy.alberobello_valle_d_itria(), 224.0)

    # Stage 8
    builder.road_stage(italy.molfetta(), italy.peschici(), 189.0)

    # Stage 9
    builder.road_stage(italy.montenero_di_bisaccia(), italy.blockhaus(), 149.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.individual_time_trial(italy.foligno(), italy.montefalco(), 39.8)

    # Stage 11
    builder.road_stage(italy.firenze_ponte_a_ema(), italy.bagno_di_romagna(), 161.0)

    # Stage 12
    builder.road_stage(italy.forli(), italy.reggio_emilia(), 234.0)

    # Stage 13
    builder.road_stage(italy.reggio_emilia(), italy.tortona(), 167.0)

    # Stage 14
    builder.mountain_stage(italy.castellania())
    builder.summit_finish(italy.oropa("Biella"), ColCategory.C1, 131.0)

    # Stage 15
    builder.road_stage(italy.valdengo(), italy.bergamo(), 199.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.rovetta(), italy.bormio(), 222.0)

    # Stage 17
    builder.road_stage(italy.tirano(), italy.canazei("Val di Fassa"), 219.0)

    # Stage 18
    builder.road_stage(italy.moena("Val di Fassa"), italy.ortisei_st_ulrich_val_gardena(), 137.0)

    # Stage 19
    builder.road_stage(italy.san_candido(), italy.piancavallo("Monte Jafferau"), 191.0)

    # Stage 20
    builder.road_stage(italy.pordenone(), italy.asiago(), 190.0)

    # Stage 21
    builder.individual_time_trial(italy.monza(), italy.milan(), 29.3)

    return builder.build()

def giro2018():

    builder = TourOfItalyBuilder(2018,5,4)

    # Stage 1
    builder.out_and_back_individual_time_trial(israel.jerusalem(), 9.7)

    # Stage 2
    builder.road_stage(israel.haifa(), israel.tel_aviv(), 167.0)

    # Stage 3
    builder.road_stage(israel.beersheba(), israel.eilat(), 229.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(italy.catania(), italy.caltagirone(), 202.0)

    # Stage 5
    builder.road_stage(italy.agrigento(), italy.santa_ninfa_valle_del_belice(), 153.0)

    # Stage 6
    builder.mountain_stage(italy.caltanissetta())
    builder.summit_finish(mountains.sciliy.mount_etna(), ColCategory.C1, 169.0)

    # Stage 7
    builder.road_stage(italy.pizzo(), italy.praia_a_mare(), 159.0)

    # Stage 8
    builder.mountain_stage(italy.praia_a_mare())
    builder.summit_finish(mountains.appennines.montevergine_di_mercogliano(), ColCategory.C2, 209.0)

    # Stage 9
    builder.road_stage(italy.pesco_sannita(), italy.gran_sasso_d_italia_campo_imperatore(), 225.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.penne(), italy.gualdo_tadino(), 244.0)

    # Stage 11
    builder.road_stage(italy.assisi(), italy.osimo(), 156.0)

    # Stage 12
    builder.road_stage(italy.osimo(), italy.imola(), 214.0)

    # Stage 13
    builder.road_stage(italy.ferrara(), italy.nervesa_della_battaglia(), 180.0)

    # Stage 14
    builder.mountain_stage(italy.san_vito_al_tagliamento())
    builder.summit_finish(mountains.dolomites.monte_zoncolan(), ColCategory.C1, 186.0)

    # Stage 15
    builder.road_stage(italy.tolmezzo(), italy.sappada(), 176.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.individual_time_trial(italy.trento(), italy.rovereto(), 34.2)

    # Stage 17
    builder.road_stage(italy.riva_del_garda(), italy.iseo(), 149.5)

    # Stage 18
    builder.mountain_stage(italy.abbiategrasso())
    builder.summit_finish(mountains.alps.prato_nevoso(), ColCategory.C1, 196.0)

    # Stage 19
    builder.mountain_stage(italy.veneria_reale())
    builder.summit_finish(mountains.alps.bardonecchia_monte_jafferau(), ColCategory.C1, 185.0)

    # Stage 20
    builder.mountain_stage(italy.susa())
    builder.summit_finish(mountains.alps.cervinia(), ColCategory.C1, 214.0)

    # Stage 21
    builder.criterium(italy.rome(), 115.0)

    return builder.build()

def giro2019():

    builder = TourOfItalyBuilder(2019,5,11)

    # Stage 1
    builder.individual_time_trial(italy.bologna(), italy.san_luca(), 8.0)

    # Stage 2
    builder.road_stage(italy.bologna(), italy.fucecchio(), 205.0)

    # Stage 3
    builder.road_stage(italy.vinci(), italy.orbetello(), 220.0)

    # Stage 4
    builder.road_stage(italy.orbetello(), italy.frascati(), 235.0)

    # Stage 5
    builder.road_stage(italy.frascati(), italy.terracina(), 140.0)

    # Stage 6
    builder.road_stage(italy.cassino(), italy.san_giovanni_rotondo(), 238.0)

    # Stage 7
    builder.road_stage(italy.vasto(), italy.l_aquila(), 185.0)

    # Stage 8
    builder.road_stage(italy.tortoreto_lido(), italy.pesaro(), 239.0)

    # Stage 9
    builder.individual_time_trial(italy.riccione(), san_marino.san_marino(), 34.8)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(italy.ravenna(), italy.modena(), 145.0)

    # Stage 11
    builder.road_stage(italy.carpi(), italy.novi_ligure(), 221.0)

    # Stage 12
    builder.road_stage(italy.cuneo(), italy.pinerolo(), 158.0)

    # Stage 13
    builder.mountain_stage(italy.pinerolo())
    builder.summit_finish(mountains.alps.ceresole_reale(), ColCategory.C1, 196.0)

    # Stage 14
    builder.road_stage(italy.saint_vincent(), italy.courmayeur_skyway_monte_bianco(), 131.0)

    # Stage 15
    builder.road_stage(italy.ivrea(), italy.como(), 232.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(italy.lovere(), italy.ponte_di_legno(), 194.0)

    # Stage 17
    builder.mountain_stage(italy.commezzadura())
    builder.summit_finish(italy.anterselva_antholz(), ColCategory.C3, 181.0)

    # Stage 18
    builder.road_stage(italy.valdaora(), italy.santa_maria_di_sala(), 222.0)

    # Stage 19
    builder.mountain_stage(italy.treviso())
    builder.summit_finish(mountains.dolomites.san_martino_di_castrozza(), ColCategory.C2, 151.0)

    # Stage 20
    builder.mountain_stage(italy.feltre())
    builder.summit_finish(mountains.dolomites.monte_avena(), ColCategory.C1, 194.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(italy.verona(), 17.0)

    return builder.build()

