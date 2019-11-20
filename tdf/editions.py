import country
import andorra
import belgium
import france
import germany
import ireland
import italy
import luxembourg
import monaco
import mountains.alps
import mountains.massif_amorican
import mountains.massif_central
import mountains.pyrenees
import mountains.vosges
import netherlands
import spain
import switzerland
import united_kingdom
import west_germany
from col                import ColCategory
from stage_race         import TourDeFrance
from stage_race_builder import NonConsecutiveStageRaceBuilder, TourDeFranceBuilder

def tdf1903():

    paris     = france.paris()
    lyon      = france.lyon()
    marseille = france.marseille()
    toulouse  = france.toulouse()
    bordeaux  = france.bordeaux()
    nantes    = france.nantes()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1903)
    builder.road_stage(7, 1, paris, lyon, 467)
    builder.road_stage(7, 5, lyon, marseille, 374)
    builder.road_stage(7, 8, marseille, toulouse, 423)
    builder.road_stage(7, 12, toulouse, bordeaux, 268)
    builder.road_stage(7, 13, bordeaux, nantes, 425)
    builder.road_stage(7, 18, nantes, paris, 471)
    return builder.build()

def tdf1904():

    montgeron = france.montgeron()
    lyon      = france.lyon()
    marseille = france.marseille()
    toulouse  = france.toulouse()
    bordeaux  = france.bordeaux()
    nantes    = france.nantes()
    paris     = france.paris()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1904)
    builder.road_stage(7, 2, montgeron, lyon, 467)
    builder.road_stage(7, 9, lyon, marseille, 374)
    builder.road_stage(7, 13, marseille, toulouse, 424)
    builder.road_stage(7, 17, toulouse, bordeaux, 268)
    builder.road_stage(7, 20, bordeaux, nantes, 425)
    builder.road_stage(7, 23, nantes, paris, 471)
    return builder.build()

def tdf1905():

    paris       = france.paris()
    nancy       = france.nancy()
    besancon    = france.besancon()
    grenoble    = france.grenoble()
    toulon      = france.toulon()
    nimes       = france.nimes()
    toulouse    = france.toulouse()
    bordeaux    = france.bordeaux()
    la_rochelle = france.la_rochelle()
    rennes      = france.rennes()
    caen        = france.caen()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1905)
    builder.road_stage(7, 9, paris, nancy, 340)
    builder.road_stage(7, 11, nancy, besancon, 299)
    builder.road_stage(7, 14, besancon, grenoble, 327)
    builder.road_stage(7, 16, grenoble, toulon, 348)
    builder.road_stage(7, 18, toulon, nimes, 192)
    builder.road_stage(7, 20, nimes, toulouse, 307)
    builder.road_stage(7, 22, toulouse, bordeaux, 268)
    builder.road_stage(7, 24, bordeaux, la_rochelle, 257)
    builder.road_stage(7, 26, la_rochelle, rennes, 263)
    builder.road_stage(7, 28, rennes, caen, 167)
    builder.road_stage(7, 29, caen, paris, 253)
    return builder.build()

def tdf1906():
    paris       = france.paris()
    lille       = france.lille()
    douai       = france.douai()
    nancy       = france.nancy()
    dijon       = france.dijon()
    grenoble    = france.grenoble()
    nice        = france.nice()
    marseille   = france.marseille()
    toulouse    = france.toulouse()
    bayonne     = france.bayonne()
    bordeaux    = france.bordeaux()
    nantes      = france.nantes()
    brest       = france.brest()
    caen        = france.caen()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1906)
    builder.road_stage(7, 4, paris, lille, 275.0)
    builder.road_stage(7, 6, douai, nancy, 400.0)
    builder.road_stage(7, 8, nancy, dijon, 416.0)
    builder.road_stage(7, 10, dijon, grenoble, 311.0)
    builder.road_stage(7, 12, grenoble, nice, 345.0)
    builder.road_stage(7, 14, nice, marseille, 292.0)
    builder.road_stage(7, 16, marseille, toulouse, 480.0)
    builder.road_stage(7, 18, toulouse, bayonne, 300.0)
    builder.road_stage(7, 20, bayonne, bordeaux, 338.0)
    builder.road_stage(7, 22, bordeaux, nantes, 391.0)
    builder.road_stage(7, 24, nantes, brest, 321.0)
    builder.road_stage(7, 26, brest, caen, 415.0)
    builder.road_stage(7, 29, caen, paris, 259.0)
    return builder.build()

def tdf1907():

    bayonne  = france.bayonne()
    belfort  = france.belfort()
    bordeaux = france.bordeaux()
    brest    = france.brest()
    caen     = france.caen()
    grenoble = france.grenoble()
    lyon     = france.lyon()
    nantes   = france.nantes()
    nice     = france.nice()
    nimes    = france.nimes()
    metz     = france.metz()
    paris    = france.paris()
    roubaix  = france.roubaix()
    toulouse = france.toulouse()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1907)
    builder.road_stage(7, 8, paris, roubaix, 272)
    builder.road_stage(7, 10, roubaix, metz, 398)
    builder.road_stage(7, 12, metz, belfort, 259)
    builder.road_stage(7, 14, belfort, lyon, 309)
    builder.road_stage(7, 16, lyon, grenoble, 311)
    builder.road_stage(7, 18, grenoble, nice, 345)
    builder.road_stage(7, 20, nice, nimes, 345)
    builder.road_stage(7, 22, nimes, toulouse, 303)
    builder.road_stage(7, 24, toulouse, bayonne, 299)
    builder.road_stage(7, 26, bayonne, bordeaux, 269)
    builder.road_stage(7, 28, bordeaux, nantes, 391)
    builder.road_stage(7, 30, nantes, brest, 321)
    builder.road_stage(8, 1, brest, caen, 415)
    builder.road_stage(8, 4, caen, paris, 251)
    return builder.build()

def tdf1908():

    bayonne  = france.bayonne()
    belfort  = france.belfort()
    bordeaux = france.bordeaux()
    brest    = france.brest()
    caen     = france.caen()
    grenoble = france.grenoble()
    lyon     = france.lyon()
    nantes   = france.nantes()
    nice     = france.nice()
    nimes    = france.nimes()
    metz     = france.metz()
    paris    = france.paris()
    roubaix  = france.roubaix()
    toulouse = france.toulouse()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1908)
    builder.road_stage(7, 13, paris, roubaix, 272)
    builder.road_stage(7, 15, roubaix, metz, 398)
    builder.road_stage(7, 17, metz, belfort, 259)
    builder.road_stage(7, 19, belfort, lyon, 309)
    builder.road_stage(7, 21, lyon, grenoble, 311)
    builder.road_stage(7, 23, grenoble, nice, 345)
    builder.road_stage(7, 25, nice, nimes, 354)
    builder.road_stage(7, 27, nimes, toulouse, 303)
    builder.road_stage(7, 29, toulouse, bayonne, 299)
    builder.road_stage(7, 31, bayonne, bordeaux, 269)
    builder.road_stage(8,  2, bordeaux, nantes, 391)
    builder.road_stage(8,  4, nantes, brest, 321)
    builder.road_stage(8,  6, brest, caen, 415)
    builder.road_stage(8,  9, caen, paris, 251)
    return builder.build()

def tdf1909():

    bayonne  = france.bayonne()
    belfort  = france.belfort()
    bordeaux = france.bordeaux()
    brest    = france.brest()
    caen     = france.caen()
    grenoble = france.grenoble()
    lyon     = france.lyon()
    nantes   = france.nantes()
    nice     = france.nice()
    nimes    = france.nimes()
    metz     = france.metz()
    paris    = france.paris()
    roubaix  = france.roubaix()
    toulouse = france.toulouse()

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1908)
    builder.road_stage(7,  5, paris, roubaix, 272)
    builder.road_stage(7,  7, roubaix, metz, 398)
    builder.road_stage(7,  9, metz, belfort, 259)
    builder.road_stage(7, 11, belfort, lyon, 309)
    builder.road_stage(7, 13, lyon, grenoble, 311)
    builder.road_stage(7, 15, grenoble, nice, 346)
    builder.road_stage(7, 17, nice, nimes, 345)
    builder.road_stage(7, 19, nimes, toulouse, 303)
    builder.road_stage(7, 21, toulouse, bayonne, 299)
    builder.road_stage(7, 23, bayonne, bordeaux, 269)
    builder.road_stage(7, 25, bordeaux, nantes, 391)
    builder.road_stage(7, 27, nantes, brest, 321)
    builder.road_stage(7, 29, brest, caen, 424)
    builder.road_stage(8,  1, caen, paris, 250)
    return builder.build()

def tdf1910():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1910)
    builder.road_stage(7, 3, france.paris(), france.roubaix(), 269.0)
    builder.road_stage(7, 5, france.roubaix(), france.metz(), 398.0)
    builder.road_stage(7, 7, france.metz(), france.belfort(), 259.0)
    builder.road_stage(7, 9, france.belfort(), france.lyon(), 309.0)
    builder.road_stage(7, 11, france.lyon(), france.grenoble(), 311.0)
    builder.road_stage(7, 13, france.grenoble(), france.nice(), 345.0)
    builder.road_stage(7, 17, france.nice(), france.nimes(), 345.0)
    builder.road_stage(7, 19, france.nimes(), france.perpignan(), 216.0)
    builder.road_stage(7, 21, france.perpignan(), france.luchon(), 289.0)
    builder.road_stage(7, 23, france.bayonne(), france.bordeaux(), 269.0)
    builder.road_stage(7, 25, france.bordeaux(), france.nantes(), 391.0)
    builder.road_stage(7, 27, france.nantes(), france.brest(), 321.0)
    builder.road_stage(7, 29, france.brest(), france.caen(), 424.0)
    builder.road_stage(7, 31, france.caen(), france.paris(), 262.0)
    return builder.build()

def tdf1911():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1911)
    builder.road_stage(7, 2, france.paris(), france.dunkerque(), 351.0)
    builder.road_stage(7, 4, france.dunkerque(), france.longwy(), 388.0)
    builder.road_stage(7, 6, france.longwy(), france.belfort(), 331.0)
    builder.road_stage(7, 8, france.belfort(), france.chamonix(), 344.0)
    builder.road_stage(7, 10, france.chamonix(), france.grenoble(), 366.0)
    builder.road_stage(7, 12, france.grenoble(), france.nice(), 348.0)
    builder.road_stage(7, 14, france.nice(), france.marseille(), 334.0)
    builder.road_stage(7, 16, france.marseille(), france.perpignan(), 335.0)
    builder.road_stage(7, 18, france.perpignan(), france.luchon(), 289.0)
    builder.road_stage(7, 20, france.luchon(), france.bayonne(), 326.0)
    builder.road_stage(7, 22, france.bayonne(), france.la_rochelle(), 379.0)
    builder.road_stage(7, 23, france.la_rochelle(), france.brest(), 470.0)
    builder.road_stage(7, 26, france.brest(), france.cherbourg(), 405.0)
    builder.road_stage(7, 28, france.cherbourg(), france.le_havre(), 361.0)
    builder.road_stage(7, 30, france.le_havre(), france.paris(), 317.0)
    return builder.build()

def tdf1912():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1912)
    builder.road_stage(6, 30, france.paris(), france.dunkerque(), 351.0)
    builder.road_stage(7, 2, france.dunkerque(), france.longwy(), 388.0)
    builder.road_stage(7, 4, france.longwy(), france.belfort(), 331.0)
    builder.road_stage(7, 6, france.belfort(), france.chamonix(), 344.0)
    builder.road_stage(7, 8, france.chamonix(), france.grenoble(), 366.0)
    builder.road_stage(7, 10, france.grenoble(), france.nice(), 323.0)
    builder.road_stage(7, 12, france.nice(), france.marseille(), 334.0)
    builder.road_stage(7, 14, france.marseille(), france.perpignan(), 335.0)
    builder.road_stage(7, 16, france.perpignan(), france.luchon(), 289.0)
    builder.road_stage(7, 18, france.luchon(), france.bayonne(), 326.0)
    builder.road_stage(7, 20, france.bayonne(), france.la_rochelle(), 379.0)
    builder.road_stage(7, 21, france.la_rochelle(), france.brest(), 470.0)
    builder.road_stage(7, 24, france.brest(), france.cherbourg(), 405.0)
    builder.road_stage(7, 26, france.cherbourg(), france.le_havre(), 361.0)
    builder.road_stage(7, 28, france.le_havre(), france.paris(), 317.0)
    return builder.build()

def tdf1913():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1913)
    builder.road_stage(6, 29, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(7, 1, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(7, 3, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 5, france.brest(), france.la_rochelle(), 470.0)
    builder.road_stage(7, 7, france.la_rochelle(), france.bayonne(), 379.0)
    builder.road_stage(7, 9, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 11, france.luchon(), france.perpignan(), 324.0)
    builder.road_stage(7, 13, france.perpignan(), france.aix_en_provence(), 325.0)
    builder.road_stage(7, 15, france.aix_en_provence(), france.nice(), 356.0)
    builder.road_stage(7, 17, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 19, france.grenoble(), switzerland.geneva(), 325.0)
    builder.road_stage(7, 21, switzerland.geneva(), france.belfort(), 335.0)
    builder.road_stage(7, 23, france.belfort(), france.longwy(), 325.0)
    builder.road_stage(7, 25, france.longwy(), france.dunkerque(), 393.0)
    builder.road_stage(7, 27, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1914():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1914)
    builder.road_stage(6, 28, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(6, 30, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(7, 2, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 4, france.brest(), france.la_rochelle(), 470.0)
    builder.road_stage(7, 6, france.la_rochelle(), france.bayonne(), 376.0)
    builder.road_stage(7, 8, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 10, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 12, france.perpignan(), france.marseille(), 370.0)
    builder.road_stage(7, 14, france.marseille(), france.nice(), 338.0)
    builder.road_stage(7, 16, france.nice(), france.grenoble(), 323.0)
    builder.road_stage(7, 18, france.grenoble(), switzerland.geneva(), 325.0)
    builder.road_stage(7, 20, switzerland.geneva(), france.belfort(), 325.0)
    builder.road_stage(7, 22, france.belfort(), france.longwy(), 325.0)
    builder.road_stage(7, 24, france.longwy(), france.dunkerque(), 390.0)
    builder.road_stage(7, 26, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1919():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1919)
    builder.road_stage(6, 29, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(7, 1, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(7, 3, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 5, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 7, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 9, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 11, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 13, france.perpignan(), france.marseille(), 370.0)
    builder.road_stage(7, 15, france.marseille(), france.nice(), 338.0)
    builder.road_stage(7, 17, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 19, france.grenoble(), switzerland.geneva(), 325.0)
    builder.road_stage(7, 21, switzerland.geneva(), france.strasbourg(), 371.0)
    builder.road_stage(7, 23, france.strasbourg(), france.metz(), 315.0)
    builder.road_stage(7, 25, france.metz(), france.dunkerque(), 468.0)
    builder.road_stage(7, 27, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1920():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1920)
    builder.road_stage(6, 27, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(6, 29, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(7, 1, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 3, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 5, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 7, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 9, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 11, france.perpignan(), france.aix_en_provence(), 325.0)
    builder.road_stage(7, 14, france.aix_en_provence(), france.nice(), 356.0)
    builder.road_stage(7, 16, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 18, france.grenoble(), france.gex(), 362.0)
    builder.road_stage(7, 20, france.gex(), france.strasbourg(), 354.0)
    builder.road_stage(7, 22, france.strasbourg(), france.metz(), 300.0)
    builder.road_stage(7, 24, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 27, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1921():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1921)
    builder.road_stage(6, 26, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(6, 28, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(6, 30, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 2, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 4, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 6, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 8, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 10, france.perpignan(), france.toulon(), 411.0)
    builder.road_stage(7, 12, france.toulon(), france.nice(), 272.0)
    builder.road_stage(7, 14, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 16, france.grenoble(), switzerland.geneva(), 325.0)
    builder.road_stage(7, 18, switzerland.geneva(), france.strasbourg(), 371.0)
    builder.road_stage(7, 20, france.strasbourg(), france.metz(), 300.0)
    builder.road_stage(7, 22, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 24, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1922():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1922)
    builder.road_stage(6, 25, france.paris(), france.le_havre(), 388.0)
    builder.road_stage(6, 27, france.le_havre(), france.cherbourg(), 364.0)
    builder.road_stage(6, 29, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 1, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 3, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 5, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 7, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 9, france.perpignan(), france.toulon(), 411.0)
    builder.road_stage(7, 11, france.toulon(), france.nice(), 284.0)
    builder.road_stage(7, 13, france.nice(), france.briancon(), 274.0)
    builder.road_stage(7, 15, france.briancon(), switzerland.geneva(), 260.0)
    builder.road_stage(7, 17, switzerland.geneva(), france.strasbourg(), 371.0)
    builder.road_stage(7, 19, france.strasbourg(), france.metz(), 300.0)
    builder.road_stage(7, 21, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 23, france.dunkerque(), france.paris(), 340.0)
    return builder.build()

def tdf1923():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1923)
    builder.road_stage(6, 24, france.paris(), france.le_havre(), 381.0)
    builder.road_stage(6, 26, france.le_havre(), france.cherbourg(), 371.0)
    builder.road_stage(6, 28, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(6, 30, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 2, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 4, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 6, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 8, france.perpignan(), france.toulon(), 427.0)
    builder.road_stage(7, 10, france.toulon(), france.nice(), 281.0)
    builder.road_stage(7, 12, france.nice(), france.briancon(), 275.0)
    builder.road_stage(7, 14, france.briancon(), switzerland.geneva(), 260.0)
    builder.road_stage(7, 16, switzerland.geneva(), france.strasbourg(), 377.0)
    builder.road_stage(7, 18, france.strasbourg(), france.metz(), 300.0)
    builder.road_stage(7, 20, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 22, france.dunkerque(), france.paris(), 343.0)
    return builder.build()

def tdf1924():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1924)
    builder.road_stage(6, 22, france.paris(), france.le_havre(), 381.0)
    builder.road_stage(6, 24, france.le_havre(), france.cherbourg(), 371.0)
    builder.road_stage(6, 26, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(6, 28, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(6, 30, france.les_sables_d_olonne(), france.bayonne(), 482.0)
    builder.road_stage(7, 2, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 4, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 6, france.perpignan(), france.toulon(), 427.0)
    builder.road_stage(7, 8, france.toulon(), france.nice(), 280.0)
    builder.road_stage(7, 10, france.nice(), france.briancon(), 275.0)
    builder.road_stage(7, 12, france.briancon(), france.gex(), 307.0)
    builder.road_stage(7, 14, france.gex(), france.strasbourg(), 360.0)
    builder.road_stage(7, 16, france.strasbourg(), france.metz(), 300.0)
    builder.road_stage(7, 18, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 20, france.dunkerque(), france.paris(), 343.0)
    return builder.build()

def tdf1925():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1925)
    builder.road_stage(6, 21, france.paris(), france.le_havre(), 340.0)
    builder.road_stage(6, 23, france.le_havre(), france.cherbourg(), 371.0)
    builder.road_stage(6, 25, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(6, 26, france.brest(), france.vannes(), 208.0)
    builder.road_stage(6, 27, france.vannes(), france.les_sables_d_olonne(), 204.0)
    builder.road_stage(6, 28, france.les_sables_d_olonne(), france.bordeaux(), 293.0)
    builder.road_stage(6, 29, france.bordeaux(), france.bayonne(), 189.0)
    builder.road_stage(7, 1, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 3, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 4, france.perpignan(), france.nimes(), 215.0)
    builder.road_stage(7, 5, france.nimes(), france.toulon(), 215.0)
    builder.road_stage(7, 7, france.toulon(), france.nice(), 280.0)
    builder.road_stage(7, 9, france.nice(), france.briancon(), 275.0)
    builder.road_stage(7, 11, france.briancon(), france.evian(), 303.0)
    builder.road_stage(7, 13, france.evian(), france.mulhouse(), 373.0)
    builder.road_stage(7, 15, france.mulhouse(), france.metz(), 334.0)
    builder.road_stage(7, 17, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(7, 19, france.dunkerque(), france.paris(), 343.0)
    return builder.build()

def tdf1926():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1926)
    builder.road_stage(6, 20, france.evian(), france.mulhouse(), 373.0)
    builder.road_stage(6, 22, france.mulhouse(), france.metz(), 334.0)
    builder.road_stage(6, 24, france.metz(), france.dunkerque(), 433.0)
    builder.road_stage(6, 26, france.dunkerque(), france.le_havre(), 361.0)
    builder.road_stage(6, 28, france.le_havre(), france.cherbourg(), 357.0)
    builder.road_stage(6, 30, france.cherbourg(), france.brest(), 405.0)
    builder.road_stage(7, 2, france.brest(), france.les_sables_d_olonne(), 412.0)
    builder.road_stage(7, 3, france.les_sables_d_olonne(), france.bordeaux(), 285.0)
    builder.road_stage(7, 4, france.bordeaux(), france.bayonne(), 189.0)
    builder.road_stage(7, 6, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 8, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 10, france.perpignan(), france.toulon(), 427.0)
    builder.road_stage(7, 12, france.toulon(), france.nice(), 280.0)
    builder.road_stage(7, 14, france.nice(), france.briancon(), 275.0)
    builder.road_stage(7, 16, france.briancon(), france.evian(), 303.0)
    builder.road_stage(7, 17, france.evian(), france.dijon(), 321.0)
    builder.road_stage(7, 18, france.dijon(), france.paris(), 341.0)
    return builder.build()

def tdf1927():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1927)
    builder.team_time_trial(6, 19, france.paris(), france.dieppe(), 180.0)
    builder.team_time_trial(6, 20, france.dieppe(), france.le_havre(), 103.0)
    builder.team_time_trial(6, 21, france.le_havre(), france.caen(), 225.0)
    builder.team_time_trial(6, 22, france.caen(), france.cherbourg(), 140.0)
    builder.team_time_trial(6, 23, france.cherbourg(), france.dinan(), 199.0)
    builder.team_time_trial(6, 24, france.dinan(), france.brest(), 206.0)
    builder.team_time_trial(6, 25, france.brest(), france.vannes(), 207.0)
    builder.team_time_trial(6, 26, france.vannes(), france.les_sables_d_olonne(), 204.0)
    builder.team_time_trial(6, 27, france.les_sables_d_olonne(), france.bordeaux(), 285.0)
    builder.road_stage(6, 28, france.bordeaux(), france.bayonne(), 189.0)
    builder.road_stage(6, 30, france.bayonne(), france.luchon(), 326.0)
    builder.road_stage(7, 2, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 4, france.perpignan(), france.marseille(), 360.0)
    builder.team_time_trial(7, 5, france.marseille(), france.toulon(), 120.0)
    builder.road_stage(7, 6, france.toulon(), france.nice(), 220.0)
    builder.road_stage(7, 8, france.nice(), france.briancon(), 275.0)
    builder.road_stage(7, 9, france.briancon(), france.evian(), 283.0)
    builder.team_time_trial(7, 11, france.evian(), france.pontarlier(), 213.0)
    builder.team_time_trial(7, 12, france.pontarlier(), france.belfort(), 119.0)
    builder.team_time_trial(7, 13, france.belfort(), france.strasbourg(), 145.0)
    builder.team_time_trial(7, 14, france.strasbourg(), france.metz(), 165.0)
    builder.team_time_trial(7, 15, france.metz(), france.charleville(), 159.0)
    builder.team_time_trial(7, 16, france.charleville(), france.dunkerque(), 270.0)
    builder.road_stage(7, 17, france.dunkerque(), france.paris(), 344.0)
    return builder.build()

def tdf1928():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1928)
    builder.team_time_trial(6, 17, france.paris(), france.caen(), 207.0)
    builder.team_time_trial(6, 18, france.caen(), france.cherbourg(), 140.0)
    builder.team_time_trial(6, 19, france.cherbourg(), france.dinan(), 199.0)
    builder.team_time_trial(6, 20, france.dinan(), france.brest(), 206.0)
    builder.team_time_trial(6, 21, france.brest(), france.vannes(), 208.0)
    builder.team_time_trial(6, 22, france.vannes(), france.les_sables_d_olonne(), 204.0)
    builder.team_time_trial(6, 23, france.les_sables_d_olonne(), france.bordeaux(), 285.0)
    builder.team_time_trial(6, 24, france.bordeaux(), france.hendaye(), 225.0)
    builder.road_stage(6, 26, france.hendaye(), france.luchon(), 387.0)
    builder.road_stage(6, 28, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(6, 30, france.perpignan(), france.marseille(), 363.0)
    builder.road_stage(7, 2, france.marseille(), france.nice(), 330.0)
    builder.road_stage(7, 4, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 6, france.grenoble(), france.evian(), 329.0)
    builder.team_time_trial(7, 8, france.evian(), france.pontarlier(), 213.0)
    builder.team_time_trial(7, 9, france.pontarlier(), france.belfort(), 119.0)
    builder.team_time_trial(7, 10, france.belfort(), france.strasbourg(), 145.0)
    builder.team_time_trial(7, 11, france.strasbourg(), france.metz(), 165.0)
    builder.team_time_trial(7, 12, france.metz(), france.charleville(), 159.0)
    builder.team_time_trial(7, 13, france.charleville(), france.malo_les_bains(), 271.0)
    builder.team_time_trial(7, 14, france.malo_les_bains(), france.dunkerque(), 234.0)
    builder.road_stage(7, 15, france.dieppe(), france.paris(), 331.0)
    return builder.build()

def tdf1929():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1929)
    builder.road_stage(6, 30, france.paris(), france.caen(), 206.0)
    builder.road_stage(7, 1, france.caen(), france.cherbourg(), 140.0)
    builder.road_stage(7, 2, france.cherbourg(), france.dinan(), 199.0)
    builder.road_stage(7, 3, france.dinan(), france.brest(), 206.0)
    builder.road_stage(7, 4, france.brest(), france.vannes(), 208.0)
    builder.road_stage(7, 5, france.vannes(), france.les_sables_d_olonne(), 206.0)
    builder.road_stage(7, 6, france.les_sables_d_olonne(), france.bordeaux(), 285.0)
    builder.road_stage(7, 7, france.bordeaux(), france.bayonne(), 182.0)
    builder.road_stage(7, 9, france.bayonne(), france.luchon(), 363.0)
    builder.road_stage(7, 11, france.luchon(), france.perpignan(), 323.0)
    builder.road_stage(7, 13, france.perpignan(), france.marseille(), 366.0)
    builder.team_time_trial(7, 15, france.marseille(), france.cannes(), 191.0)
    builder.road_stage(7, 16, france.cannes(), france.nice(), 133.0)
    builder.road_stage(7, 18, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 20, france.grenoble(), france.evian(), 329.0)
    builder.road_stage(7, 22, france.evian(), france.belfort(), 283.0)
    builder.road_stage(7, 23, france.belfort(), france.strasbourg(), 145.0)
    builder.road_stage(7, 24, france.strasbourg(), france.metz(), 165.0)
    builder.team_time_trial(7, 25, france.metz(), france.charleville(), 159.0)
    builder.team_time_trial(7, 26, france.charleville(), france.malo_les_bains(), 270.0)
    builder.road_stage(7, 27, france.malo_les_bains(), france.dunkerque(), 234.0)
    builder.road_stage(7, 28, france.dieppe(), france.paris(), 332.0)
    return builder.build()

def tdf1930():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1930)
    builder.road_stage(7, 2, france.paris(), france.caen(), 206.0)
    builder.road_stage(7, 3, france.caen(), france.dinan(), 203.0)
    builder.road_stage(7, 4, france.dinan(), france.brest(), 206.0)
    builder.road_stage(7, 5, france.brest(), france.vannes(), 210.0)
    builder.road_stage(7, 6, france.vannes(), france.les_sables_d_olonne(), 202.0)
    builder.road_stage(7, 7, france.les_sables_d_olonne(), france.bordeaux(), 285.0)
    builder.road_stage(7, 8, france.bordeaux(), france.hendaye(), 222.0)
    builder.road_stage(7, 9, france.hendaye(), france.pau(), 146.0)
    builder.road_stage(7, 10, france.pau(), france.luchon(), 231.0)
    builder.road_stage(7, 12, france.luchon(), france.perpignan(), 322.0)
    builder.road_stage(7, 14, france.perpignan(), france.montpellier(), 164.0)
    builder.road_stage(7, 15, france.montpellier(), france.marseille(), 209.0)
    builder.road_stage(7, 16, france.marseille(), france.cannes(), 181.0)
    builder.road_stage(7, 17, france.cannes(), france.nice(), 132.0)
    builder.road_stage(7, 19, france.nice(), france.grenoble(), 333.0)
    builder.road_stage(7, 21, france.grenoble(), france.evian(), 331.0)
    builder.road_stage(7, 23, france.evian(), france.belfort(), 282.0)
    builder.road_stage(7, 24, france.belfort(), france.metz(), 223.0)
    builder.road_stage(7, 25, france.metz(), france.charleville(), 159.0)
    builder.road_stage(7, 26, france.charleville(), france.malo_les_bains(), 271.0)
    builder.road_stage(7, 28, france.malo_les_bains(), france.paris(), 300.0)
    return builder.build()

def tdf1931():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1931)
    builder.road_stage(6, 30, france.paris(), france.caen(), 208.0)
    builder.road_stage(7, 1, france.caen(), france.dinan(), 212.0)
    builder.road_stage(7, 2, france.dinan(), france.brest(), 206.0)
    builder.road_stage(7, 3, france.brest(), france.vannes(), 211.0)
    builder.road_stage(7, 4, france.vannes(), france.les_sables_d_olonne(), 202.0)
    builder.road_stage(7, 5, france.les_sables_d_olonne(), france.bordeaux(), 338.0)
    builder.road_stage(7, 6, france.bordeaux(), france.bayonne(), 180.0)
    builder.road_stage(7, 7, france.bayonne(), france.pau(), 106.0)
    builder.road_stage(7, 8, france.pau(), france.luchon(), 231.0)
    builder.road_stage(7, 10, france.luchon(), france.perpignan(), 322.0)
    builder.road_stage(7, 12, france.perpignan(), france.montpellier(), 164.0)
    builder.road_stage(7, 13, france.montpellier(), france.marseille(), 207.0)
    builder.road_stage(7, 14, france.marseille(), france.cannes(), 181.0)
    builder.road_stage(7, 15, france.cannes(), france.nice(), 132.0)
    builder.road_stage(7, 17, france.nice(), france.gap(), 233.0)
    builder.road_stage(7, 18, france.gap(), france.grenoble(), 102.0)
    builder.road_stage(7, 19, france.grenoble(), france.aix_les_bains(), 230.0)
    builder.road_stage(7, 20, france.aix_les_bains(), france.evian(), 204.0)
    builder.road_stage(7, 21, france.evian(), france.belfort(), 282.0)
    builder.road_stage(7, 22, france.belfort(), france.colmar(), 209.0)
    builder.road_stage(7, 23, france.colmar(), france.metz(), 192.0)
    builder.road_stage(7, 24, france.metz(), france.charleville(), 159.0)
    builder.road_stage(7, 26, france.charleville(), france.malo_les_bains(), 271.0)
    builder.road_stage(7, 28, france.malo_les_bains(), france.paris(), 313.0)
    return builder.build()

def tdf1932():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1932)
    builder.road_stage(7, 6, france.paris(), france.caen(), 208.0)
    builder.road_stage(7, 7, france.caen(), france.nantes(), 300.0)
    builder.road_stage(7, 9, france.nantes(), france.bordeaux(), 387.0)
    builder.road_stage(7, 11, france.bordeaux(), france.pau(), 206.0)
    builder.road_stage(7, 12, france.pau(), france.luchon(), 229.0)
    builder.road_stage(7, 14, france.luchon(), france.perpignan(), 322.0)
    builder.road_stage(7, 16, france.perpignan(), france.montpellier(), 168.0)
    builder.road_stage(7, 17, france.montpellier(), france.marseille(), 206.0)
    builder.road_stage(7, 18, france.marseille(), france.cannes(), 191.0)
    builder.road_stage(7, 19, france.cannes(), france.nice(), 132.0)
    builder.road_stage(7, 21, france.nice(), france.gap(), 233.0)
    builder.road_stage(7, 22, france.gap(), france.grenoble(), 102.0)
    builder.road_stage(7, 23, france.grenoble(), france.aix_les_bains(), 230.0)
    builder.road_stage(7, 24, france.aix_les_bains(), france.evian(), 204.0)
    builder.road_stage(7, 25, france.evian(), france.belfort(), 291.0)
    builder.road_stage(7, 26, france.belfort(), france.strasbourg(), 145.0)
    builder.road_stage(7, 27, france.strasbourg(), france.metz(), 165.0)
    builder.road_stage(7, 28, france.metz(), france.charleville(), 159.0)
    builder.road_stage(7, 29, france.charleville(), france.malo_les_bains(), 271.0)
    builder.road_stage(7, 30, france.malo_les_bains(), france.amiens(), 212.0)
    builder.road_stage(7, 31, france.amiens(), france.paris(), 159.0)
    return builder.build()

def tdf1933():

    builder = NonConsecutiveStageRaceBuilder(TourDeFrance(), 1933)
    builder.road_stage(6, 27, france.paris(), france.lille(), 262.0)
    builder.road_stage(6, 28, france.lille(), france.charleville(), 192.0)
    builder.road_stage(6, 29, france.charleville(), france.metz(), 166.0)
    builder.road_stage(6, 30, france.metz(), france.belfort(), 220.0)
    builder.road_stage(7, 1, france.belfort(), france.evian(), 293.0)
    builder.road_stage(7, 3, france.evian(), france.aix_les_bains(), 207.0)
    builder.road_stage(7, 4, france.aix_les_bains(), france.grenoble(), 229.0)
    builder.road_stage(7, 5, france.grenoble(), france.gap(), 102.0)
    builder.road_stage(7, 6, france.gap(), france.digne(), 227.0)
    builder.road_stage(7, 7, france.digne(), france.nice(), 156.0)
    builder.road_stage(7, 9, france.nice(), france.cannes(), 128.0)
    builder.road_stage(7, 10, france.cannes(), france.marseille(), 208.0)
    builder.road_stage(7, 11, france.marseille(), france.montpellier(), 168.0)
    builder.road_stage(7, 12, france.montpellier(), france.perpignan(), 166.0)
    builder.road_stage(7, 14, france.perpignan(), france.ax_les_thermes(), 158.0)
    builder.road_stage(7, 15, france.ax_les_thermes(), france.luchon(), 165.0)
    builder.road_stage(7, 16, france.luchon(), france.tarbes(), 91.0)
    builder.road_stage(7, 17, france.tarbes(), france.pau(), 185.0)
    builder.road_stage(7, 19, france.pau(), france.bordeaux(), 233.0)
    builder.road_stage(7, 20, france.bordeaux(), france.la_rochelle(), 183.0)
    builder.road_stage(7, 21, france.la_rochelle(), france.rennes(), 266.0)
    builder.road_stage(7, 22, france.rennes(), france.caen(), 169.0)
    builder.road_stage(7, 23, france.caen(), france.paris(), 222.0)
    return builder.build()

def tdf1934():

    builder = TourDeFranceBuilder(1934,7,3)
    
    # Stage 1
    builder.road_stage(france.paris(), france.lille(), 262)

    # Stage 2
    builder.road_stage(france.lille(), france.charleville(), 192)

    # Stage 3
    builder.road_stage(france.charleville(), france.metz(), 161)

    # Stage 4
    builder.road_stage(france.metz(), france.belfort(), 220)

    # Stage 5
    builder.road_stage(france.belfort(), france.evian(), 293)

    builder.rest_day(france.evian())



    # Stage 6
    builder.road_stage(france.evian(), france.aix_les_bains(), 207)

    # Stage 7
    builder.road_stage(france.aix_les_bains(), france.grenoble(), 229)

    # Stage 8
    builder.road_stage(france.grenoble(), france.gap(), 102)

    # Stage 9
    builder.road_stage(france.gap(), france.digne(), 227)

    # Stage 10
    builder.road_stage(france.digne(), france.nice(), 156)

    builder.rest_day(france.nice())



    # Stage 11
    builder.road_stage(france.nice(), france.cannes(), 126)

    # Stage 12
    builder.road_stage(france.cannes(), france.marseille(), 195)

    # Stage 13
    builder.road_stage(france.marseille(), france.montpellier(), 172)

    # Stage 14
    builder.road_stage(france.montpellier(), france.perpignan(), 177)

    builder.rest_day(france.perpignan())



    # Stage 15
    builder.road_stage(france.perpignan(), france.ax_les_thermes(), 158)

    # Stage 16
    builder.road_stage(france.ax_les_thermes(), france.luchon(), 165)

    # Stage 17
    builder.road_stage(france.luchon(), france.tarbes(), 91)

    # Stage 18
    builder.road_stage(france.tarbes(), france.pau(), 172)

    builder.rest_day(france.pau())


    # Stage 19
    builder.road_stage(france.pau(), france.bordeaux(), 215)

    # Stage 20
    builder.road_stage(france.bordeaux(), france.la_rochelle(), 183)

    # Stages 21a & 21b
    builder.enable_split_stages()
    builder.road_stage(france.la_rochelle(), france.la_roche_sur_yon(), 81)
    builder.individual_time_trial(france.la_roche_sur_yon(), france.nantes(), 90)
    builder.disable_split_stages()

    # Stage 21
    builder.road_stage(france.nantes(), france.caen(), 275)

    # Stage 22
    builder.road_stage(france.caen(), france.paris(), 221)

    return builder.build()

def tdf1935():

    builder = TourDeFranceBuilder(1935,7,4)

    # Stage 1
    builder.road_stage(france.paris(), france.lille(), 262.0)

    # Stage 2
    builder.road_stage(france.lille(), france.charleville(), 192.0)

    # Stage 3
    builder.road_stage(france.charleville(), france.metz(), 161.0)

    # Stage 4
    builder.road_stage(france.metz(), france.belfort(), 220.0)

    # Stage 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.belfort(), switzerland.geneva(), 262.0)
    builder.individual_time_trial(switzerland.geneva(), france.evian(), 58.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.evian())

    # Stage 6
    builder.road_stage(france.evian(), france.aix_les_bains(), 207.0)

    # Stage 7
    builder.road_stage(france.aix_les_bains(), france.grenoble(), 229.0)

    # Stage 8
    builder.road_stage(france.grenoble(), france.gap(), 102.0)

    # Stage 9
    builder.road_stage(france.gap(), france.digne(), 227.0)

    # Stage 10
    builder.road_stage(france.digne(), france.nice(), 156.0)

    # Rest day
    builder.rest_day(france.nice())

    # Stage 11
    builder.road_stage(france.nice(), france.cannes(), 126.0)

    # Stage 12
    builder.road_stage(france.cannes(), france.marseille(), 195.0)

    # Stage 13a & 13b
    builder.enable_split_stages()
    builder.road_stage(france.marseille(), france.nimes(), 112.0)
    builder.individual_time_trial(france.nimes(), france.montpellier(), 56.0)
    builder.disable_split_stages()

    # Stage 14a& 14b
    builder.enable_split_stages()
    builder.road_stage(france.montpellier(), france.narbonne(), 103.0)
    builder.individual_time_trial(france.narbonne(), france.perpignan(), 63.0)
    builder.disable_split_stages()

    # Stage 15
    builder.road_stage(france.perpignan(), france.luchon(), 325.0)

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 16
    builder.road_stage(france.luchon(), france.pau(), 194.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 17
    builder.road_stage(france.pau(), france.bordeaux(), 224.0)

    # Stage 18 & 18b
    builder.enable_split_stages()
    builder.road_stage(france.bordeaux(), france.rochefort(), 103.0)
    builder.individual_time_trial(france.rochefort(), france.la_rochelle(), 33.0)
    builder.disable_split_stages()

    # Stage 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(france.la_rochelle(), france.la_roche_sur_yon(), 81.0)
    builder.individual_time_trial(france.la_roche_sur_yon(), france.nantes(), 90.0)
    builder.disable_split_stages()

    # Stage 20a & 20b
    builder.enable_split_stages()
    builder.road_stage(france.nantes(), france.vire(), 220.0)
    builder.individual_time_trial(france.vire(), france.caen(), 55.0)
    builder.disable_split_stages()

    # Stage 21
    builder.road_stage(france.caen(), france.paris(), 221.0)

    return builder.build()

def tdf1936():

    builder = TourDeFranceBuilder(1936,7,7)

    # Stage 1
    builder.road_stage(france.paris(), france.lille(), 258.0)

    # Stage 2
    builder.road_stage(france.lille(), france.charleville(), 192.0)

    # Stage 3
    builder.road_stage(france.charleville(), france.metz(), 161.0)

    # Stage 4
    builder.road_stage(france.metz(), france.belfort(), 220.0)

    # Stage 5
    builder.road_stage(france.belfort(), france.evian_les_bains(), 298.0)

    # Rest day
    builder.rest_day(france.evian_les_bains())

    # Stage 6
    builder.road_stage(france.evian_les_bains(), france.aix_les_bains(), 212.0)

    # Stage 7
    builder.road_stage(france.aix_les_bains(), france.grenoble(), 230.0)

    # Stage 8
    builder.road_stage(france.grenoble(), france.briancon(), 194.0)

    # Stage 9
    builder.road_stage(france.briancon(), france.digne(), 220.0)

    # Rest day
    builder.rest_day(france.digne())

    # Stage 10
    builder.road_stage(france.digne(), france.nice(), 156.0)

    # Stage 11
    builder.road_stage(france.nice(), france.cannes(), 126.0)

    # Rest day
    builder.rest_day(france.cannes())

    # Stage 12
    builder.road_stage(france.cannes(), france.marseille(), 195.0)

    # Stage 13a & 13b
    builder.enable_split_stages()
    builder.road_stage(france.marseille(), france.nimes(), 112.0)
    builder.individual_time_trial(france.nimes(), france.montpellier(), 52.0)
    builder.disable_split_stages()

    # Stage 14a & 14b
    builder.enable_split_stages()
    builder.road_stage(france.montpellier(), france.narbonne(), 103.0)
    builder.individual_time_trial(france.narbonne(), france.perpignan(), 63.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.perpignan())

    # Stage 15
    builder.road_stage(france.perpignan(), france.luchon(), 325.0)

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 16
    builder.road_stage(france.luchon(), france.pau(), 194.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 17
    builder.road_stage(france.pau(), france.bordeaux(), 229.0)

    # Stage 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(france.bordeaux(), france.saintes(), 117.0)
    builder.individual_time_trial(france.saintes(), france.la_rochelle(), 75.0)
    builder.disable_split_stages()

    # Stage 19a, 19b & 19c
    builder.enable_split_stages()
    builder.road_stage(france.la_rochelle(), france.la_roche_sur_yon(), 81.0)
    builder.individual_time_trial(france.la_roche_sur_yon(), france.cholet(), 65.0)
    builder.road_stage(france.cholet(), france.angers(), 67.0)
    builder.disable_split_stages()

    # Stage 20a & 20b
    builder.enable_split_stages()
    builder.road_stage(france.angers(), france.vire(), 204.0)
    builder.individual_time_trial(france.vire(), france.caen(), 55.0)
    builder.disable_split_stages()

    # Stage 21
    builder.road_stage(france.caen(), france.paris(), 234.0)

    return builder.build()

def tdf1937():

    builder = TourDeFranceBuilder(1937,6,30)

    # Stage 1
    builder.road_stage(france.paris(), france.lille(), 263.0)

    # Stage 2
    builder.road_stage(france.lille(), france.charleville(), 192.0)

    # Stage 3
    builder.road_stage(france.charleville(), france.metz(), 161.0)

    # Stage 4
    builder.road_stage(france.metz(), france.belfort(), 220.0)

    # Stage 5a, 5b & 5c
    builder.enable_split_stages()
    builder.road_stage(france.belfort(), france.lons_le_saunier(), 175.0)
    builder.team_time_trial(france.lons_le_saunier(), france.champagnole(), 34.0)
    builder.road_stage(france.champagnole(), switzerland.geneva(), 93.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(switzerland.geneva())

    # Stage 6
    builder.road_stage(switzerland.geneva(), france.aix_les_bains(), 180.0)

    # Stage 7
    builder.road_stage(france.aix_les_bains(), france.grenoble(), 228.0)

    # Stage 8
    builder.road_stage(france.grenoble(), france.briancon(), 194.0)

    # Stage 9
    builder.road_stage(france.briancon(), france.digne(), 220.0)

    # Rest day
    builder.rest_day(france.digne())

    # Stage 10
    builder.road_stage(france.digne(), france.nice(), 251.0)

    # Rest day
    builder.rest_day(france.nice())

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(france.nice(), france.toulon(), 169.0)
    builder.team_time_trial(france.toulon(), france.marseille(), 65.0)
    builder.disable_split_stages()

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.road_stage(france.marseille(), france.nimes(), 112.0)
    builder.road_stage(france.nimes(), france.montpellier(), 51.0)
    builder.disable_split_stages()

    # Stages 13a & 13b
    builder.enable_split_stages()
    builder.road_stage(france.montpellier(), france.narbonne(), 51.0)
    builder.road_stage(france.narbonne(), france.perpignan(), 63.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.perpignan())

    # Stages 14a, 14b & 14c
    builder.enable_split_stages()
    builder.road_stage(france.perpignan(), france.bourg_madame(), 99.0)
    builder.road_stage(france.bourg_madame(), france.ax_les_thermes(), 59.0)
    builder.road_stage(france.ax_les_thermes(), france.luchon(), 167.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 15
    builder.road_stage(france.luchon(), france.pau(), 194.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 16
    builder.road_stage(france.pau(), france.bordeaux(), 235.0)

    # Stages 17a, 17b & 17c
    builder.enable_split_stages()
    builder.road_stage(france.bordeaux(), france.royan(), 123.0)
    builder.road_stage(france.royan(), france.saintes(), 37.0)
    builder.road_stage(france.saintes(), france.la_rochelle(), 37.0)
    builder.disable_split_stages()

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.team_time_trial(france.la_rochelle(), france.la_roche_sur_yon(), 82.0)
    builder.road_stage(france.la_roche_sur_yon(), france.rennes(), 172.0)
    builder.disable_split_stages()

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(france.rennes(), france.vire(), 114.0)
    builder.individual_time_trial(france.vire(), france.caen(), 59.0)
    builder.disable_split_stages()

    # Stage 20
    builder.road_stage(france.caen(), france.paris(), 234.0)

    return builder.build()

def tdf1938():

    builder = TourDeFranceBuilder(1938,7,5)

    # Stage 1
    builder.road_stage(france.paris(), france.caen(), 215.0)

    # Stage 2
    builder.road_stage(france.caen(), france.saint_brieuc(), 237.0)

    # Stage 3
    builder.road_stage(france.saint_brieuc(), france.nantes(), 238.0)

    # Stages 4a, 4b & 4c
    builder.enable_split_stages()
    builder.road_stage(france.nantes(), france.la_roche_sur_yon(), 62.0)
    builder.road_stage(france.la_roche_sur_yon(), france.la_rochelle(), 83.0)
    builder.road_stage(france.la_rochelle(), france.royan(), 83.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.royan())

    # Stage 5
    builder.road_stage(france.royan(), france.bordeaux(), 198.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(france.bordeaux(), france.arcachon(), 53.0)
    builder.road_stage(france.arcachon(), france.bayonne(), 171.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(france.bayonne(), france.pau(), 115.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 8
    builder.road_stage(france.pau(), france.luchon(), 193.0)

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 9
    builder.road_stage(france.luchon(), france.perpignan(), 260.0)

    # Stages 10a, 10b & 10c
    builder.enable_split_stages()
    builder.road_stage(france.perpignan(), france.narbonne(), 63.0)
    builder.individual_time_trial(france.narbonne(), france.beziers(), 27.0)
    builder.road_stage(france.beziers(), france.montpellier(), 73.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(france.montpellier(), france.marseille(), 223.0)

    # Stage 12
    builder.road_stage(france.marseille(), france.cannes(), 199.0)

    # Rest day
    builder.rest_day(france.cannes())

    # Stage 13
    builder.road_stage(france.cannes(), france.digne(), 284.0)

    # Stage 14
    builder.road_stage(france.digne(), france.briancon(), 219.0)

    # Stage 15
    builder.road_stage(france.briancon(), france.aix_les_bains(), 311.0)

    # Rest day
    builder.rest_day(france.aix_les_bains())

    # Stage 16
    builder.road_stage(france.aix_les_bains(), france.besancon(), 284.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(france.besancon(), france.belfort(), 89.0)
    builder.road_stage(france.belfort(), france.strasbourg(), 143.0)
    builder.disable_split_stages()

    # Stage 18
    builder.road_stage(france.strasbourg(), france.metz(), 186.0)

    # Stage 19
    builder.road_stage(france.metz(), france.reims(), 196.0)

    # Rest day
    builder.rest_day(france.reims())

    # Stages 20a, 20b & 20c
    builder.enable_split_stages()
    builder.road_stage(france.reims(), france.laon(), 48.0)
    builder.individual_time_trial(france.laon(), france.saint_quentin(), 42.0)
    builder.road_stage(france.saint_quentin(), france.lille(), 107.0)
    builder.disable_split_stages()

    # Stage 21
    builder.road_stage(france.lille(), france.paris(), 279.0)

    return builder.build()

def tdf1939():

    builder = TourDeFranceBuilder(1939,7,10)

    # Stage 1
    builder.road_stage(france.paris(), france.caen(), 215.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.individual_time_trial(france.caen(), france.vire(), 64.0)
    builder.road_stage(france.vire(), france.rennes(), 119.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(france.rennes(), france.brest(), 244.0)

    # Stage 4
    builder.road_stage(france.brest(), france.lorient(), 174.0)

    # Stage 5
    builder.road_stage(france.lorient(), france.nantes(), 207.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(france.nantes(), france.la_rochelle(), 144.0)
    builder.road_stage(france.la_rochelle(), france.royan(), 107.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.royan())

    # Stage 7
    builder.road_stage(france.royan(), france.bordeaux(), 198.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(france.bordeaux(), france.salies_de_bearn(), 210.0)
    builder.individual_time_trial(france.salies_de_bearn(), france.pau(), 69.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(france.pau(), france.toulouse(), 311.0)

    # Rest day
    builder.rest_day(france.toulouse())

    # Stages 10a, 10b & 10c
    builder.enable_split_stages()
    builder.road_stage(france.toulouse(), france.narbonne(), 149.0)
    builder.individual_time_trial(france.narbonne(), france.beziers(), 27.0)
    builder.road_stage(france.beziers(), france.montpellier(), 70.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(france.montpellier(), france.marseille(), 212.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.road_stage(france.marseille(), france.saint_raphael(), 157.0)
    builder.road_stage(france.saint_raphael(), monaco.monaco(), 122.0)
    builder.disable_split_stages()

    # Stage 13
    builder.criterium(monaco.monaco(), 101.0)

    # Stage 14
    builder.road_stage(monaco.monaco(), france.digne(), 175.0)

    # Stage 15
    builder.road_stage(france.digne(), france.briancon(), 219.0)

    # Stages 16a, 16b & 16c
    builder.enable_split_stages()
    builder.criterium(france.briancon(), 126.0)
    builder.individual_time_trial(france.bonneval(), france.bourg_saint_maurice(), 64.0)
    builder.road_stage(france.bourg_saint_maurice(), france.annecy(), 104.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.annecy())

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(france.annecy(), france.dole(), 226.0)
    builder.individual_time_trial(france.dole(), france.dijon(), 59.0)
    builder.disable_split_stages()

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(france.dijon(), france.troyes(), 151.0)
    builder.road_stage(france.troyes(), france.paris(), 201.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1947():

    builder = TourDeFranceBuilder(1947,6,25)

    # Stage 1
    builder.road_stage(france.paris(), france.lille(), 236.0)

    # Stage 2
    builder.road_stage(france.lille(), belgium.brussels(), 182.0)

    # Stage 3
    builder.road_stage(belgium.brussels(), luxembourg.luxembourg_city(), 314.0)

    # Stage 4
    builder.road_stage(luxembourg.luxembourg_city(), france.strasbourg(), 223.0)

    # Stage 5
    builder.road_stage(france.strasbourg(), france.besancon(), 248.0)

    # Rest day
    builder.rest_day(france.besancon())

    # Stage 6
    builder.road_stage(france.besancon(), france.lyon(), 249.0)

    # Stage 7
    builder.road_stage(france.lyon(), france.grenoble(), 172.0)

    # Stage 8
    builder.road_stage(france.grenoble(), france.briancon(), 185.0)

    # Rest day
    builder.rest_day(france.briancon())

    # Stage 9
    builder.road_stage(france.briancon(), france.digne(), 217.0)

    # Stage 10
    builder.road_stage(france.digne(), france.nice(), 255.0)

    # Rest day
    builder.rest_day(france.nice())

    # Stage 11
    builder.road_stage(france.nice(), france.marseille(), 230.0)

    # Stage 12
    builder.road_stage(france.marseille(), france.montpellier(), 165.0)

    # Stage 13
    builder.road_stage(france.montpellier(), france.carcassonne(), 172.0)

    # Stage 14
    builder.road_stage(france.carcassonne(), france.luchon(), 253.0)

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 15
    builder.road_stage(france.luchon(), france.pau(), 195.0)

    # Stage 16
    builder.road_stage(france.pau(), france.bordeaux(), 195.0)

    # Stage 17
    builder.road_stage(france.bordeaux(), france.les_sables_d_olonne(), 272.0)

    # Stage 18
    builder.road_stage(france.les_sables_d_olonne(), france.vannes(), 236.0)

    # Rest day
    builder.rest_day(france.vannes())

    # Stage 19
    builder.individual_time_trial(france.vannes(), france.saint_brieuc(), 139.0)

    # Stage 20
    builder.road_stage(france.saint_brieuc(), france.caen(), 235.0)

    # Stage 21
    builder.road_stage(france.caen(), france.paris(), 257.0)

    return builder.build()

def tdf1948():

    builder = TourDeFranceBuilder(1948,6,30)

    # Stage 1
    builder.road_stage(france.paris(), france.trouville(), 237.0)

    # Stage 2
    builder.road_stage(france.trouville(), france.dinard(), 259.0)

    # Stage 3
    builder.road_stage(france.dinard(), france.nantes(), 251.0)

    # Stage 4
    builder.road_stage(france.nantes(), france.la_rochelle(), 166.0)

    # Stage 5
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 262.0)

    # Stage 6
    builder.road_stage(france.bordeaux(), france.biarritz(), 244.0)

    # Rest day
    builder.rest_day(france.biarritz())

    # Stage 7
    builder.road_stage(france.biarritz(), france.lourdes(), 219.0)

    # Stage 8
    builder.road_stage(france.lourdes(), france.toulouse(), 261.0)

    # Rest day
    builder.rest_day(france.toulouse())

    # Stage 9
    builder.road_stage(france.toulouse(), france.montpellier(), 246.0)

    # Stage 10
    builder.road_stage(france.montpellier(), france.marseille(), 248.0)

    # Stage 11
    builder.road_stage(france.marseille(), italy.san_remo(), 245.0)

    # Stage 12
    builder.road_stage(italy.san_remo(), france.cannes(), 170.0)

    # Rest day
    builder.rest_day(france.cannes())

    # Stage 13
    builder.road_stage(france.cannes(), france.briancon(), 274.0)

    # Stage 14
    builder.road_stage(france.briancon(), france.aix_les_bains(), 263.0)

    # Rest day
    builder.rest_day(france.aix_les_bains())

    # Stage 15
    builder.road_stage(france.aix_les_bains(), switzerland.lausanne(), 256.0)

    # Stage 16
    builder.road_stage(switzerland.lausanne(), france.mulhouse(), 243.0)

    # Rest day
    builder.rest_day(france.mulhouse())

    # Stage 17
    builder.individual_time_trial(france.mulhouse(), france.strasbourg(), 120.0)

    # Stage 18
    builder.road_stage(france.strasbourg(), france.metz(), 195.0)

    # Stage 19
    builder.road_stage(france.metz(), belgium.liege(), 249.0)

    # Stage 20
    builder.road_stage(belgium.liege(), france.roubaix(), 228.0)

    # Stage 21
    builder.road_stage(france.roubaix(), france.paris(), 286.0)

    return builder.build()

def tdf1949():

    builder = TourDeFranceBuilder(1949,6,30)

    # Stage 1
    builder.road_stage(france.paris(), france.reims(), 182.0)

    # Stage 2
    builder.road_stage(france.reims(), belgium.brussels(), 273.0)

    # Stage 3
    builder.road_stage(belgium.brussels(), france.boulogne_sur_mer(), 211.0)

    # Stage 4
    builder.road_stage(france.boulogne_sur_mer(), france.rouen(), 185.0)

    # Stage 5
    builder.road_stage(france.rouen(), france.saint_malo(), 293.0)

    # Stage 6
    builder.road_stage(france.saint_malo(), france.les_sables_d_olonne(), 305.0)

    # Rest day
    builder.rest_day(france.les_sables_d_olonne())

    # Stage 7
    builder.individual_time_trial(france.les_sables_d_olonne(), france.la_rochelle(), 92.0)

    # Stage 8
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 262.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), spain.san_sebastian(), 228.0)

    # Stage 10
    builder.road_stage(spain.san_sebastian(), france.pau(), 192.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 11
    builder.road_stage(france.pau(), france.luchon(), 193.0)

    # Stage 12
    builder.road_stage(france.luchon(), france.toulouse(), 134.0)

    # Stage 13
    builder.road_stage(france.toulouse(), france.nimes(), 289.0)

    # Stage 14
    builder.road_stage(france.nimes(), france.marseille(), 199.0)

    # Stage 15
    builder.road_stage(france.marseille(), france.cannes(), 215.0)

    # Rest day
    builder.rest_day(france.cannes())


    # Stage 16
    builder.road_stage(france.cannes(), france.briancon(), 275.0)

    # Stage 17
    builder.road_stage(france.briancon(), italy.aosta(), 257.0)

    # Rest day
    builder.rest_day(italy.aosta())


    # Stage 18
    builder.road_stage(italy.aosta(), switzerland.lausanne(), 265.0)

    # Stage 19
    builder.road_stage(switzerland.lausanne(), france.colmar(), 283.0)

    # Stage 20
    builder.individual_time_trial(france.colmar(), france.nancy(), 137.0)

    # Stage 21
    builder.road_stage(france.nancy(), france.paris(), 340.0)

    return builder.build()

def tdf1950():

    builder = TourDeFranceBuilder(1950,7,13)

    # Stage 1
    builder.road_stage(france.paris(), france.metz(), 307.0)

    # Stage 2
    builder.road_stage(france.metz(), belgium.liege(), 241.0)

    # Stage 3
    builder.road_stage(belgium.liege(), france.lille(), 232.5)

    # Stage 4
    builder.road_stage(france.lille(), france.rouen(), 231.0)

    # Stage 5
    builder.road_stage(france.rouen(), france.dinard(), 316.0)

    # Rest day
    builder.rest_day(france.dinard())

    # Stage 6
    builder.individual_time_trial(france.dinard(), france.saint_brieuc(), 78.0)

    # Stage 7
    builder.road_stage(france.saint_brieuc(), france.angers(), 248.0)

    # Stage 8
    builder.road_stage(france.angers(), france.niort(), 181.0)

    # Stage 9
    builder.road_stage(france.niort(), france.bordeaux(), 206.0)

    # Stage 10
    builder.road_stage(france.bordeaux(), france.pau(), 202.0)

    # Rest day
    builder.rest_day(france.pau())


    # Stage 11
    builder.road_stage(france.pau(), france.saint_gaudens(), 230.0)

    # Stage 12
    builder.road_stage(france.saint_gaudens(), france.perpignan(), 233.0)

    # Stage 13
    builder.road_stage(france.perpignan(), france.nimes(), 215.0)

    # Stage 14
    builder.road_stage(france.nimes(), france.toulon(), 222.0)

    # Stage 15
    builder.road_stage(france.toulon(), france.menton(), 205.5)

    # Stage 16
    builder.road_stage(france.menton(), france.nice(), 96.0)

    # Rest day
    builder.rest_day(france.nice())

    # Stage 17
    builder.road_stage(france.nice(), france.gap(), 229.0)

    # Stage 18
    builder.road_stage(france.gap(), france.briancon(), 165.0)

    # Stage 19
    builder.road_stage(france.briancon(), france.saint_etienne(), 291.0)

    # Rest day
    builder.rest_day(france.saint_etienne())

    # Stage 20
    builder.individual_time_trial(france.saint_etienne(), france.lyon(), 98.0)

    # Stage 21
    builder.road_stage(france.lyon(), france.dijon(), 233.0)

    # Stage 22
    builder.road_stage(france.dijon(), france.paris(), 314.0)

    return builder.build()

def tdf1951():

    builder = TourDeFranceBuilder(1951,7,4)

    # Stage 1
    builder.road_stage(france.metz(), france.reims(), 185.0)

    # Stage 2
    builder.road_stage(france.reims(), belgium.ghent(), 228.0)

    # Stage 3
    builder.road_stage(belgium.ghent(), france.le_treport(), 219.0)

    # Stage 4
    builder.road_stage(france.le_treport(), france.paris(), 188.0)

    # Stage 5
    builder.road_stage(france.paris(), france.caen(), 215.0)

    # Stage 6
    builder.road_stage(france.caen(), france.rennes(), 182.0)

    # Stage 7
    builder.individual_time_trial(france.la_guerche_de_bretagne(), france.angers(), 85.0)

    # Stage 8
    builder.road_stage(france.angers(), france.limoges(), 241.0)

    # Rest day
    builder.rest_day(france.limoges())

    # Stage 9
    builder.road_stage(france.limoges(), france.clermont_ferrand(), 236.0)

    # Stage 10
    builder.road_stage(france.clermont_ferrand(), france.brive(), 216.0)

    # Stage 11
    builder.road_stage(france.brive(), france.agen(), 177.0)

    # Stage 12
    builder.road_stage(france.agen(), france.dax(), 185.0)

    # Stage 13
    builder.road_stage(france.dax(), france.tarbes(), 201.0)

    # Stage 14
    builder.road_stage(france.tarbes(), france.luchon(), 142.0)

    # Stage 15
    builder.road_stage(france.luchon(), france.carcassonne(), 213.0)

    # Stage 16
    builder.road_stage(france.carcassonne(), france.montpellier(), 192.0)

    # Rest day
    builder.rest_day(france.montpellier())


    # Stage 17
    builder.road_stage(france.montpellier(), france.avignon(), 224.0)

    # Stage 18
    builder.road_stage(france.avignon(), france.marseille(), 173.0)

    # Stage 19
    builder.road_stage(france.marseille(), france.gap(), 208.0)

    # Stage 20
    builder.road_stage(france.gap(), france.briancon(), 165.0)

    # Stage 21
    builder.road_stage(france.briancon(), france.aix_les_bains(), 201.0)

    # Stage 22
    builder.individual_time_trial(france.aix_les_bains(), switzerland.geneva(), 97.0)

    # Stage 23
    builder.road_stage(switzerland.geneva(), france.dijon(), 197.0)

    # Stage 24
    builder.road_stage(france.dijon(), france.paris(), 322.0)

    return builder.build()

def tdf1952():

    builder = TourDeFranceBuilder(1952,6,25)

    # Stage 1
    builder.road_stage(france.brest(), france.rennes(), 246.0)

    # Stage 2
    builder.road_stage(france.rennes(), france.le_mans(), 181.0)

    # Stage 3
    builder.road_stage(france.le_mans(), france.rouen(), 189.0)

    # Stage 4
    builder.road_stage(france.rouen(), france.roubaix(), 232.0)

    # Stage 5
    builder.road_stage(france.roubaix(), belgium.namur(), 197.0)

    # Stage 6
    builder.road_stage(belgium.namur(), france.metz(), 228.0)

    # Stage 7
    builder.individual_time_trial(france.metz(), france.nancy(), 60.0)

    # Stage 8
    builder.road_stage(france.nancy(), france.mulhouse(), 252.0)

    # Stage 9
    builder.road_stage(france.mulhouse(), switzerland.lausanne(), 238.0)

    # Stage 10
    builder.mountain_stage(switzerland.lausanne())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 266.0)

    # Rest day
    builder.rest_day(mountains.alps.alpe_d_huez())

    # Stage 11
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 182.0)

    # Stage 12
    builder.road_stage(mountains.alps.sestriere(), monaco.monaco(), 251.0)

    # Stage 13
    builder.road_stage(monaco.monaco(), france.aix_en_provence(), 214.0)

    # Stage 14
    builder.road_stage(france.aix_en_provence(), france.avignon(), 178.0)

    # Stage 15
    builder.road_stage(france.avignon(), france.perpignan(), 275.0)

    # Stage 16
    builder.road_stage(france.perpignan(), france.toulouse(), 200.0)

    # Rest day
    builder.rest_day(france.toulouse())


    # Stage 17
    builder.road_stage(france.toulouse(), france.bagneres_de_bigorre(), 204.0)

    # Stage 18
    builder.road_stage(france.bagneres_de_bigorre(), france.pau(), 149.0)

    # Stage 19
    builder.road_stage(france.pau(), france.bordeaux(), 195.0)

    # Stage 20
    builder.road_stage(france.bordeaux(), france.limoges(), 228.0)

    # Stage 21
    builder.mountain_stage(france.limoges())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 245.0)

    # Stage 22
    builder.individual_time_trial(france.clermont_ferrand(), france.vichy(), 63.0)

    # Stage 23
    builder.road_stage(france.vichy(), france.paris(), 354.0)

    return builder.build()

def tdf1953():

    builder = TourDeFranceBuilder(1953,7,3)

    # Stage 1
    builder.road_stage(france.strasbourg(), france.metz(), 195.0)

    # Stage 2
    builder.road_stage(france.metz(), belgium.liege(), 227.0)

    # Stage 3
    builder.road_stage(belgium.liege(), france.lille(), 221.0)

    # Stage 4
    builder.road_stage(france.lille(), france.dieppe(), 188.0)

    # Stage 5
    builder.road_stage(france.dieppe(), france.caen(), 200.0)

    # Stage 6
    builder.road_stage(france.caen(), france.le_mans(), 206.0)

    # Stage 7
    builder.road_stage(france.le_mans(), france.nantes(), 181.0)

    # Stage 8
    builder.road_stage(france.nantes(), france.bordeaux(), 345.0)

    # Rest day
    builder.rest_day(france.bordeaux())


    # Stage 9
    builder.road_stage(france.bordeaux(), france.pau(), 197.0)

    # Stage 10
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.cauterets(), ColCategory.HC, 103.0)

    # Stage 11
    builder.road_stage(mountains.pyrenees.cauterets(), france.luchon(), 115.0)

    # Stage 12
    builder.road_stage(france.luchon(), france.albi(), 228.0)

    # Stage 13
    builder.road_stage(france.albi(), france.beziers(), 189.0)

    # Stage 14
    builder.road_stage(france.beziers(), france.nimes(), 214.0)

    # Stage 15
    builder.road_stage(france.nimes(), france.marseille(), 173.0)

    # Stage 16
    builder.road_stage(france.marseille(), monaco.monaco(), 236.0)

    # Rest day
    builder.rest_day(monaco.monaco())

    # Stage 17
    builder.road_stage(monaco.monaco(), france.gap(), 261.0)

    # Stage 18
    builder.road_stage(france.gap(), france.briancon(), 165.0)

    # Stage 19
    builder.road_stage(france.briancon(), france.lyon(), 227.0)

    # Stage 20
    builder.individual_time_trial(france.lyon(), france.saint_etienne(), 70.0)

    # Stage 21
    builder.road_stage(france.saint_etienne(), france.montlucon(), 210.0)

    # Stage 22
    builder.road_stage(france.montlucon(), france.paris(), 328.0)

    return builder.build()

def tdf1954():

    builder = TourDeFranceBuilder(1954,7,8)

    # Stage 1
    builder.road_stage(netherlands.amsterdam(), belgium.brasschaat(), 216.0)

    # Stage 2
    builder.road_stage(belgium.beveren(), france.lille(), 255.0)

    # Stage 3
    builder.road_stage(france.lille(), france.rouen(), 219.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.team_time_trial(france.rouen(), france.circuit_des_essarts(), 10.4)
    builder.road_stage(france.rouen(), france.caen(), 131.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(france.caen(), france.saint_brieuc(), 224.0)

    # Stage 6
    builder.road_stage(france.saint_brieuc(), france.brest(), 179.0)

    # Stage 7
    builder.road_stage(france.brest(), france.vannes(), 211.0)

    # Stage 8
    builder.road_stage(france.vannes(), france.angers(), 190.0)

    # Stage 9
    builder.road_stage(france.angers(), france.bordeaux(), 343.0)

    # Rest day
    builder.rest_day(france.bordeaux())

    # Stage 10
    builder.road_stage(france.bordeaux(), france.bayonne(), 202.0)

    # Stage 11
    builder.road_stage(france.bayonne(), france.pau(), 241.0)

    # Stage 12
    builder.road_stage(france.pau(), france.luchon(), 161.0)

    # Stage 13
    builder.road_stage(france.luchon(), france.mulhouse(), 203.0)

    # Stage 14
    builder.road_stage(france.mulhouse(), france.millau(), 225.0)

    # Stage 15
    builder.road_stage(france.millau(), france.le_puy(), 197.0)

    # Stage 16
    builder.road_stage(france.le_puy(), france.lyon(), 194.0)

    # Rest day
    builder.rest_day(france.lyon())

    # Stage 17
    builder.road_stage(france.lyon(), france.grenoble(), 182.0)

    # Stage 18
    builder.road_stage(france.grenoble(), france.briancon(), 216.0)

    # Stage 19
    builder.road_stage(france.briancon(), france.aix_les_bains(), 221.0)

    # Stage 20
    builder.road_stage(france.aix_les_bains(), france.besancon(), 243.0)

    # Stages 21a & 21b
    builder.enable_split_stages()
    builder.road_stage(france.besancon(), france.epinal(), 134.0)
    builder.individual_time_trial(france.epinal(), france.nancy(), 72.0)
    builder.disable_split_stages()

    # Stage 22
    builder.road_stage(france.nancy(), france.troyes(), 216.0)

    # Stage 23
    builder.road_stage(france.troyes(), france.paris(), 180.0)

    return builder.build()

def tdf1955():

    builder = TourDeFranceBuilder(1955,7,7)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(france.le_havre(), france.dieppe(), 102.0)
    builder.out_and_back_team_time_trial(france.dieppe(), 12.5)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(france.dieppe(), france.roubaix(), 204.0)

    # Stage 3
    builder.road_stage(france.roubaix(), belgium.namur(), 210.0)

    # Stage 4
    builder.road_stage(belgium.namur(), france.metz(), 225.0)

    # Stage 5
    builder.road_stage(france.metz(), france.colmar(), 229.0)

    # Stage 6
    builder.road_stage(france.colmar(), switzerland.zurich(), 195.0)

    # Stage 7
    builder.road_stage(switzerland.zurich(), france.thonon_les_bains(), 267.0)

    # Stage 8
    builder.road_stage(france.thonon_les_bains(), france.briancon(), 253.0)

    # Stage 9
    builder.road_stage(france.briancon(), monaco.monaco(), 275.0)

    # Rest day
    builder.rest_day(monaco.monaco())


    # Stage 10
    builder.road_stage(monaco.monaco(), france.marseille(), 240.0)

    # Stage 11
    builder.road_stage(france.marseille(), france.avignon(), 198.0)

    # Stage 12
    builder.road_stage(france.avignon(), france.millau(), 240.0)

    # Stage 13
    builder.road_stage(france.millau(), france.albi(), 205.0)

    # Stage 14
    builder.road_stage(france.albi(), france.narbonne(), 156.0)

    # Stage 15
    builder.road_stage(france.narbonne(), france.ax_les_thermes(), 151.0)

    # Rest day
    builder.rest_day(france.ax_les_thermes())


    # Stage 16
    builder.road_stage(france.ax_les_thermes(), france.toulouse(), 123.0)

    # Stage 17
    builder.road_stage(france.toulouse(), france.saint_gaudens(), 250.0)

    # Stage 18
    builder.road_stage(france.saint_gaudens(), france.pau(), 205.0)

    # Stage 19
    builder.road_stage(france.pau(), france.bordeaux(), 195.0)

    # Stage 20
    builder.road_stage(france.bordeaux(), france.poitiers(), 243.0)

    # Stage 21
    builder.individual_time_trial(france.chatellerault(), france.tours(), 68.6)

    # Stage 22
    builder.road_stage(france.tours(), france.paris(), 229.0)

    return builder.build()

def tdf1956():

    builder = TourDeFranceBuilder(1956,7,5)

    # Stage 1
    builder.road_stage(france.reims(), belgium.liege(), 223.0)

    # Stage 2
    builder.road_stage(belgium.liege(), france.lille(), 217.0)

    # Stage 3
    builder.road_stage(france.lille(), france.rouen(), 225.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.circuit_de_rouen_les_essarts(), 15.1)
    builder.road_stage(france.rouen(), france.caen(), 125.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(france.caen(), france.saint_malo(), 189.0)

    # Stage 6
    builder.road_stage(france.saint_malo(), france.lorient(), 192.0)

    # Stage 7
    builder.road_stage(france.lorient(), france.angers(), 244.0)

    # Stage 8
    builder.road_stage(france.angers(), france.la_rochelle(), 180.0)

    # Stage 9
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 219.0)

    # Rest day
    builder.rest_day(france.bordeaux())

    # Stage 10
    builder.road_stage(france.bordeaux(), france.bayonne(), 201.0)

    # Stage 11
    builder.road_stage(france.bayonne(), france.pau(), 255.0)

    # Stage 12
    builder.road_stage(france.pau(), france.luchon(), 130.0)

    # Stage 13
    builder.road_stage(france.luchon(), france.toulouse(), 176.0)

    # Stage 14
    builder.road_stage(france.toulouse(), france.montpellier(), 231.0)

    # Stage 15
    builder.road_stage(france.montpellier(), france.aix_en_provence(), 204.0)

    # Rest day
    builder.rest_day(france.aix_en_provence())

    # Stage 16
    builder.road_stage(france.aix_en_provence(), france.gap(), 203.0)

    # Stage 17
    builder.road_stage(france.gap(), italy.turin(), 234.0)

    # Stage 18
    builder.road_stage(italy.turin(), france.grenoble(), 250.0)

    # Stage 19
    builder.road_stage(france.grenoble(), france.saint_etienne(), 173.0)

    # Stage 20
    builder.individual_time_trial(france.saint_etienne(), france.lyon(), 73.0)

    # Stage 21
    builder.road_stage(france.lyon(), france.montlucon(), 237.0)

    # Stage 22
    builder.road_stage(france.montlucon(), france.paris(), 331.0)

    return builder.build()

def tdf1957():

    builder = TourDeFranceBuilder(1957,6,27)

    # Stage 1
    builder.road_stage(france.nantes(), france.granville(), 204.0)

    # Stage 2
    builder.road_stage(france.granville(), france.caen(), 226.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(france.circuit_de_la_prairie(), 15.0)
    builder.road_stage(france.caen(), france.rouen(), 134.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.rouen(), france.roubaix(), 232.0)

    # Stage 5
    builder.road_stage(france.roubaix(), belgium.charleroi(), 170.0)

    # Stage 6
    builder.road_stage(belgium.charleroi(), france.metz(), 248.0)

    # Stage 7
    builder.road_stage(france.metz(), france.colmar(), 223.0)

    # Stage 8
    builder.road_stage(france.colmar(), france.besancon(), 192.0)

    # Stage 9
    builder.road_stage(france.besancon(), france.thonon_les_bains(), 188.0)

    # Rest day
    builder.rest_day(france.thonon_les_bains())

    # Stage 10
    builder.road_stage(france.thonon_les_bains(), france.briancon(), 247.0)

    # Stage 11
    builder.road_stage(france.briancon(), france.cannes(), 286.0)

    # Stage 12
    builder.road_stage(france.cannes(), france.marseille(), 239.0)

    # Stage 13
    builder.road_stage(france.marseille(), france.ales(), 160.0)

    # Stage 14
    builder.road_stage(france.ales(), france.perpignan(), 246.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(france.perpignan(), spain.barcelona(), 197.0)
    builder.out_and_back_individual_time_trial(spain.montjuic_circuit(), 9.8)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(spain.barcelona())

    # Stage 16
    builder.road_stage(spain.barcelona(), france.ax_les_thermes(), 220.0)

    # Stage 17
    builder.road_stage(france.ax_les_thermes(), france.saint_gaudens(), 236.0)

    # Stage 18
    builder.road_stage(france.saint_gaudens(), france.pau(), 207.0)

    # Stage 19
    builder.road_stage(france.pau(), france.bordeaux(), 194.0)

    # Stage 20
    builder.individual_time_trial(france.bordeaux(), france.libourne(), 66.0)

    # Stage 21
    builder.road_stage(france.libourne(), france.tours(), 317.0)

    # Stage 22
    builder.road_stage(france.tours(), france.paris(), 227.0)

    return builder.build()

def tdf1958():

    builder = TourDeFranceBuilder(1958,6,26)

    # Stage 1
    builder.road_stage(belgium.brussels(), belgium.ghent(), 184.0)

    # Stage 2
    builder.road_stage(belgium.ghent(), france.dunkerque(), 198.0)

    # Stage 3
    builder.road_stage(france.dunkerque(), france.mers_les_bains(), 177.0)

    # Stage 4
    builder.road_stage(france.le_treport(), france.versailles(), 205.0)

    # Stage 5
    builder.road_stage(france.versailles(), france.caen(), 232.0)

    # Stage 6
    builder.road_stage(france.caen(), france.saint_brieuc(), 223.0)

    # Stage 7
    builder.road_stage(france.saint_brieuc(), france.brest(), 170.0)

    # Stage 8
    builder.out_and_back_individual_time_trial(france.chateaulin(), 46.0)

    # Stage 9
    builder.road_stage(france.quimper(), france.saint_nazaire(), 206.0)

    # Stage 10
    builder.road_stage(france.saint_nazaire(), france.royan(), 255.0)

    # Stage 11
    builder.road_stage(france.royan(), france.bordeaux(), 137.0)

    # Stage 12
    builder.road_stage(france.bordeaux(), france.dax(), 161.0)

    # Stage 13
    builder.road_stage(france.dax(), france.pau(), 230.0)

    # Stage 14
    builder.road_stage(france.pau(), france.luchon(), 129.0)

    # Stage 15
    builder.road_stage(france.luchon(), france.toulouse(), 176.0)

    # Stage 16
    builder.road_stage(france.toulouse(), france.beziers(), 187.0)

    # Stage 17
    builder.road_stage(france.beziers(), france.nimes(), 189.0)

    # Stage 18
    builder.mountain_time_trial(france.bedoin())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 21.0)

    # Stage 19
    builder.road_stage(france.carpentras(), france.gap(), 178.0)

    # Stage 20
    builder.road_stage(france.gap(), france.briancon(), 165.0)

    # Stage 21
    builder.road_stage(france.briancon(), france.aix_les_bains(), 219.0)

    # Stage 22
    builder.road_stage(france.aix_les_bains(), france.besancon(), 237.0)

    # Stage 23
    builder.individual_time_trial(france.besancon(), france.dijon(), 74.0)

    # Stage 24
    builder.road_stage(france.dijon(), france.paris(), 320.0)

    return builder.build()

def tdf1959():

    builder = TourDeFranceBuilder(1959,6,25)

    # Stage 1
    builder.road_stage(france.mulhouse(), france.metz(), 238.0)

    # Stage 2
    builder.road_stage(france.metz(), belgium.namur(), 234.0)

    # Stage 3
    builder.road_stage(belgium.namur(), france.roubaix(), 217.0)

    # Stage 4
    builder.road_stage(france.roubaix(), france.rouen(), 230.0)

    # Stage 5
    builder.road_stage(france.rouen(), france.rennes(), 286.0)

    # Stage 6
    builder.individual_time_trial(france.blain(), france.nantes(), 45.0)

    # Stage 7
    builder.road_stage(france.nantes(), france.la_rochelle(), 190.0)

    # Stage 8
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 201.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), france.bayonne(), 207.0)

    # Rest day
    builder.rest_day(france.bayonne())


    # Stage 10
    builder.road_stage(france.bayonne(), france.bagneres_de_bigorre(), 235.0)

    # Stage 11
    builder.road_stage(france.bagneres_de_bigorre(), france.saint_gaudens(), 119.0)

    # Stage 12
    builder.road_stage(france.saint_gaudens(), france.albi(), 184.0)

    # Stage 13
    builder.road_stage(france.albi(), france.aurillac(), 219.0)

    # Stage 14
    builder.road_stage(france.aurillac(), france.clermont_ferrand(), 231.0)

    # Stage 15
    builder.out_and_back_individual_time_trial(mountains.massif_central.puy_de_dome(), 12.0)

    # Stage 16
    builder.road_stage(france.clermont_ferrand(), france.saint_etienne(), 210.0)

    # Rest day
    builder.rest_day(france.saint_etienne())

    # Stage 17
    builder.road_stage(france.saint_etienne(), france.grenoble(), 197.0)

    # Stage 18
    builder.road_stage(france.grenoble(), italy.saint_vincent(), 243.0)

    # Stage 19
    builder.road_stage(italy.saint_vincent(), france.annecy(), 251.0)

    # Stage 20
    builder.road_stage(france.annecy(), france.chalon_sur_saone(), 202.0)

    # Stage 21
    builder.individual_time_trial(france.seurre(), france.dijon(), 69.0)

    # Stage 22
    builder.road_stage(france.dijon(), france.paris(), 331.0)

    return builder.build()

def tdf1960():

    builder = TourDeFranceBuilder(1960,6,26)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(france.lille(), belgium.brussels(), 108.0)
    builder.out_and_back_individual_time_trial(belgium.brussels(), 27.8)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(belgium.brussels(), france.dunkerque(), 206.0)

    # Stage 3
    builder.road_stage(france.dunkerque(), france.dieppe(), 209.0)

    # Stage 4
    builder.road_stage(france.dieppe(), france.caen(), 211.0)

    # Stage 5
    builder.road_stage(france.caen(), france.saint_malo(), 189.0)

    # Stage 6
    builder.road_stage(france.saint_malo(), france.lorient(), 191.0)

    # Stage 7
    builder.road_stage(france.lorient(), france.angers(), 244.0)

    # Stage 8
    builder.road_stage(france.angers(), france.limoges(), 240.0)

    # Stage 9
    builder.road_stage(france.limoges(), france.bordeaux(), 225.0)

    # Stage 10
    builder.road_stage(france.mont_de_marsan(), france.pau(), 228.0)

    # Stage 11
    builder.road_stage(france.pau(), france.luchon(), 161.0)

    # Stage 12
    builder.road_stage(france.luchon(), france.toulouse(), 176.0)

    # Stage 13
    builder.road_stage(france.toulouse(), france.millau(), 224.0)

    # Rest day
    builder.rest_day(france.millau())


    # Stage 14
    builder.road_stage(france.millau(), france.avignon(), 217.0)

    # Stage 15
    builder.road_stage(france.avignon(), france.gap(), 187.0)

    # Stage 16
    builder.road_stage(france.gap(), france.briancon(), 172.0)

    # Stage 17
    builder.road_stage(france.briancon(), france.aix_les_bains(), 229.0)

    # Stage 18
    builder.road_stage(france.aix_les_bains(), france.thonon_les_bains(), 215.0)

    # Stage 19
    builder.individual_time_trial(france.pontarlier(), france.besancon(), 83.0)

    # Stage 20
    builder.road_stage(france.besancon(), france.troyes(), 229.0)

    # Stage 21
    builder.road_stage(france.troyes(), france.paris(), 200.0)

    return builder.build()

def tdf1961():

    builder = TourDeFranceBuilder(1961,6,25)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(france.rouen(), france.versailles(), 136.5)
    builder.out_and_back_individual_time_trial(france.versailles(), 28.5)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(france.pontoise(), france.roubaix(), 230.5)

    # Stage 3
    builder.road_stage(france.roubaix(), belgium.charleroi(), 197.5)

    # Stage 4
    builder.road_stage(belgium.charleroi(), france.metz(), 237.5)

    # Stage 5
    builder.road_stage(france.metz(), france.strasbourg(), 221.0)

    # Stage 6
    builder.road_stage(france.strasbourg(), france.belfort(), 180.5)

    # Stage 7
    builder.road_stage(france.belfort(), france.chalon_sur_saone(), 214.5)

    # Stage 8
    builder.road_stage(france.chalon_sur_saone(), france.saint_etienne(), 240.5)

    # Stage 9
    builder.road_stage(france.saint_etienne(), france.grenoble(), 230.0)

    # Stage 10
    builder.road_stage(france.grenoble(), italy.turin(), 250.5)

    # Stage 11
    builder.road_stage(italy.turin(), france.antibes(), 225.0)

    # Stage 12
    builder.road_stage(france.antibes(), france.aix_en_provence(), 199.0)

    # Stage 13
    builder.road_stage(france.aix_en_provence(), france.montpellier(), 177.5)

    # Rest day
    builder.rest_day(france.montpellier())

    # Stage 14
    builder.road_stage(france.montpellier(), france.perpignan(), 174.0)

    # Stage 15
    builder.road_stage(france.perpignan(), france.toulouse(), 206.0)

    # Stage 16
    builder.mountain_stage(france.toulouse())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 208.0)

    # Stage 17
    builder.road_stage(france.luchon(), france.pau(), 197.0)

    # Stage 18
    builder.road_stage(france.pau(), france.bordeaux(), 207.0)

    # Stage 19
    builder.individual_time_trial(france.bergerac(), france.perigueux(), 74.5)

    # Stage 20
    builder.road_stage(france.perigueux(), france.tours(), 309.5)

    # Stage 21
    builder.road_stage(france.tours(), france.paris(), 252.5)

    return builder.build()

def tdf1962():

    builder = TourDeFranceBuilder(1962,6,24)

    # Stage 1
    builder.road_stage(france.nancy(), belgium.spa(), 253.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(belgium.spa(), belgium.herentals(), 147.0)
    builder.out_and_back_team_time_trial(belgium.herentals(), 23.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(belgium.brussels(), france.amiens(), 210.0)

    # Stage 4
    builder.road_stage(france.amiens(), france.le_havre(), 196.5)

    # Stage 5
    builder.road_stage(france.pont_l_eveque(), france.saint_malo(), 215.0)

    # Stage 6
    builder.road_stage(france.dinard(), france.brest(), 235.5)

    # Stage 7
    builder.road_stage(france.quimper(), france.saint_nazaire(), 201.0)

    # Stage 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(france.saint_nazaire(), france.lucon(), 155.0)
    builder.individual_time_trial(france.lucon(), france.la_rochelle(), 43.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 214.0)

    # Stage 10
    builder.road_stage(france.bordeaux(), france.bayonne(), 184.5)

    # Stage 11
    builder.road_stage(france.bayonne(), france.pau(), 155.5)

    # Stage 12
    builder.road_stage(france.pau(), france.saint_gaudens(), 207.5)

    # Stage 13
    builder.mountain_time_trial(france.luchon())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 18.5)

    # Stage 14
    builder.road_stage(france.luchon(), france.carcassonne(), 215.0)

    # Stage 15
    builder.road_stage(france.carcassonne(), france.montpellier(), 196.5)

    # Stage 16
    builder.road_stage(france.montpellier(), france.aix_en_provence(), 185.0)

    # Stage 17
    builder.road_stage(france.aix_en_provence(), france.antibes(), 201.0)

    # Stage 18
    builder.road_stage(france.antibes(), france.briancon(), 241.5)

    # Stage 19
    builder.road_stage(france.briancon(), france.aix_les_bains(), 204.5)

    # Stage 20
    builder.individual_time_trial(france.bourgoin(), france.lyon(), 68.0)

    # Stage 21
    builder.road_stage(france.lyon(), france.nevers(), 232.0)

    # Stage 22
    builder.road_stage(france.nevers(), france.paris(), 271.0)

    return builder.build()

def tdf1963():

    builder = TourDeFranceBuilder(1963,6,23)

    # Stage 1
    builder.road_stage(france.paris(), france.epernay(), 152.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(france.reims(), belgium.jambes(), 186.0)
    builder.out_and_back_team_time_trial(belgium.jambes(), 22.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(belgium.jambes(), france.roubaix(), 223.0)

    # Stage 4
    builder.road_stage(france.roubaix(), france.rouen(), 236.0)

    # Stage 5
    builder.road_stage(france.rouen(), france.rennes(), 285.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(france.rennes(), france.angers(), 118.0)
    builder.out_and_back_individual_time_trial(france.angers(), 25.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(france.angers(), france.limoges(), 236.0)

    # Stage 8
    builder.road_stage(france.limoges(), france.bordeaux(), 232.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), france.pau(), 202.0)

    # Stage 10
    builder.road_stage(france.pau(), france.bagneres_de_bigorre(), 148.0)

    # Stage 11
    builder.road_stage(france.bagneres_de_bigorre(), france.luchon(), 131.0)

    # Stage 12
    builder.road_stage(france.luchon(), france.toulouse(), 173.0)

    # Stage 13
    builder.road_stage(france.toulouse(), france.aurillac(), 234.0)

    # Rest day
    builder.rest_day(france.aurillac())


    # Stage 14
    builder.road_stage(france.aurillac(), france.saint_etienne(), 237.0)

    # Stage 15
    builder.road_stage(france.saint_etienne(), france.grenoble(), 174.0)

    # Stage 16
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.val_d_isere(), ColCategory.C1, 202.0)

    # Stage 17
    builder.road_stage(mountains.alps.val_d_isere(), france.chamonix(), 228.0)

    # Stage 18
    builder.road_stage(france.chamonix(), france.lons_le_saunier(), 225.0)

    # Stage 19
    builder.individual_time_trial(france.arbois(), france.besancon(), 54.0)

    # Stage 20
    builder.road_stage(france.besancon(), france.troyes(), 234.0)

    # Stage 21
    builder.road_stage(france.troyes(), france.paris(), 185.0)

    return builder.build()

def tdf1964():

    builder = TourDeFranceBuilder(1964,6,22)

    # Stage 1
    builder.road_stage(france.rennes(), france.lisieux(), 215.0)

    # Stage 2
    builder.road_stage(france.lisieux(), france.amiens(), 208.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.road_stage(france.amiens(), belgium.forest(), 197.0)
    builder.out_and_back_team_time_trial(belgium.forest(), 21.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(belgium.forest(), france.metz(), 292.0)

    # Stage 5
    builder.road_stage(france.luneville(), west_germany.freiburg(), 161.0)

    # Stage 6
    builder.road_stage(west_germany.freiburg(), france.besancon(), 200.0)

    # Stage 7
    builder.road_stage(france.besancon(), france.thonon_les_bains(), 195.0)

    # Stage 8
    builder.road_stage(france.thonon_les_bains(), france.briancon(), 249.0)

    # Stage 9
    builder.road_stage(france.briancon(), monaco.monaco(), 239.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.road_stage(monaco.monaco(), france.hyeres(), 187.0)
    builder.individual_time_trial(france.hyeres(), france.toulon(), 21.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(france.toulon(), france.montpellier(), 250.0)

    # Stage 12
    builder.road_stage(france.montpellier(), france.perpignan(), 174.0)

    # Stage 13
    builder.road_stage(france.perpignan(), andorra.andorra_la_vella(), 170.0)

    # Rest day
    builder.rest_day(andorra.andorra_la_vella())

    # Stage 14
    builder.road_stage(andorra.andorra_la_vella(), france.toulouse(), 186.0)

    # Stage 15
    builder.road_stage(france.toulouse(), france.luchon(), 203.0)

    # Stage 16
    builder.road_stage(france.luchon(), france.pau(), 197.0)

    # Stage 17
    builder.individual_time_trial(france.peyrehorade(), france.bayonne(), 43.0)

    # Stage 18
    builder.road_stage(france.bayonne(), france.bordeaux(), 187.0)

    # Stage 19
    builder.road_stage(france.bordeaux(), france.brive(), 215.0)

    # Stage 20
    builder.mountain_stage(france.brive())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 217.0)

    # Stage 21
    builder.road_stage(france.clermont_ferrand(), france.orleans(), 311.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.road_stage(france.orleans(), france.versailles(), 119.0)
    builder.individual_time_trial(france.versailles(), france.paris(), 27.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1965():

    builder = TourDeFranceBuilder(1965,6,22)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(west_germany.cologne(), belgium.liege(), 149.0)
    builder.out_and_back_team_time_trial(belgium.liege(), 22.5)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(belgium.liege(), france.roubaix(), 200.5)

    # Stage 3
    builder.road_stage(france.roubaix(), france.rouen(), 240.0)

    # Stage 4
    builder.road_stage(france.caen(), france.saint_brieuc(), 227.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.saint_brieuc(), france.chateaulin(), 147.0)
    builder.out_and_back_individual_time_trial(france.chateaulin(), 26.7)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(france.quimper(), france.la_baule(), 210.5)

    # Stage 7
    builder.road_stage(france.la_baule(), france.la_rochelle(), 219.0)

    # Stage 8
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 197.5)

    # Stage 9
    builder.road_stage(france.dax(), france.bagneres_de_bigorre(), 226.5)

    # Stage 10
    builder.road_stage(france.bagneres_de_bigorre(), france.ax_les_thermes(), 222.5)

    # Stage 11
    builder.road_stage(france.ax_les_thermes(), spain.barcelona(), 240.5)

    # Rest day
    builder.rest_day(spain.barcelona())


    # Stage 12
    builder.road_stage(spain.barcelona(), france.perpignan(), 219.0)

    # Stage 13
    builder.road_stage(france.perpignan(), france.montpellier(), 164.0)

    # Stage 14
    builder.mountain_stage(france.montpellier())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 173.0)

    # Stage 15
    builder.road_stage(france.carpentras(), france.gap(), 167.5)

    # Stage 16
    builder.road_stage(france.gap(), france.briancon(), 177.0)

    # Stage 17
    builder.road_stage(france.briancon(), france.aix_les_bains(), 193.5)

    # Stage 18
    builder.individual_time_trial(france.aix_les_bains(), france.le_revard(), 26.9)

    # Stage 19
    builder.road_stage(france.aix_les_bains(), france.lyon(), 165.0)

    # Stage 20
    builder.road_stage(france.lyon(), france.auxerre(), 198.5)

    # Stage 21
    builder.road_stage(france.auxerre(), france.versailles(), 225.5)

    # Stage 22
    builder.individual_time_trial(france.versailles(), france.paris(), 37.8)

    return builder.build()

def tdf1966():

    builder = TourDeFranceBuilder(1966,6,21)

    # Stage 1
    builder.road_stage(france.nancy(), france.charleville(), 209.0)

    # Stage 2
    builder.road_stage(france.charleville(), belgium.tournai(), 198.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(belgium.tournai(), 21.0)
    builder.road_stage(belgium.tournai(), france.dunkerque(), 131.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.dunkerque(), france.dieppe(), 205.0)

    # Stage 5
    builder.road_stage(france.dieppe(), france.caen(), 178.0)

    # Stage 6
    builder.road_stage(france.caen(), france.angers(), 217.0)

    # Stage 7
    builder.road_stage(france.angers(), france.royan(), 252.0)

    # Stage 8
    builder.road_stage(france.royan(), france.bordeaux(), 138.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), france.bayonne(), 201.0)

    # Stage 10
    builder.road_stage(france.bayonne(), france.pau(), 234.0)

    # Stage 11
    builder.road_stage(france.pau(), france.luchon(), 188.0)

    # Rest day
    builder.rest_day(france.luchon())

    # Stage 12
    builder.road_stage(france.luchon(), france.revel(), 219.0)

    # Stage 13
    builder.road_stage(france.revel(), france.sete(), 191.0)

    # Stages 14a & 14b
    builder.enable_split_stages()
    builder.road_stage(france.montpellier(), france.vals_les_bains(), 144.0)
    builder.out_and_back_individual_time_trial(france.vals_les_bains(), 20.0)
    builder.disable_split_stages()

    # Stage 15
    builder.road_stage(france.privas(), france.le_bourg_d_oisans(), 203.0)

    # Stage 16
    builder.road_stage(france.le_bourg_d_oisans(), france.briancon(), 148.0)

    # Stage 17
    builder.road_stage(france.briancon(), italy.turin(), 160.0)

    # Rest day
    builder.rest_day(italy.turin())

    # Stage 18
    builder.road_stage(italy.ivrea(), france.chamonix(), 188.0)

    # Stage 19
    builder.road_stage(france.chamonix(), france.saint_etienne(), 265.0)

    # Stage 20
    builder.road_stage(france.saint_etienne(), france.montlucon(), 223.0)

    # Stage 21
    builder.road_stage(france.montlucon(), france.orleans(), 232.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.road_stage(france.orleans(), france.rambouillet(), 111.0)
    builder.individual_time_trial(france.rambouillet(), france.paris(), 51.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1967():

    builder = TourDeFranceBuilder(1967,6,29)

    # Prologue
    builder.out_and_back_prologue(france.angers(), 5.8)
    # Stage 1
    builder.road_stage(france.angers(), france.saint_malo(), 185.5)

    # Stage 2
    builder.road_stage(france.saint_malo(), france.caen(), 180.0)

    # Stage 3
    builder.road_stage(france.caen(), france.amiens(), 248.0)

    # Stage 4
    builder.road_stage(france.amiens(), france.roubaix(), 191.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.roubaix(), belgium.jambes(), 172.0)
    builder.out_and_back_team_time_trial(belgium.jambes(), 17.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(belgium.jambes(), france.metz(), 238.0)

    # Stage 7
    builder.road_stage(france.metz(), france.strasbourg(), 205.5)

    # Stage 8
    builder.road_stage(france.metz(), france.belfort(), 215.0)

    # Rest day
    builder.rest_day(france.belfort())


    # Stage 9
    builder.road_stage(france.belfort(), france.divonne_les_bains(), 238.5)

    # Stage 10
    builder.road_stage(france.divonne_les_bains(), france.briancon(), 243.0)

    # Stage 11
    builder.road_stage(france.briancon(), france.digne(), 197.0)

    # Stage 12
    builder.road_stage(france.digne(), france.marseille(), 207.5)

    # Stage 13
    builder.road_stage(france.marseille(), france.carpentras(), 211.5)

    # Stage 14
    builder.road_stage(france.carpentras(), france.sete(), 201.5)

    # Rest day
    builder.rest_day(france.sete())


    # Stage 15
    builder.road_stage(france.sete(), france.toulouse(), 230.5)

    # Stage 16
    builder.road_stage(france.toulouse(), france.luchon(), 188.0)

    # Stage 17
    builder.road_stage(france.luchon(), france.pau(), 250.0)

    # Stage 18
    builder.road_stage(france.pau(), france.bordeaux(), 206.5)

    # Stage 19
    builder.road_stage(france.bordeaux(), france.limoges(), 217.0)

    # Stage 20
    builder.mountain_stage(france.limoges())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 222.0)

    # Stage 21
    builder.road_stage(france.clermont_ferrand(), france.fontainebleau(), 359.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.road_stage(france.fontainebleau(), france.versailles(), 104.0)
    builder.individual_time_trial(france.versailles(), france.paris(), 46.6)
    builder.disable_split_stages()

    return builder.build()

def tdf1968():

    builder = TourDeFranceBuilder(1968,6,27)

    # Prologue
    builder.out_and_back_prologue(france.vittel(), 6.1)

    # Stage 1
    builder.road_stage(france.vittel(), luxembourg.esch_sur_alzette(), 189.0)

    # Stage 2
    builder.road_stage(belgium.arlon(), belgium.forest(), 210.5)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(belgium.forest(), 22.0)
    builder.road_stage(belgium.forest(), france.roubaix(), 112.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.roubaix(), france.rouen(), 238.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.rouen(), france.bagnoles_de_l_orne(), 165.0)
    builder.road_stage(france.bagnoles_de_l_orne(), france.dinard(), 154.5)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(france.dinard(), france.lorient(), 188.0)

    # Stage 7
    builder.road_stage(france.lorient(), france.nantes(), 190.0)

    # Stage 8
    builder.road_stage(france.nantes(), france.royan(), 233.0)

    # Rest day
    builder.rest_day(france.royan())

    # Stage 9
    builder.road_stage(france.royan(), france.bordeaux(), 137.5)

    # Stage 10
    builder.road_stage(france.bordeaux(), france.bayonne(), 202.5)

    # Stage 11
    builder.road_stage(france.bayonne(), france.pau(), 183.5)

    # Stage 12
    builder.road_stage(france.pau(), france.saint_gaudens(), 226.5)

    # Stage 13
    builder.road_stage(france.saint_gaudens(), spain.la_seu_d_urgell(), 208.5)

    # Stage 14
    builder.road_stage(spain.la_seu_d_urgell(), france.perpignan(), 231.5)

    # Rest day
    builder.rest_day(france.font_romeu_odeillo_via())

    # Stage 15
    builder.road_stage(france.font_romeu_odeillo_via(), france.albi(), 250.5)

    # Stage 16
    builder.road_stage(france.albi(), france.aurillac(), 199.0)

    # Stage 17
    builder.road_stage(france.aurillac(), france.saint_etienne(), 236.5)

    # Stage 18
    builder.road_stage(france.saint_etienne(), france.grenoble(), 235.0)

    # Stage 19
    builder.road_stage(france.grenoble(), france.sallanches(), 200.0)

    # Stage 20
    builder.road_stage(france.sallanches(), france.besancon(), 242.5)

    # Stage 21
    builder.road_stage(france.besancon(), france.auxerre(), 242.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.road_stage(france.auxerre(), france.melun(), 136.0)
    builder.individual_time_trial(france.melun(), france.paris(), 55.2)
    builder.disable_split_stages()

    return builder.build()

def tdf1969():

    builder = TourDeFranceBuilder(1969,6,28)

    # Prologue
    builder.out_and_back_prologue(france.roubaix(), 10.0)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(france.roubaix(), belgium.sint_pieters_woluwe(), 147.0)
    builder.out_and_back_team_time_trial(belgium.sint_pieters_woluwe(), 16.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(belgium.sint_pieters_woluwe(), netherlands.maastricht(), 182.0)

    # Stage 3
    builder.road_stage(netherlands.maastricht(), france.charleville_mezieres(), 213.0)

    # Stage 4
    builder.road_stage(france.charleville_mezieres(), france.nancy(), 214.0)

    # Stage 5
    builder.road_stage(france.nancy(), france.mulhouse(), 194.0)

    # Stage 6
    builder.road_stage(france.mulhouse(), france.ballon_d_alsace(), 133.0)

    # Stage 7
    builder.road_stage(france.belfort(), france.divonne_les_bains(), 241.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.divonne_les_bains(), 9.0)
    builder.road_stage(france.divonne_les_bains(), france.thonon_les_bains(), 137.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(france.thonon_les_bains(), france.chamonix(), 111.0)

    # Stage 10
    builder.road_stage(france.chamonix(), france.briancon(), 221.0)

    # Stage 11
    builder.road_stage(france.briancon(), france.digne(), 198.0)

    # Stage 12
    builder.road_stage(france.digne(), france.aubagne(), 161.0)

    # Stage 13
    builder.road_stage(france.aubagne(), france.la_grande_motte(), 196.0)

    # Stage 14
    builder.road_stage(france.la_grande_motte(), france.revel(), 234.0)

    # Rest day
    builder.rest_day(france.revel())

    # Stage 15
    builder.road_stage(france.castelnaudary(), france.luchon(), 199.0)

    # Stage 16
    builder.road_stage(france.luchon(), france.mourenx(), 214.0)

    # Stage 17
    builder.road_stage(france.mourenx(), france.bordeaux(), 201.0)

    # Stage 18
    builder.road_stage(france.bordeaux(), france.brive(), 193.0)

    # Stage 19
    builder.mountain_stage(france.brive())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 198.0)

    # Stage 20
    builder.road_stage(france.clermont_ferrand(), france.montargis(), 329.0)

    # Stages 21a & 21b
    builder.enable_split_stages()
    builder.road_stage(france.montargis(), france.creteil(), 111.0)
    builder.individual_time_trial(france.creteil(), france.paris(), 37.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1970():

    builder = TourDeFranceBuilder(1970,6,26)

    # Prologue
    builder.out_and_back_prologue(france.limoges(), 7.4)
    # Stage 1
    builder.road_stage(france.limoges(), france.la_rochelle(), 224.0)

    # Stage 2
    builder.road_stage(france.la_rochelle(), france.angers(), 200.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(france.angers(), 10.7)
    builder.road_stage(france.angers(), france.rennes(), 140.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.rennes(), france.lisieux(), 229.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.lisieux(), france.rouen(), 94.5)
    builder.road_stage(france.rouen(), france.amiens(), 223.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(france.amiens(), france.valenciennes(), 135.5)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.road_stage(france.valenciennes(), belgium.forest(), 120.0)
    builder.out_and_back_individual_time_trial(belgium.forest(), 7.2)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(france.ciney(), west_germany.felsberg(), 232.5)

    # Stage 9
    builder.road_stage(west_germany.saarlouis(), france.mulhouse(), 269.5)

    # Stage 10
    builder.road_stage(france.belfort(), france.divonne_les_bains(), 241.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.divonne_les_bains(), 8.8)
    builder.road_stage(france.divonne_les_bains(), france.thonon_les_bains(), 139.5)
    builder.disable_split_stages()

    # Stage 12
    builder.road_stage(france.divonne_les_bains(), france.grenoble(), 194.0)

    # Stage 13
    builder.road_stage(france.grenoble(), france.gap(), 194.5)

    # Stage 14
    builder.mountain_stage(france.gap())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 170.0)

    # Stage 15
    builder.road_stage(france.carpentras(), france.montpellier(), 140.5)

    # Stage 16
    builder.road_stage(france.montpellier(), france.toulouse(), 160.0)

    # Stage 17
    builder.road_stage(france.toulouse(), france.saint_gaudens(), 190.0)

    # Stage 18
    builder.mountain_stage(france.saint_gaudens())
    builder.summit_finish(mountains.pyrenees.la_mongie(), ColCategory.C1, 135.5)

    # Stage 19
    builder.road_stage(france.bagneres_de_bigorre(), france.mourenx(), 185.5)

    # Stages 20a & 20b
    builder.enable_split_stages()
    builder.road_stage(france.mourenx(), france.bordeaux(), 223.5)
    builder.out_and_back_individual_time_trial(france.bordeaux(), 8.2)
    builder.disable_split_stages()

    # Stage 21
    builder.road_stage(france.ruffex(), france.tours(), 191.5)

    # Stage 22
    builder.road_stage(france.tours(), france.versailles(), 238.5)

    # Stage 23
    builder.individual_time_trial(france.versailles(), france.paris(), 54.0)

    return builder.build()

def tdf1971():

    builder = TourDeFranceBuilder(1971,6,26)

    # Prologue
    builder.out_and_back_prologue(france.mulhouse(), 11.0)

    # Stages 1a, 1b & 1c
    builder.enable_split_stages()
    builder.road_stage(france.mulhouse(), switzerland.basel(), 59.5)
    builder.road_stage(switzerland.basel(), west_germany.freiburg(), 90.0)
    builder.road_stage(west_germany.freiburg(), france.mulhouse(), 74.5)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(france.mulhouse(), france.strasbourg(), 144.0)

    # Stage 3
    builder.road_stage(france.strasbourg(), france.nancy(), 165.6)

    # Stage 4
    builder.road_stage(france.nancy(), belgium.marche_en_famenne(), 242.0)

    # Stage 5
    builder.road_stage(belgium.dinant(), france.roubaix(), 208.5)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(france.roubaix(), france.amiens(), 127.5)
    builder.road_stage(france.amiens(), france.le_touquet(), 133.5)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.le_touquet())

    # Stage 7
    builder.road_stage(france.rungis(), france.nevers(), 257.5)

    # Stage 8
    builder.mountain_stage(france.nevers())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 221.0)

    # Stage 9
    builder.road_stage(france.clermont_ferrand(), france.saint_etienne(), 153.0)

    # Stage 10
    builder.road_stage(france.saint_etienne(), france.grenoble(), 188.5)

    # Stage 11
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.orcieres_merlette(), ColCategory.C1, 134.0)

    # Rest day
    builder.rest_day(mountains.alps.orcieres_merlette())

    # Stage 12
    builder.road_stage(mountains.alps.orcieres_merlette(), france.marseille(), 251.0)

    # Stage 13
    builder.criterium(france.albi(), 16.3)

    # Stage 14
    builder.road_stage(france.revel(), france.luchon(), 214.5)

    # Stage 15
    builder.mountain_stage(france.luchon())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 19.6)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(france.luchon(), france.gourette(), 145.0)
    builder.road_stage(france.gourette(), france.pau(), 57.5)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(france.mont_de_marsan(), france.bordeaux(), 188.0)

    # Stage 18
    builder.road_stage(france.bordeaux(), france.poitiers(), 244.0)

    # Stage 19
    builder.road_stage(france.blois(), france.versailles(), 244.0)

    # Stage 20
    builder.individual_time_trial(france.versailles(), france.paris(), 53.8)

    return builder.build()

def tdf1972():

    builder = TourDeFranceBuilder(1972,7,1)

    # Prologue
    builder.out_and_back_prologue(france.angers(), 7.2)

    # Stage 1
    builder.road_stage(france.angers(), france.saint_brieuc(), 235.5)

    # Stage 2
    builder.road_stage(france.saint_brieuc(), france.la_baule(), 206.5)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.road_stage(france.pornichet(), france.saint_jean_de_monts(), 161.0)
    builder.out_and_back_individual_time_trial(france.merlin_plage(), 16.2)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.merlin_plage(), france.royan(), 236.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.royan(), france.bordeaux(), 133.5)
    builder.out_and_back_individual_time_trial(france.bordeaux(), 12.7)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(france.bordeaux(), france.bayonne(), 205.0)

    # Rest day
    builder.rest_day(france.bayonne())

    # Stage 7
    builder.road_stage(france.bayonne(), france.pau(), 220.5)

    # Stage 8
    builder.road_stage(france.pau(), france.luchon(), 163.5)

    # Stage 9
    builder.road_stage(france.luchon(), france.colomiers(), 179.0)

    # Stage 10
    builder.road_stage(france.castres(), france.la_grand_motte(), 210.0)

    # Stage 11
    builder.mountain_stage(france.carnon_plage())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 207.0)

    # Stage 12
    builder.mountain_stage(france.carpentras())
    builder.summit_finish(mountains.alps.orcieres_merlette(), ColCategory.C1, 192.0)

    # Rest day
    builder.rest_day(mountains.alps.orcieres_merlette())

    # Stage 13
    builder.road_stage(mountains.alps.orcieres_merlette(), france.briancon(), 201.0)

    # Stages 14a & 14b
    builder.enable_split_stages()
    builder.road_stage(france.briancon(), france.valloire(), 51.0)
    builder.road_stage(france.valloire(), france.aix_les_bains(), 151.0)
    builder.disable_split_stages()

    # Stage 15
    builder.road_stage(france.aix_les_bains(), france.le_revard(), 28.0)

    # Stage 16
    builder.road_stage(france.aix_les_bains(), france.pontarlier(), 198.5)

    # Stage 17
    builder.road_stage(france.pontarlier(), france.ballon_d_alsace(), 213.0)

    # Stage 18
    builder.road_stage(france.vesoul(), france.auxerre(), 257.5)

    # Stage 19
    builder.road_stage(france.auxerre(), france.versailles(), 230.0)

    # Stages 20a & 20b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.versailles(), 42.0)
    builder.road_stage(france.versailles(), france.paris(), 89.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1973():

    builder = TourDeFranceBuilder(1973,6,30)

    # Prologue
    builder.out_and_back_prologue(netherlands.scheveningen(), 7.1)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(netherlands.scheveningen(), netherlands.rotterdam(), 84.0)
    builder.road_stage(netherlands.rotterdam(), belgium.sint_niklaas(), 137.5)
    builder.disable_split_stages()

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(belgium.sint_niklaas(), 12.4)
    builder.road_stage(belgium.sint_niklaas(), france.roubaix(), 138.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(france.roubaix(), france.reims(), 226.0)

    # Stage 4
    builder.road_stage(france.reims(), france.nancy(), 214.0)

    # Stage 5
    builder.road_stage(france.nancy(), france.mulhouse(), 188.0)

    # Stage 6
    builder.road_stage(france.mulhouse(), france.divonne_les_bains(), 244.5)

    # Rest day
    builder.rest_day(france.divonne_les_bains())

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.road_stage(france.divonne_les_bains(), france.gaillard(), 86.5)
    builder.mountain_stage(france.gaillard())
    builder.summit_finish(mountains.alps.meribel_les_allues(), ColCategory.C1, 150.5)
    builder.disable_split_stages()

    # Stage 8
    builder.mountain_stage(france.moutiers())
    builder.summit_finish(mountains.alps.les_orres(), ColCategory.C1, 237.5)

    # Stage 9
    builder.road_stage(france.embrun(), france.nice(), 234.5)

    # Stage 10
    builder.road_stage(france.nice(), france.aubagne(), 222.5)

    # Stage 11
    builder.road_stage(france.montpellier(), france.argeles_sur_mer(), 238.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.individual_time_trial(france.perpignan(), france.thuir(), 28.3)
    builder.mountain_stage(france.thuir())
    builder.summit_finish(mountains.pyrenees.pyrenees2000(), ColCategory.C1, 76.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(mountains.pyrenees.pyrenees2000())

    # Stage 13
    builder.road_stage(france.bourg_madame(), france.luchon(), 235.0)

    # Stage 14
    builder.road_stage(france.luchon(), france.pau(), 227.5)

    # Stage 15
    builder.road_stage(france.pau(), france.fleurance(), 137.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(france.fleurance(), france.bordeaux(), 210.0)
    builder.out_and_back_individual_time_trial(france.bordeaux(), 12.4)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(france.sainte_foy_la_grande(), france.brive_la_gaillarde(), 248.0)

    # Stage 18
    builder.mountain_stage(france.brive_la_gaillarde())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 216.5)

    # Stage 19
    builder.road_stage(france.bourges(), france.versailles(), 233.5)

    # Stages 20a & 20b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.versailles(), 16.0)
    builder.road_stage(france.versailles(), france.paris(), 89.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1974():

    builder = TourDeFranceBuilder(1974,6,27)

    # Prologue
    builder.out_and_back_prologue(france.brest(), 7.0)
    # Stage 1
    builder.road_stage(france.brest(), france.saint_pol_de_leon(), 144.0)

    # Stage 2
    builder.criterium(united_kingdom.plymouth(), 164.0)

    # Stage 3
    builder.road_stage(france.morlaix(), france.saint_malo(), 190.0)

    # Stage 4
    builder.road_stage(france.saint_malo(), france.caen(), 184.0)

    # Stage 5
    builder.road_stage(france.caen(), france.dieppe(), 165.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(france.dieppe(), belgium.harelbeke(), 239.0)
    builder.out_and_back_team_time_trial(belgium.harelbeke(), 9.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(belgium.mons(), france.chalons_sur_marne(), 221.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(france.chalons_sur_marne(), france.chaumont(), 136.0)
    builder.road_stage(france.chaumont(), france.besancon(), 152.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(france.besancon(), france.gaillard(), 241.0)

    # Stage 10
    builder.road_stage(france.gaillard(), france.aix_les_bains(), 131.0)

    # Stage 11
    builder.road_stage(france.aix_les_bains(), france.serre_chevalier(), 199.0)

    # Rest day
    builder.rest_day(france.aix_les_bains())


    # Stage 12
    builder.road_stage(france.savines_le_lac(), france.orange(), 231.0)

    # Stage 13
    builder.road_stage(france.avignon(), france.montpellier(), 126.0)

    # Stage 14
    builder.road_stage(france.lodeve(), france.colomiers(), 249.0)

    # Rest day
    builder.rest_day(france.colomiers())


    # Stage 15
    builder.road_stage(france.colomiers(), spain.la_seu_d_urgell(), 225.0)

    # Stage 16
    builder.mountain_stage(spain.la_seu_d_urgell())
    builder.summit_finish(france.saint_lary_soulan_pla_d_adet(), ColCategory.C1, 209.0)

    # Stage 17
    builder.mountain_stage(france.saint_lary_soulan())
    builder.summit_finish(mountains.pyrenees.la_mongie(), ColCategory.C1, 119.0)

    # Stage 18
    builder.road_stage(france.bagneres_de_bigorre(), france.pau(), 141.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(france.pau(), france.bordeaux(), 196.0)
    builder.out_and_back_individual_time_trial(france.bordeaux(), 12.0)
    builder.disable_split_stages()

    # Stage 20
    builder.road_stage(france.saint_gilles_croix_de_vie(), france.nantes(), 120.0)

    # Stages 21a & 21b
    builder.enable_split_stages()
    builder.road_stage(france.vouvray(), france.orleans(), 113.0)
    builder.out_and_back_individual_time_trial(france.orleans(), 37.0)
    builder.disable_split_stages()

    # Stage 22
    builder.road_stage(france.orleans(), france.paris(), 146.0)

    return builder.build()

def tdf1975():

    builder = TourDeFranceBuilder(1975,6,26)

    # Prologue
    builder.out_and_back_prologue(belgium.charleroi(), 6.0)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(belgium.charleroi(), belgium.molenbeek(), 94.0)
    builder.road_stage(belgium.molenbeek(), france.roubaix(), 109.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(france.roubaix(), france.amiens(), 121.0)

    # Stage 3
    builder.road_stage(france.amiens(), france.versailles(), 170.0)

    # Stage 4
    builder.road_stage(france.versailles(), france.le_mans(), 223.0)

    # Stage 5
    builder.road_stage(france.sable_sur_sarthe(), france.merlin_plage(), 222.0)

    # Stage 6
    builder.out_and_back_individual_time_trial(france.merlin_plage(), 16.0)

    # Stage 7
    builder.road_stage(france.saint_gilles_croix_de_vie(), france.angouleme(), 236.0)

    # Stage 8
    builder.road_stage(france.angouleme(), france.bordeaux(), 134.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.road_stage(france.langon(), france.fleurance(), 131.0)
    builder.individual_time_trial(france.fleurance(), france.auch(), 37.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.auch())

    # Stage 10
    builder.road_stage(france.auch(), france.pau(), 206.0)

    # Stage 11
    builder.mountain_stage(france.pau())
    builder.summit_finish(france.saint_lary_soulan_pla_d_adet(), ColCategory.HC, 160.0)

    # Stage 12
    builder.road_stage(france.tarbes(), france.albi(), 242.0)

    # Stage 13
    builder.mountain_stage(france.albi())
    builder.summit_finish(mountains.massif_central.le_lioran(), ColCategory.C1, 260.0)

    # Stage 14
    builder.mountain_stage(france.aurillac())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 174.0)

    # Rest day
    builder.rest_day(france.nice())

    # Stage 15
    builder.mountain_stage(france.nice())
    builder.summit_finish(mountains.alps.pra_loup(), ColCategory.C1, 217.0)

    # Stage 16
    builder.road_stage(france.barcelonette(), france.serre_chevalier(), 107.0)

    # Stage 17
    builder.road_stage(france.valloire(), france.morzine_avoriaz(), 225.0)

    # Stage 18
    builder.individual_time_trial(france.morzine(), france.chatel(), 40.0)

    # Stage 19
    builder.road_stage(france.thonon_les_bains(), france.chalon_sur_saone(), 229.0)

    # Stage 20
    builder.road_stage(france.pouilly_en_auxois(), france.melun(), 256.0)

    # Stage 21
    builder.road_stage(france.melun(), france.senlis(), 220.0)

    # Stage 22
    builder.criterium(france.paris(), 164.0)

    return builder.build()

def tdf1976():
    builder = TourDeFranceBuilder(1976,6,24)

    # Prologue
    builder.out_and_back_prologue(france.saint_jean_de_monts(), 8.0)

    # Stage 1
    builder.road_stage(france.saint_jean_de_monts(), france.angers(), 173.0)

    # Stage 2
    builder.road_stage(france.angers(), france.caen(), 237.0)

    # Stage 3
    builder.out_and_back_individual_time_trial(france.le_touquet_paris_plage(), 37.0)

    # Stage 4
    builder.road_stage(france.le_touquet_paris_plage(), belgium.bornem(), 258.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(belgium.leuven(), 4.0)
    builder.road_stage(belgium.leuven(), belgium.verviers(), 144.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(belgium.bastogne(), france.nancy(), 209.0)

    # Stage 7
    builder.road_stage(france.nancy(), france.mulhouse(), 206.0)

    # Stage 8
    builder.road_stage(france.valentigney(), france.divonne_les_bains(), 220.0)

    # Rest day
    builder.rest_day(france.divonne_les_bains())

    # Stage 9
    builder.mountain_stage(france.divonne_les_bains())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 258.0)

    # Stage 10
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.montgenevre(), ColCategory.C1, 166.0)

    # Stage 11
    builder.road_stage(mountains.alps.montgenevre(), france.manosque(), 224.0)

    # Rest day
    builder.rest_day(france.le_barcares())

    # Stage 12
    builder.mountain_stage(france.le_barcares())
    builder.summit_finish(mountains.pyrenees.pyrenees2000(), ColCategory.C1, 205.0)

    # Stage 13
    builder.road_stage(mountains.pyrenees.pyrenees2000(), france.saint_gaudens(), 188.0)

    # Stage 14
    builder.road_stage(france.saint_gaudens(), france.saint_lary_soulan(), 139.0)

    # Stage 15
    builder.road_stage(france.saint_lary_soulan(), france.pau(), 195.0)

    # Stage 16
    builder.road_stage(france.pau(), france.fleurance(), 152.0)

    # Stage 17
    builder.individual_time_trial(france.fleurance(), france.auch(), 39.0)

    # Stages 18a, 18b & 18c
    builder.enable_split_stages()
    builder.road_stage(france.auch(), france.langon(), 86.0)
    builder.road_stage(france.langon(), france.lacanau(), 123.0)
    builder.road_stage(france.lacanau(), france.bordeaux(), 70.0)
    builder.disable_split_stages()

    # Stage 19
    builder.road_stage(france.sainte_foy_la_grande(), france.tulle(), 220.0)

    # Stage 20
    builder.mountain_stage(france.tulle())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 220.0)

    # Stage 21
    builder.road_stage(france.montargis(), france.versailles(), 145.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.paris(), 6.0)
    builder.criterium(france.paris(), 91.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1977():
    builder = TourDeFranceBuilder(1977,6,30)

    # Prologue
    builder.out_and_back_prologue(france.fleurance(), 5.0)

    # Stage 1
    builder.road_stage(france.fleurance(), france.auch(), 237.0)

    # Stage 2
    builder.road_stage(france.auch(), france.pau(), 253.0)

    # Stage 3
    builder.road_stage(france.oloron_sainte_marie(), spain.vitoria_gasteiz(), 248.0)

    # Stage 4
    builder.road_stage(spain.vitoria_gasteiz(), france.seignosse_le_penon(), 256.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.road_stage(france.morcenx(), france.bordeaux(), 139.0)
    builder.out_and_back_individual_time_trial(france.bordeaux(), 30.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(france.bordeaux())

    # Stage 6
    builder.road_stage(france.bordeaux(), france.limoges(), 225.0)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.road_stage(france.jaunay_clan(), france.angers(), 140.0)
    builder.out_and_back_team_time_trial(france.angers(), 4.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(france.angers(), france.lorient(), 247.0)

    # Stage 9
    builder.road_stage(france.lorient(), france.rennes(), 187.0)

    # Stage 10
    builder.road_stage(france.bagnoles_de_l_orne(), france.rouen(), 174.0)

    # Stage 11
    builder.road_stage(france.rouen(), france.roubaix(), 242.0)

    # Stage 12
    builder.road_stage(france.roubaix(), belgium.charleroi(), 193.0)

    # Stages 13a & 13b
    builder.enable_split_stages()
    builder.criterium(west_germany.freiburg(), 46.0)
    builder.road_stage(france.altkirch(), france.besancon(), 160.0)
    builder.disable_split_stages()

    # Rest day
    builder.rest_day(west_germany.freiburg())

    # Stage 14
    builder.road_stage(france.besancon(), france.thonon_les_bains(), 230.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(france.thonon_les_bains(), france.morzine(), 105.0)
    builder.mountain_time_trial(france.morzine())
    builder.summit_finish(france.avoriaz(), ColCategory.C1, 14.0)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(france.morzine(), france.chamonix(), 121.0)

    # Stage 17
    builder.mountain_stage(france.chamonix())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 185.0)

    # Stage 18
    builder.road_stage(france.rossignol_voiron(), france.saint_etienne(), 199.0)

    # Stage 19
    builder.road_stage(france.saint_trivier_sur_moignans(), france.dijon(), 172.0)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.dijon(), 50.0)

    # Stage 21
    builder.road_stage(france.montereau_fault_yonne(), france.versailles(), 142.0)

    # Stages 22a & 22b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(france.paris(), 6.0)
    builder.criterium(france.paris(), 91.0)
    builder.disable_split_stages()

    return builder.build()

def tdf1978():
    builder = TourDeFranceBuilder(1978,6,29)

    # Prologue
    builder.out_and_back_prologue(netherlands.leiden(), 5.0)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(netherlands.leiden(), netherlands.sint_willebrord(), 135.0)
    builder.road_stage(netherlands.sint_willebrord(), belgium.brussels(), 100.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(belgium.brussels(), france.saint_amand_les_eaux(), 199.0)

    # Stage 3
    builder.road_stage(france.saint_amand_les_eaux(), france.saint_germain_en_laye(), 244.0)

    # Stage 4
    builder.team_time_trial(france.evreux(), france.caen(), 153.0)

    # Stage 5
    builder.road_stage(france.caen(), france.maze_montgeoffroy(), 244.0)

    # Stage 6
    builder.road_stage(france.maze_montgeoffroy(), france.poitiers(), 162.0)

    # Stage 7
    builder.road_stage(france.poitiers(), france.bordeaux(), 242.0)

    # Stage 8
    builder.individual_time_trial(france.saint_emilion(), france.sainte_foy_la_grande(), 59.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), france.biarritz(), 233.0)

    # Rest day
    builder.rest_day(france.biarritz())

    # Stage 10
    builder.road_stage(france.biarritz(), france.pau(), 192.0)

    # Stage 11
    builder.road_stage(france.pau(), france.saint_lary_soulan_pla_d_adet(), 161.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.road_stage(france.tarbes(), france.valence_d_agen(), 158.0)
    builder.road_stage(france.valence_d_agen(), france.toulouse(), 96.0)
    builder.disable_split_stages()

    # Stage 13
    builder.mountain_stage(france.figeac())
    builder.summit_finish(mountains.massif_central.super_besse(), ColCategory.C3, 221.0)

    # Stage 14
    builder.mountain_time_trial(france.besse_en_chandesse())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 52.0)

    # Stage 15
    builder.road_stage(france.saint_dier_d_auvergne(), france.saint_etienne(), 196.0)

    # Stage 16
    builder.mountain_stage(france.saint_etienne())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 241.0)

    # Rest day
    builder.rest_day(mountains.alps.alpe_d_huez())

    # Stage 17
    builder.road_stage(france.grenoble(), france.morzine(), 225.0)

    # Stage 18
    builder.road_stage(france.morzine(), switzerland.lausanne(), 137.0)

    # Stage 19
    builder.road_stage(switzerland.lausanne(), france.belfort(), 182.0)

    # Stage 20
    builder.individual_time_trial(france.metz(), france.nancy(), 72.0)

    # Stage 21
    builder.road_stage(france.epernay(), france.senlis(), 207.0)

    # Stage 22
    builder.road_stage(france.saint_germain_en_laye(), france.paris(), 162.0)

    return builder.build()

def tdf1979():
    builder = TourDeFranceBuilder(1979,6,27)

    # Prologue
    builder.out_and_back_prologue(france.fleurance(), 5)

    # Stage 1
    builder.road_stage(france.fleurance(), france.luchon(), 225)

    # Stage 2
    builder.mountain_time_trial(france.luchon())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 24)

    # Stage 3
    builder.road_stage(france.luchon(), france.pau(), 180)

    # Stage 4
    builder.team_time_trial(france.captieux(), france.bordeaux(), 87)

    # Stage 5
    builder.road_stage(france.neuville_de_poitou(), france.angers(), 145)

    # Stage 6
    builder.road_stage(france.angers(), france.saint_brieuc(), 239)

    # Stage 7
    builder.road_stage(france.saint_hilaire_du_harcouet(), france.deauville(), 158)

    # Stage 8
    builder.team_time_trial(france.deauville(), france.le_havre(), 90)

    # Stage 9
    builder.road_stage(france.amiens(), france.roubaix(), 201)

    # Stage 10
    builder.road_stage(france.roubaix(), belgium.brussels(), 124)

    # Stage 11
    builder.out_and_back_individual_time_trial(belgium.brussels(), 33)

    # Stage 12
    builder.road_stage(belgium.rochefort(), france.metz(), 193)

    # Stage 13
    builder.road_stage(france.metz(), france.ballon_d_alsace(), 202)

    # Stage 14
    builder.road_stage(france.belfort(), france.evian_les_bains(), 248)

    # Stage 15
    builder.individual_time_trial(france.evian_les_bains(), france.morzine_avoriaz(), 54)

    # Stage 16
    builder.mountain_stage(france.morzine_avoriaz())
    builder.summit_finish(mountains.alps.les_menuires(), ColCategory.C1, 201)

    builder.rest_day(mountains.alps.les_menuires())

    # Stage 17
    alpe_d_huez = mountains.alps.alpe_d_huez()

    builder.mountain_stage(mountains.alps.les_menuires())
    builder.summit_finish(alpe_d_huez, ColCategory.HC, 167)

    # Stage 18
    builder.mountain_stage(alpe_d_huez)
    builder.summit_finish(alpe_d_huez, ColCategory.HC, 119)

    # Stage 19
    builder.road_stage(alpe_d_huez, france.saint_priest(), 162)

    # Stage 20
    builder.road_stage(france.saint_priest(), france.dijon(), 240)

    # Stage 21
    builder.out_and_back_individual_time_trial(france.dijon(), 49)

    # Stage 22
    builder.road_stage(france.dijon(), france.auxerre(), 189)

    # Stage 23
    builder.road_stage(france.auxerre(), france.nogent_sur_marne(), 205)

    # Stage 24
    builder.road_stage(france.le_perreux_sur_marne(), france.paris(), 180)

    return builder.build()

def tdf1980():

    builder = TourDeFranceBuilder(1980,6,26)

    # Prologue
    builder.out_and_back_prologue(west_germany.frankfurt(), 8.0)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(west_germany.frankfurt(), west_germany.wiesbaden(), 133.0)
    builder.team_time_trial(west_germany.wiesbaden(), west_germany.frankfurt(), 46.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(west_germany.frankfurt(), france.metz(), 276.0)

    # Stage 3
    builder.road_stage(france.metz(), belgium.liege(), 282.0)

    # Stage 4
    builder.out_and_back_individual_time_trial(belgium.spa(), 35.0)

    # Stage 5
    builder.road_stage(belgium.liege(), france.lille(), 249.0)

    # Stage 6
    builder.road_stage(france.lille(), france.compiegne(), 216.0)

    # Stages 7a & 7b
    builder.enable_split_stages()
    builder.team_time_trial(france.compiegne(), france.beauvais(), 65.0)
    builder.road_stage(france.beauvais(), france.rouen(), 92.0)
    builder.disable_split_stages()

    # Stage 8
    builder.road_stage(france.flers(), france.saint_malo(), 164.0)

    # Rest day
    builder.rest_day(france.saint_malo())

    # Stage 9
    builder.road_stage(france.saint_malo(), france.nantes(), 205.0)

    # Stage 10
    builder.road_stage(france.rochefort(), france.bordeaux(), 163.0)

    # Stage 11
    builder.individual_time_trial(france.damazan(), france.laplume(), 52.0)

    # Stage 12
    builder.road_stage(france.agen(), france.pau(), 194.0)

    # Stage 13
    builder.road_stage(france.pau(), france.bagneres_de_luchon(), 200.0)

    # Stage 14
    builder.road_stage(france.lezignan_corbieres(), france.montpellier(), 189.0)

    # Stage 15
    builder.road_stage(france.montpellier(), france.martigues(), 160.0)

    # Stage 16
    builder.mountain_stage(france.trets())
    builder.summit_finish(mountains.alps.pra_loup(), ColCategory.C1, 209.0)

    # Stage 17
    builder.road_stage(france.serre_chevalier(), france.morzine(), 242.0)

    # Rest day
    builder.rest_day(france.morzine())

    # Stage 18
    builder.road_stage(france.morzine(), france.prapoutel(), 199.0)

    # Stage 19
    builder.road_stage(france.voreppe(), france.saint_etienne(), 140.0)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.saint_etienne(), 34.0)

    # Stage 21
    builder.road_stage(france.auxerre(), france.fontenay_sous_bois(), 208.0)

    # Stage 22
    builder.road_stage(france.fontenay_sous_bois(), france.paris(), 186.0)

    return builder.build()

def tdf1981():

    builder = TourDeFranceBuilder(1981,6,25)

    # Prologue
    builder.out_and_back_prologue(france.nice(), 6.0)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.criterium(france.nice(), 97.0)
    builder.out_and_back_team_time_trial(france.nice(), 40.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(france.nice(), france.martigues(), 254.0)

    # Stage 3
    builder.road_stage(france.martigues(), france.narbonne(), 232.0)

    # Stage 4
    builder.team_time_trial(france.narbonne(), france.carcassonne(), 77.0)

    # Stage 5
    builder.road_stage(france.saint_gaudens(), france.pla_d_adet(), 117.0)

    # Stage 6
    builder.individual_time_trial(france.nay(), france.pau(), 27.0)

    # Stage 7
    builder.road_stage(france.pau(), france.bordeaux(), 227.0)

    # Stage 8
    builder.road_stage(france.rochefort(), france.nantes(), 182.0)

    # Rest day
    builder.rest_day(france.nantes())

    # Stage 9
    builder.road_stage(france.nantes(), france.le_mans(), 197.0)

    # Stage 10
    builder.road_stage(france.le_mans(), france.aulnay_sous_bois(), 264.0)

    # Stage 11
    builder.road_stage(france.compiegne(), france.roubaix(), 246.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.road_stage(france.roubaix(), belgium.brussels(), 107.0)
    builder.road_stage(belgium.brussels(), belgium.circuit_zolder(), 138.0)
    builder.disable_split_stages()

    # Stage 13
    builder.road_stage(belgium.beringen(), belgium.hasselt(), 157.0)

    # Stage 14
    builder.out_and_back_individual_time_trial(france.mulhouse(), 38.0)

    # Stage 15
    builder.road_stage(france.besancon(), france.thonon_les_bains(), 231.0)

    # Stage 16
    builder.road_stage(france.thonon_les_bains(), france.morzine(), 200.0)

    # Rest day
    builder.rest_day(france.morzine())

    # Stage 17
    builder.mountain_stage(france.morzine())

    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 230.0)

    # Stage 18
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.le_pleynet(), ColCategory.C1, 134.0)

    # Stage 19
    builder.road_stage(france.veurey(), france.saint_priest(), 118.0)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.saint_priest(), 46.0)

    # Stage 21
    builder.road_stage(france.auxerre(), france.fontenay_sous_bois(), 207.0)

    # Stage 22
    builder.road_stage(france.fontenay_sous_bois(), france.paris(), 187.0)

    return builder.build()

def tdf1982():

    builder = TourDeFranceBuilder(1982,7,2)

    # Prologue
    builder.out_and_back_prologue(switzerland.basel(), 7.0)

    # Stage 1
    builder.road_stage(switzerland.basel(), switzerland.mohin(), 207.0)

    # Stage 2
    builder.road_stage(switzerland.basel(), france.nancy(), 250.0)

    # Stage 3
    builder.road_stage(france.nancy(), france.longwy(), 134.0)

    # Stage 4
    builder.road_stage(belgium.beauraing(), belgium.mouscron(), 219.0)

    # Stage 5
    builder.team_time_trial(france.orchies(), france.fontaine_au_pire(), 73.0)

    # Stage 6
    builder.criterium(france.lille(), 233.0)

    # Rest day
    builder.rest_day(france.lille())

    # Stage 7
    builder.road_stage(france.cancale(), france.concarneau(), 235.0)

    # Stage 8
    builder.road_stage(france.concarneau(), france.chateaulin(), 201.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.team_time_trial(france.lorient(), france.plumelec(), 69.0)
    builder.road_stage(france.plumelec(), france.nantes(), 138.0)
    builder.disable_split_stages()

    # Stage 10
    builder.road_stage(france.saintes(), france.bordeaux(), 147.0)

    # Stage 11
    builder.out_and_back_individual_time_trial(france.valence_d_agen(), 57.0)

    # Stage 12
    builder.road_stage(france.fleurance(), france.pau(), 249.0)

    # Stage 13
    builder.road_stage(france.pau(), france.saint_lary_soulan_pla_d_adet(), 122.0)

    # Rest day
    builder.rest_day(france.martigues())

    # Stage 14
    builder.out_and_back_individual_time_trial(france.martigues(), 33.0)

    # Stage 15
    builder.mountain_stage(france.manosque())
    builder.summit_finish(mountains.alps.orcieres_merlette(), ColCategory.C1, 208.0)

    # Stage 16
    builder.mountain_stage(mountains.alps.orcieres_merlette())

    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 123.0)

    # Stage 17
    builder.road_stage(france.le_bourg_d_oisans(), france.morzine(), 251.0)

    # Stage 18
    builder.road_stage(france.morzine(), france.saint_priest(), 233.0)

    # Stage 19
    builder.out_and_back_individual_time_trial(france.saint_priest(), 48.0)

    # Stage 20
    builder.road_stage(france.sens(), france.aulnay_sous_bois(), 161.0)

    # Stage 21
    builder.road_stage(france.fontenay_sous_bois(), france.paris(), 187.0)

    return builder.build()

def tdf1983():

    builder = TourDeFranceBuilder(1983,7,1)

    # Prologue
    builder.out_and_back_prologue(france.fontenay_sous_bois(), 6.0)

    # Stage 1
    builder.road_stage(france.nogent_sur_marne(), france.creteil(), 163.0)

    # Stage 2
    builder.road_stage(france.soissons(), france.fontaine_au_pire(), 100.0)

    # Stage 3
    builder.road_stage(france.valenciennes(), france.roubaix(), 152.0)

    # Stage 4
    builder.road_stage(france.roubaix(), france.le_havre(), 300.0)

    # Stage 5
    builder.road_stage(france.le_havre(), france.le_mans(), 257.0)

    # Stage 6
    builder.individual_time_trial(france.chateaubriant(), france.nantes(), 58.0)

    # Stage 7
    builder.road_stage(france.nantes(), france.ile_d_oleron(), 216.0)

    # Stage 8
    builder.road_stage(france.la_rochelle(), france.bordeaux(), 222.0)

    # Stage 9
    builder.road_stage(france.bordeaux(), france.pau(), 207.0)

    # Stage 10
    builder.road_stage(france.pau(), france.bagneres_de_luchon(), 201.0)

    # Stage 11
    builder.road_stage(france.bagneres_de_luchon(), france.fleurance(), 177.0)

    # Stage 12
    builder.road_stage(france.fleurance(), france.roquefort_sur_soulzon(), 261.0)

    # Stage 13
    builder.road_stage(france.roquefort_sur_soulzon(), france.aurillac(), 210.0)

    # Stage 14
    builder.road_stage(france.aurillac(), france.issoire(), 149.0)

    # Stage 15
    builder.mountain_time_trial(france.clermont_ferrand())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.HC, 16.0)

    # Stage 16
    builder.road_stage(france.issoire(), france.saint_etienne(), 144.0)

    # Stage 17
    builder.mountain_stage(france.la_tour_du_pin())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 233.0)

    # Rest day
    builder.rest_day(mountains.alps.alpe_d_huez())

    # Stage 18
    builder.road_stage(france.le_bourg_d_oisans(), france.morzine(), 247.0)

    # Stage 19
    builder.mountain_time_trial(france.morzine())
    builder.summit_finish(france.avoriaz(), ColCategory.C1, 15.0)

    # Stage 20
    builder.road_stage(france.morzine(), france.dijon(), 291.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(france.dijon(), 50.0)

    # Stage 22
    builder.road_stage(france.alfortville(), france.paris(), 195.0)

    return builder.build()

def tdf1984():

    builder = TourDeFranceBuilder(1984,6,29)

    # Prologue
    builder.prologue(france.montreuil(), france.noisy_le_sec(), 5.0)

    # Stage 1
    builder.road_stage(france.bondy(), france.saint_denis(), 149.0)

    # Stage 2
    builder.road_stage(france.bobigny(), france.louvroil(), 249.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.team_time_trial(france.louvroil(), france.valenciennes(), 51.0)
    builder.road_stage(france.valenciennes(), france.bethune(), 83.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(france.bethune(), france.cergy_pontoise(), 207.0)

    # Stage 5
    builder.road_stage(france.cergy_pontoise(), france.alencon(), 202.0)

    # Stage 6
    builder.individual_time_trial(france.alencon(), france.le_mans(), 67.0)

    # Stage 7
    builder.road_stage(france.le_mans(), france.nantes(), 192.0)

    # Stage 8
    builder.road_stage(france.nantes(), france.bordeaux(), 338.0)

    # Stage 9
    builder.road_stage(france.langon(), france.pau(), 198.0)

    # Stage 10
    builder.mountain_stage(france.pau())

    builder.summit_finish(mountains.pyrenees.guzet_neige(), ColCategory.C1, 227.0)

    # Stage 11
    builder.road_stage(france.saint_girons(), france.blagnac(), 111.0)

    # Stage 12
    builder.road_stage(france.blagnac(), france.rodez(), 220.0)

    # Stage 13
    builder.road_stage(france.rodez(), france.domaine_du_rouret(), 228.0)

    # Stage 14
    builder.road_stage(france.domaine_du_rouret(), france.grenoble(), 241.0)

    # Rest day
    builder.rest_day(france.grenoble())

    # Stage 15
    builder.mountain_time_trial(france.les_echelles())
    builder.summit_finish(mountains.alps.la_ruchere(), ColCategory.C1, 22.0)

    # Stage 16
    builder.mountain_stage(france.grenoble())

    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 151.0)

    # Stage 17
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.la_plagne(), ColCategory.HC, 185.0)

    # Stage 18
    builder.road_stage(mountains.alps.la_plagne(), france.morzine(), 186.0)

    # Stage 19
    builder.mountain_stage(france.morzine())
    builder.summit_finish(mountains.alps.crans_montana(), ColCategory.C1, 141.0)

    # Stage 20
    builder.road_stage(mountains.alps.crans_montana(), france.villefranche_sur_saone(), 320.0)

    # Stage 21
    builder.individual_time_trial(france.villie_morgon(), france.villefranche_sur_saone(), 51.0)

    # Stage 22
    builder.road_stage(france.pantin(), france.paris(), 197.0)

    return builder.build()

def tdf1985():

    builder = TourDeFranceBuilder(1985,6,28)

    # Prologue
    builder.out_and_back_prologue(france.plumelec(), 6.0)

    # Stage 1
    builder.road_stage(france.vannes(), france.lanester(), 256.0)

    # Stage 2
    builder.road_stage(france.lorient(), france.vitre(), 242.0)

    # Stage 3
    builder.road_stage(france.vitre(), france.fougeres(), 242.0)

    # Stage 4
    builder.road_stage(france.fougeres(), france.pont_audemer(), 239.0)

    # Stage 5
    builder.road_stage(france.neufchatel_en_bray(), france.roubaix(), 224.0)

    # Stage 6
    builder.road_stage(france.roubaix(), france.reims(), 222.0)

    # Stage 7
    builder.road_stage(france.reims(), france.nancy(), 217.0)

    # Stage 8
    builder.individual_time_trial(france.sarrebourg(), france.strasbourg(), 75.0)

    # Stage 9
    builder.road_stage(france.strasbourg(), france.epinal(), 174.0)

    # Stage 10
    builder.road_stage(france.epinal(), france.pontarlier(), 204.0)

    # Stage 11
    builder.road_stage(france.pontarlier(), france.morzine_avoriaz(), 195.0)

    # Stage 12
    builder.mountain_stage(france.morzine_avoriaz())
    builder.summit_finish(mountains.alps.lans_en_vercors(), ColCategory.C1, 269.0)

    # Stage 13
    builder.out_and_back_individual_time_trial(mountains.alps.villard_de_lans(), 32.0)

    # Rest day
    builder.rest_day(mountains.alps.villard_de_lans())

    # Stage 14
    builder.road_stage(france.autrans(), france.saint_etienne(), 179.0)

    # Stage 15
    builder.road_stage(france.saint_etienne(), france.aurillac(), 238.0)

    # Stage 16
    builder.road_stage(france.aurillac(), france.toulouse(), 247.0)

    # Stage 17
    builder.mountain_stage(france.toulouse())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 209.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(france.luz_saint_sauveur(), france.aubisque(), 53.0)
    builder.road_stage(france.laruns(), france.pau(), 83.0)
    builder.disable_split_stages()

    # Stage 19
    builder.road_stage(france.pau(), france.bordeaux(), 203.0)

    # Stage 20
    builder.road_stage(france.montpon_menesterol(), france.limoges(), 225.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(france.lac_de_vassiviere(), 46.0)

    # Stage 22
    builder.road_stage(france.orleans(), france.paris(), 196.0)

    return builder.build()

def tdf1986():

    builder = TourDeFranceBuilder(1986,7,4)

    # Prologue
    builder.out_and_back_prologue(france.boulogne_billancourt(), 4.6)

    # Stage 1
    builder.enable_morning_stage()
    builder.road_stage(france.nanterre(), france.sceaux(), 85.0)

    # Stage 2
    builder.team_time_trial(france.meudon(), france.saint_quentin_en_yvelines(), 56.0)

    # Stage 3
    builder.road_stage(france.levallois_perret(), france.lievin(), 214.0)

    # Stage 4
    builder.road_stage(france.lievin(), france.evreux(), 243.0)

    # Stage 5
    builder.road_stage(france.evreux(), france.villers_sur_mer(), 124.5)

    # Stage 6
    builder.road_stage(france.villers_sur_mer(), france.cherbourg(), 200.0)

    # Stage 7
    builder.road_stage(france.cherbourg(), france.saint_hilaire_du_harcouet(), 201.0)

    # Stage 8
    builder.road_stage(france.saint_hilaire_du_harcouet(), france.nantes(), 204.0)

    # Stage 9
    builder.out_and_back_individual_time_trial(france.nantes(), 61.5)

    # Stage 10
    builder.road_stage(france.nantes(), france.futuroscope(), 183.0)

    # Stage 11
    builder.road_stage(france.futuroscope(), france.bordeaux(), 258.3)

    # Stage 12
    builder.road_stage(france.bayonne(), france.pau(), 217.5)

    # Stage 13
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 186.0)

    # Stage 14
    builder.road_stage(mountains.pyrenees.superbagneres(), france.blagnac(), 154.0)

    # Stage 15
    builder.road_stage(france.carcassonne(), france.nimes(), 225.5)

    # Stage 16
    builder.road_stage(france.nimes(), france.gap(), 246.5)

    # Stage 17
    builder.road_stage(france.gap(), france.serre_chevalier(), 190.0)

    # Stage 18
    builder.mountain_stage(france.briancon())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 162.5)

    # Rest day
    builder.rest_day(mountains.alps.alpe_d_huez())

    # Stage 19
    builder.road_stage(mountains.alps.villard_de_lans(), france.saint_etienne(), 179.5)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.saint_etienne(), 58.0)

    # Stage 21
    builder.mountain_stage(france.saint_etienne())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.C1, 190.0)

    # Stage 22
    builder.road_stage(france.clermont_ferrand(), france.nevers(), 194.0)

    # Stage 23
    builder.road_stage(france.cosne_sur_loire(), france.paris(), 255.0)

    return builder.build()

def tdf1987():

    builder = TourDeFranceBuilder(1987,7,1)

    # Prologue
    builder.out_and_back_prologue(west_germany.west_berlin(), 6.0)

    # Stage 1
    builder.enable_morning_stage()
    builder.criterium(west_germany.west_berlin(), 105.0)

    # Stage 2
    builder.out_and_back_team_time_trial(west_germany.west_berlin(), 40.5)

    # Transfer day
    builder.rest_day()

    # Stage 3
    builder.road_stage(west_germany.karlsruhe(), west_germany.stuttgart(), 219.0)

    # Stage 4
    builder.enable_morning_stage()
    builder.road_stage(west_germany.stuttgart(), west_germany.pforzheim(), 79.0)

    # Stage 5
    builder.road_stage(west_germany.pforzheim(), france.strasbourg(), 112.5)

    # Stage 6
    builder.road_stage(france.strasbourg(), france.epinal(), 169.0)

    # Stage 7
    builder.road_stage(france.epinal(), france.troyes(), 211.0)

    # Stage 8
    builder.road_stage(france.troyes(), france.epnay_sous_senart(), 205.5)

    # Stage 9
    builder.road_stage(france.orleans(), france.renaze(), 260.0)

    # Stage 10
    builder.individual_time_trial(france.saumur(), france.futuroscope(), 87.5)

    # Stage 11
    builder.road_stage(france.poitiers(), france.chaumeil(), 255.0)

    # Stage 12
    builder.road_stage(france.brive(), france.bordeaux(), 228.0)

    # Stage 13
    builder.road_stage(france.bayonne(), france.pau(), 219.0)

    # Stage 14
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 166.0)

    # Stage 15
    builder.road_stage(france.tarbes(), france.blagnac(), 164.0)

    # Stage 16
    builder.road_stage(france.blagnac(), france.millau(), 216.5)

    # Stage 17
    builder.road_stage(france.millau(), france.avignon(), 239.0)

    # Rest day
    builder.rest_day(france.avignon())

    # Stage 18
    builder.mountain_time_trial(france.carpentras())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 36.5)

    # Stage 19
    builder.mountain_stage(france.valreas())
    builder.summit_finish(mountains.alps.villard_de_lans(), ColCategory.C1, 185.0)

    # Stage 20
    builder.mountain_stage(mountains.alps.villard_de_lans())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 201.0)

    # Stage 21
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.la_plagne(), ColCategory.HC, 185.5)

    # Stage 22
    builder.road_stage(mountains.alps.la_plagne(), france.morzine(), 186.0)

    # Stage 23
    builder.road_stage(france.saint_julien_en_genevois(), france.dijon(), 224.5)

    # Stage 24
    builder.out_and_back_individual_time_trial(france.dijon(), 38.0)

    # Stage 25
    builder.road_stage(france.creteil(), france.paris(), 192.0)

    return builder.build()

def tdf1988():

    builder = TourDeFranceBuilder(1988,7,3)

    # Prologue
    builder.prologue(france.pornichet(), france.la_baule(), 1.0)

    # Stage 1
    builder.enable_morning_stage()
    builder.road_stage(france.pontchateau(), france.machecoul(), 91.5)

    # Stage 2
    builder.team_time_trial(france.la_haie_fouassiere(), france.ancenis(), 48.0)

    # Stage 3
    builder.road_stage(france.nantes(), france.le_mans(), 213.5)

    # Stage 4
    builder.road_stage(france.le_mans(), france.evreux(), 158.0)

    # Stage 5
    builder.road_stage(france.neufchatel_en_bray(), france.lievin(), 147.5)

    # Stage 6
    builder.individual_time_trial(france.lievin(), france.wasquehal(), 52.0)

    # Stage 7
    builder.road_stage(france.wasquehal(), france.reims(), 225.5)

    # Stage 8
    builder.road_stage(france.reims(), france.nancy(), 219.0)

    # Stage 9
    builder.road_stage(france.nancy(), france.strasbourg(), 160.5)

    # Stage 10
    builder.road_stage(france.belfort(), france.besancon(), 149.5)

    # Stage 11
    builder.road_stage(france.besancon(), france.morzine(), 232.0)

    # Stage 12
    builder.mountain_stage(france.morzine())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 227.0)

    # Stage 13
    builder.mountain_time_trial(france.grenoble())
    builder.summit_finish(mountains.alps.villard_de_lans(), ColCategory.C1, 38.0)

    # Rest day
    builder.rest_day(france.blagnac())

    # Stage 14
    builder.mountain_stage(france.blagnac())
    builder.summit_finish(mountains.pyrenees.guzet_neige(), ColCategory.C1, 163.0)

    # Stage 15
    builder.mountain_stage(france.saint_girons())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 187.5)

    # Stage 16
    builder.enable_morning_stage()
    builder.road_stage(mountains.pyrenees.luz_ardiden(), france.pau(), 38.0)

    # Stage 17
    builder.road_stage(france.pau(), france.bordeaux(), 210.0)

    # Stage 18
    builder.road_stage(france.ruelle_sur_tourve(), france.limoges(), 93.5)

    # Stage 19
    builder.mountain_stage(france.limoges())
    builder.summit_finish(mountains.massif_central.puy_de_dome(), ColCategory.HC, 188.0)

    # Stage 20
    builder.road_stage(france.clermont_ferrand(), france.chalon_sur_saone(), 233.5)

    # Stage 21
    builder.out_and_back_individual_time_trial(france.santennay(), 48.0)

    # Stage 22
    builder.road_stage(france.nemours(), france.paris(), 172.5)

    return builder.build()

def tdf1989():

    builder = TourDeFranceBuilder(1989,7,1)

    # Prologue
    builder.out_and_back_prologue(luxembourg.luxembourg_city(), 7.8)

    # Stage 1
    builder.enable_morning_stage()
    builder.criterium(luxembourg.luxembourg_city(), 135.5)

    # Stage 2
    builder.out_and_back_team_time_trial(luxembourg.luxembourg_city(), 46.0)

    # Stage 3
    builder.road_stage(luxembourg.luxembourg_city(), belgium.spa(), 241.0)

    # Stage 4
    builder.road_stage(belgium.liege(), france.wasquehal(), 255.0)

    # Rest day
    builder.rest_day(france.dinard())

    # Stage 5
    builder.individual_time_trial(france.dinard(), france.rennes(), 73.0)

    # Stage 6
    builder.road_stage(france.rennes(), france.futuroscope(), 259.0)

    # Stage 7
    builder.road_stage(france.poitiers(), france.bordeaux(), 258.5)

    # Stage 8
    builder.road_stage(france.labastide_d_armagnac(), france.pau(), 157.0)

    # Stage 9
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.cauterets(), ColCategory.HC, 147.0)

    # Stage 10
    builder.mountain_stage(mountains.pyrenees.cauterets())
    builder.summit_finish(mountains.pyrenees.superbagneres(), ColCategory.HC, 136.0)

    # Stage 11
    builder.road_stage(france.luchon(), france.blagnac(), 158.5)

    # Stage 12
    builder.road_stage(france.toulouse(), france.montpellier(), 242.0)

    # Stage 13
    builder.road_stage(france.montpellier(), france.marseille(), 179.0)

    # Stage 14
    builder.road_stage(france.marseille(), france.gap(), 240.0)

    # Stage 15
    builder.mountain_time_trial(france.gap())
    builder.summit_finish(mountains.alps.orcieres_merlette(), ColCategory.C1, 39.0)

    # Rest day
    builder.rest_day(mountains.alps.orcieres_merlette())

    # Stage 16
    builder.road_stage(france.gap(), france.briancon(), 175.0)

    # Stage 17
    builder.mountain_stage(france.briancon())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 165.0)

    # Stage 18
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.villard_de_lans(), ColCategory.C1, 91.5)

    # Stage 19
    builder.road_stage(mountains.alps.villard_de_lans(), france.aix_les_bains(), 125.0)

    # Stage 20
    builder.road_stage(france.aix_les_bains(), france.l_isle_d_abeau(), 130.0)

    # Stage 21
    builder.individual_time_trial(france.versailles(), france.paris(), 24.5)

    return builder.build()

def tdf1990():

    builder = TourDeFranceBuilder(1990,6,30)

    # Prologue
    builder.out_and_back_prologue(france.futuroscope(), 6.3)

    # Stage 1
    builder.enable_morning_stage()
    builder.criterium(france.futuroscope(), 138.5)

    # Stage 2
    builder.out_and_back_team_time_trial(france.futuroscope(), 44.5)

    # Stage 3
    builder.road_stage(france.poitiers(), france.nantes(), 233.0)

    # Stage 4
    builder.road_stage(france.nantes(), france.mont_saint_michel(), 203.0)

    # Stage 5
    builder.road_stage(france.avranches(), france.rouen(), 301.0)

    # Rest day
    builder.rest_day(france.rouen())

    # Stage 6
    builder.road_stage(france.sarrebourg(), france.vittel(), 202.5)

    # Stage 7
    builder.individual_time_trial(france.vittel(), france.epinal(), 61.5)

    # Stage 8
    builder.road_stage(france.epinal(), france.besancon(), 181.5)

    # Stage 9
    builder.road_stage(france.besancon(), switzerland.geneva(), 196.0)

    # Stage 10
    builder.road_stage(switzerland.geneva(), france.saint_gervais(), 118.5)

    # Stage 11
    builder.mountain_stage(france.saint_gervais())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 182.5)

    # Stage 12
    builder.mountain_time_trial(france.fontaine())
    builder.summit_finish(mountains.alps.villard_de_lans(), ColCategory.C1, 33.5)

    # Rest day
    builder.rest_day(mountains.alps.villard_de_lans())

    # Stage 13
    builder.road_stage(mountains.alps.villard_de_lans(), france.saint_etienne(), 149.0)

    # Stage 14
    builder.road_stage(france.le_puy_en_velay(), france.millau(), 205.0)

    # Stage 15
    builder.road_stage(france.millau(), france.revel(), 170.0)

    # Stage 16
    builder.mountain_stage(france.blagnac())

    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 215.0)

    # Stage 17
    builder.road_stage(france.lourdes(), france.pau(), 150.0)

    # Stage 18
    builder.road_stage(france.pau(), france.bordeaux(), 202.0)

    # Stage 19
    builder.road_stage(france.castillon_la_bataille(), france.limoges(), 182.5)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.lac_de_vassiviere(), 45.5)

    # Stage 21
    builder.road_stage(france.bretigny_sur_orge(), france.paris(), 182.5)

    return builder.build()

def tdf1991():

    builder = TourDeFranceBuilder(1991,7,6)

    # Prologue
    builder.out_and_back_prologue(france.lyon(), 5.4)

    # Stage 1
    builder.enable_morning_stage()
    builder.criterium(france.lyon(), 114.5)

    # Stage 2
    builder.team_time_trial(france.bron(), france.chassieu(), 36.5)

    # Stage 3
    builder.road_stage(france.villeurbanne(), france.dijon(), 210.5)

    # Stage 4
    builder.road_stage(france.dijon(), france.reims(), 286.0)

    # Stage 5
    builder.road_stage(france.reims(), france.valenciennes(), 149.5)

    # Stage 6
    builder.road_stage(france.arras(), france.le_havre(), 259.0)

    # Stage 7
    builder.road_stage(france.le_havre(), france.argentan(), 167.0)

    # Stage 8
    builder.individual_time_trial(france.argentan(), france.alencon(), 73.0)

    # Stage 9
    builder.road_stage(france.alencon(), france.rennes(), 161.0)

    # Stage 10
    builder.road_stage(france.rennes(), france.quimper(), 207.5)

    # Stage 11
    builder.road_stage(france.quimper(), france.saint_herblain(), 246.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 12
    builder.road_stage(france.pau(), spain.jaca(), 192.0)

    # Stage 13
    builder.road_stage(spain.jaca(), france.val_louron(), 232.0)

    # Stage 14
    builder.road_stage(france.saint_gaudens(), france.castres(), 172.5)

    # Stage 15
    builder.road_stage(france.albi(), france.ales(), 235.0)

    # Stage 16
    builder.road_stage(france.ales(), france.gap(), 215.0)

    # Stage 17
    builder.mountain_stage(france.gap())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 125.0)

    # Stage 18
    builder.road_stage(france.le_bourg_d_oisans(), france.morzine(), 255.0)

    # Stage 19
    builder.road_stage(france.morzine(), france.aix_les_bains(), 177.0)

    # Stage 20
    builder.road_stage(france.aix_les_bains(), france.macon(), 166.0)

    # Stage 21
    builder.individual_time_trial(france.lugny(), france.macon(), 57.0)

    # Stage 22
    builder.road_stage(france.melun(), france.paris(), 178.0)

    return builder.build()

def tdf1992():

    builder = TourDeFranceBuilder(1992,7,4)

    # Prologue
    builder.out_and_back_prologue(spain.san_sebastian(), 8.0)

    # Stage 1
    builder.criterium(spain.san_sebastian(), 194.5)

    # Stage 2
    builder.road_stage(spain.san_sebastian(), france.pau(), 255.0)

    # Stage 3
    builder.road_stage(france.pau(), france.bordeaux(), 210.0)

    # Stage 4
    builder.out_and_back_team_time_trial(france.libourne(), 63.5)

    # Stage 5
    builder.road_stage(france.nogent_sur_oise(), france.wasquehal(), 196.0)

    # Stage 6
    builder.road_stage(france.roubaix(), belgium.brussels(), 167.0)

    # Stage 7
    builder.road_stage(belgium.brussels(), netherlands.valkenburg(), 196.5)

    # Stage 8
    builder.road_stage(netherlands.valkenburg(), germany.koblenz(), 206.5)

    # Stage 9
    builder.out_and_back_individual_time_trial(luxembourg.luxembourg_city(), 65.0)

    # Stage 10
    builder.road_stage(luxembourg.luxembourg_city(), france.strasbourg(), 217.0)

    # Stage 11
    builder.road_stage(france.strasbourg(), france.mulhouse(), 249.5)

    # Stage 12
    builder.road_stage(france.dole(), france.saint_gervais(), 267.5)

    # Rest day
    builder.rest_day(france.dole())

    # Stage 13
    builder.mountain_stage(france.saint_gervais())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 254.5)

    # Stage 14
    builder.mountain_stage(mountains.alps.sestriere())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 186.5)

    # Stage 15
    builder.road_stage(france.le_bourg_d_oisans(), france.saint_etienne(), 198.0)

    # Stage 16
    builder.mountain_stage(france.saint_etienne())
    builder.summit_finish(mountains.massif_central.la_bourboule(), ColCategory.C1, 212.0)

    # Stage 17
    builder.road_stage(mountains.massif_central.la_bourboule(), france.montlucon(), 189.0)

    # Stage 18
    builder.road_stage(france.montlucon(), france.tours(), 212.0)

    # Stage 19
    builder.individual_time_trial(france.tours(), france.blois(), 64.0)

    # Stage 20
    builder.road_stage(france.blois(), france.nanterre(), 222.0)

    # Stage 21
    builder.road_stage(france.la_defense(), france.paris(), 141.0)

    return builder.build()

def tdf1993():

    builder = TourDeFranceBuilder(1993,7,3)

    # Prologue
    builder.out_and_back_prologue(france.le_puy_du_fou(), 6.8)

    # Stage 1
    builder.road_stage(france.lucon(), france.les_sables_d_olonne(), 215.0)

    # Stage 2
    builder.road_stage(france.les_sables_d_olonne(), france.vannes(), 227.5)

    # Stage 3
    builder.road_stage(france.vannes(), france.dinard(), 189.5)

    # Stage 4
    builder.team_time_trial(france.dinard(), france.avranches(), 81.0)

    # Stage 5
    builder.road_stage(france.avranches(), france.evreux(), 225.5)

    # Stage 6
    builder.road_stage(france.evreux(), france.amiens(), 158.0)

    # Stage 7
    builder.road_stage(france.peronne(), france.chalons_sur_marne(), 199.0)

    # Stage 8
    builder.road_stage(france.chalons_sur_marne(), france.verdun(), 184.5)

    # Stage 9
    builder.out_and_back_individual_time_trial(france.lac_de_madine(), 59.0)

    # Rest day
    builder.rest_day(mountains.alps.villard_de_lans())

    # Stage 10
    builder.road_stage(mountains.alps.villard_de_lans(), france.serre_chevalier(), 203.0)

    # Stage 11
    builder.mountain_stage(france.serre_chevalier())
    builder.summit_finish(mountains.alps.maritime.isola2000(), ColCategory.HC, 179.0)

    # Stage 12
    builder.road_stage(france.isola(), france.marseille(), 286.5)

    # Stage 13
    builder.road_stage(france.marseille(), france.montpellier(), 181.5)

    # Stage 14
    builder.road_stage(france.montpellier(), france.perpignan(), 223.0)

    # Stage 15
    builder.road_stage(france.perpignan(), andorra.pal(), 231.5)

    # Rest day
    builder.rest_day(andorra.pal())

    # Stage 16
    builder.road_stage(andorra.pal(), france.saint_lary_soulan_pla_d_adet(), 230.0)

    # Stage 17
    builder.road_stage(france.tarbes(), france.pau(), 190.0)

    # Stage 18
    builder.road_stage(france.orthez(), france.bordeaux(), 195.5)

    # Stage 19
    builder.individual_time_trial(france.bretigny_sur_orge(), france.montlhery(), 48.0)

    # Stage 20
    builder.road_stage(france.viry_chatillon(), france.paris(), 196.5)

    return builder.build()

def tdf1994():

    builder = TourDeFranceBuilder(1994,7,2)

    # Prologue
    builder.out_and_back_prologue(france.lille(), 7.2)

    # Stage 1
    builder.road_stage(france.lille(), france.armentieres(), 234.0)

    # Stage 2
    builder.road_stage(france.roubaix(), france.boulogne_sur_mer(), 203.5)

    # Stage 3
    builder.team_time_trial(france.calais(), france.eurotunnel(), 66.5)

    # Stage 4
    builder.road_stage(united_kingdom.dover(), united_kingdom.brighton(), 204.5)

    # Stage 5
    builder.criterium(united_kingdom.portsmouth(), 187.0)

    # Stage 6
    builder.road_stage(france.cherbourg(), france.rennes(), 270.5)

    # Stage 7
    builder.road_stage(france.rennes(), france.futuroscope(), 259.5)

    # Stage 8
    builder.road_stage(france.poitiers(), france.trelissac(), 218.5)

    # Stage 9
    builder.individual_time_trial(france.perigueux(), france.bergerac(), 64.0)

    # Stage 10
    builder.road_stage(france.bergerac(), france.cahors(), 160.5)

    # Stage 11
    builder.mountain_stage(france.cahors())

    builder.summit_finish(mountains.pyrenees.hautacam(), ColCategory.HC, 263.5)

    # Rest day
    builder.rest_day(france.lourdes())

    # Stage 12
    builder.mountain_stage(france.lourdes())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 204.5)

    # Stage 13
    builder.road_stage(france.bagneres_de_bigorre(), france.albi(), 223.0)

    # Stage 14
    builder.road_stage(france.castres(), france.montpellier(), 202.0)

    # Stage 15
    builder.road_stage(france.montpellier(), france.carpentras(), 231.0)

    # Stage 16
    builder.mountain_stage(france.valreas())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 224.5)

    # Stage 17
    builder.mountain_stage(france.le_bourg_d_oisans())

    builder.summit_finish(mountains.alps.val_thorens(), ColCategory.HC, 149.0)

    # Stage 18
    builder.road_stage(france.moutiers(), france.cluses(), 174.5)

    # Stage 19
    builder.mountain_time_trial(france.cluses())
    builder.summit_finish(france.avoriaz(), ColCategory.C1, 47.5)

    # Stage 20
    builder.road_stage(france.morzine(), france.lac_saint_point(), 208.5)

    # Stage 21
    builder.road_stage(france.disneyland_paris(), france.paris(), 175.0)

    return builder.build()

def tdf1995():

    builder = TourDeFranceBuilder(1995,7,1)

    # Prologue
    builder.out_and_back_prologue(france.saint_brieuc(), 7.3)

    # Stage 1
    builder.road_stage(france.dinan(), france.lannion(), 233.5)

    # Stage 2
    builder.road_stage(france.perros_guirec(), france.vitre(), 235.5)

    # Stage 3
    builder.team_time_trial(france.mayenne(), france.alencon(), 67.0)

    # Stage 4
    builder.road_stage(france.alencon(), france.le_havre(), 162.0)

    # Stage 5
    builder.road_stage(france.fecamp(), france.dunkerque(), 261.0)

    # Stage 6
    builder.road_stage(france.dunkerque(), belgium.charleroi(), 202.0)

    # Stage 7
    builder.road_stage(belgium.charleroi(), belgium.liege(), 203.0)

    # Stage 8
    builder.individual_time_trial(belgium.huy(), belgium.seraing(), 54.0)

    # Rest day
    builder.rest_day(france.le_grand_bornand())

    # Stage 9
    builder.mountain_stage(france.le_grand_bornand())
    builder.summit_finish(mountains.alps.la_plagne(), ColCategory.HC, 160.0)

    # Stage 10
    builder.mountain_stage(mountains.alps.la_plagne())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 162.5)

    # Stage 11
    builder.road_stage(france.le_bourg_d_oisans(), france.saint_etienne(), 199.0)

    # Stage 12
    builder.road_stage(france.saint_etienne(), france.mende(), 222.5)

    # Stage 13
    builder.road_stage(france.mende(), france.revel(), 245.0)

    # Stage 14
    builder.mountain_stage(france.saint_orens_de_gameville())

    builder.summit_finish(mountains.pyrenees.guzet_neige(), ColCategory.C1, 164.0)

    # Rest day
    builder.rest_day(france.saint_girons())

    # Stage 15
    builder.mountain_stage(france.saint_girons())

    builder.summit_finish(mountains.pyrenees.cauterets(), ColCategory.HC, 206.0)

    # Stage 16
    builder.road_stage(france.tarbes(), france.pau(), 149.0)

    # Stage 17
    builder.road_stage(france.pau(), france.bordeaux(), 246.0)

    # Stage 18
    builder.road_stage(france.montpon_menesterol(), france.limoges(), 246.0)

    # Stage 19
    builder.out_and_back_individual_time_trial(france.lac_de_vassiviere(), 46.5)

    # Stage 20
    builder.road_stage(france.sainte_genevieve_des_bois(), france.paris(), 155.0)

    return builder.build()

def tdf1996():

    builder = TourDeFranceBuilder(1996,6,29)

    # Prologue
    builder.out_and_back_prologue(netherlands.s_hertogenbosch(), 9.4)

    # Stage 1
    builder.criterium(netherlands.s_hertogenbosch(), 209.0)

    # Stage 2
    builder.road_stage(netherlands.s_hertogenbosch(), france.wasquehal(), 247.5)

    # Stage 3
    builder.road_stage(france.wasquehal(), france.nogent_sur_oise(), 195.0)

    # Stage 4
    builder.road_stage(france.soissons(), france.lac_de_madine(), 232.0)

    # Stage 5
    builder.road_stage(france.lac_de_madine(), france.besancon(), 242.0)

    # Stage 6
    builder.road_stage(france.arc_et_senans(), france.aix_les_bains(), 207.0)

    # Stage 7
    builder.mountain_stage(france.chambery())
    builder.summit_finish(mountains.alps.les_arcs(), ColCategory.C1, 200.0)

    # Stage 8
    builder.mountain_time_trial(france.bourg_saint_maurice())
    builder.summit_finish(mountains.alps.val_d_isere(), ColCategory.C1, 30.5)

    # Stage 9
    builder.mountain_stage(france.le_monetier_les_bains())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 46.0)

    # Stage 10
    builder.road_stage(italy.turin(), france.gap(), 208.5)

    # Rest day
    builder.rest_day(france.gap())

    # Stage 11
    builder.road_stage(france.gap(), france.valence(), 202.0)

    # Stage 12
    builder.road_stage(france.valence(), france.le_puy_en_velay(), 143.5)

    # Stage 13
    builder.mountain_stage(france.le_puy_en_velay())

    builder.summit_finish(mountains.massif_central.super_besse(), ColCategory.C3, 177.0)

    # Stage 14
    builder.road_stage(france.besse(), france.tulle(), 186.5)

    # Stage 15
    builder.road_stage(france.brive_la_gaillarde(), france.villeneuve_sur_lot(), 176.0)

    # Stage 16
    builder.mountain_stage(france.agen())
    builder.summit_finish(mountains.pyrenees.hautacam(), ColCategory.HC, 199.0)

    # Stage 17
    builder.road_stage(france.argeles_gazost(), spain.pamplona(), 262.0)

    # Stage 18
    builder.road_stage(spain.pamplona(), france.hendaye(), 154.5)

    # Stage 19
    builder.road_stage(france.hendaye(), france.bordeaux(), 226.5)

    # Stage 20
    builder.individual_time_trial(france.bordeaux(), france.saint_emilion(), 63.5)

    # Stage 21
    builder.road_stage(france.palaiseau(), france.paris(), 147.5)

    return builder.build()

def tdf1997():

    builder = TourDeFranceBuilder(1997,7,5)

    # Prologue
    builder.out_and_back_prologue(france.rouen(), 7.3)

    # Stage 1
    builder.road_stage(france.rouen(), france.forges_les_eaux(), 192.0)

    # Stage 2
    builder.road_stage(france.saint_valery_en_caux(), france.vire(), 262.0)

    # Stage 3
    builder.road_stage(france.vire(), france.plumelec(), 224.0)

    # Stage 4
    builder.road_stage(france.plumelec(), france.le_puy_du_fou(), 223.0)

    # Stage 5
    builder.road_stage(france.chantonnay(), france.la_chatre(), 261.5)

    # Stage 6
    builder.road_stage(france.le_blanc(), france.marennes(), 217.5)

    # Stage 7
    builder.road_stage(france.marennes(), france.bordeaux(), 194.0)

    # Stage 8
    builder.road_stage(france.sauternes(), france.pau(), 161.5)

    # Stage 9
    builder.road_stage(france.pau(), france.loudenvielle(), 182.0)

    # Stage 10
    builder.mountain_stage(france.luchon())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 182.0)

    # Stage 11
    builder.road_stage(mountains.pyrenees.arcalis(), france.perpignan(), 192.0)

    # Rest day
    builder.rest_day(france.saint_etienne())

    # Stage 12
    builder.out_and_back_individual_time_trial(france.saint_etienne(), 55.0)

    # Stage 13
    builder.mountain_stage(france.saint_etienne())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 203.5)

    # Stage 14
    builder.mountain_stage(france.le_bourg_d_oisans())

    builder.summit_finish(mountains.alps.courchevel(), ColCategory.C1, 148.0)

    # Stage 15
    builder.road_stage(mountains.alps.courchevel(), france.morzine(), 208.5)

    # Stage 16
    builder.road_stage(france.morzine(), switzerland.fribourg(), 181.0)

    # Stage 17
    builder.road_stage(switzerland.fribourg(), france.colmar(), 218.5)

    # Stage 18
    builder.road_stage(france.colmar(), france.montbeliard(), 175.5)

    # Stage 19
    builder.road_stage(france.montbeliard(), france.dijon(), 172.0)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.disneyland_paris(), 63.0)

    # Stage 21
    builder.road_stage(france.disneyland_paris(), france.paris(), 149.5)

    return builder.build()

def tdf1998():

    builder = TourDeFranceBuilder(1998,7,11)

    # Prologue
    builder.out_and_back_prologue(ireland.dublin(), 5.6)

    # Stage 1
    builder.criterium(ireland.dublin(), 180.5)

    # Stage 2
    builder.road_stage(ireland.enniscorthy(), ireland.cork(), 205.5)

    # Stage 3
    builder.road_stage(france.roscoff(), france.lorient(), 169.0)

    # Stage 4
    builder.road_stage(france.plouay(), france.cholet(), 252.0)

    # Stage 5
    builder.road_stage(france.cholet(), france.chateauroux(), 228.5)

    # Stage 6
    builder.road_stage(france.la_chatre(), france.brive_la_gaillarde(), 204.5)

    # Stage 7
    builder.individual_time_trial(france.meyrignac_l_eglise(), france.correze(), 58.0)

    # Stage 8
    builder.road_stage(france.brive_la_gaillarde(), france.montauban(), 190.5)

    # Stage 9
    builder.road_stage(france.montauban(), france.pau(), 210.0)

    # Stage 10
    builder.road_stage(france.pau(), france.luchon(), 196.5)

    # Stage 11
    builder.mountain_stage(france.luchon())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 170.0)

    # Rest day
    builder.rest_day(france.ariege())

    # Stage 12
    builder.road_stage(france.tarascon_sur_ariege(), france.cap_d_agde(), 222.0)

    # Stage 13
    builder.road_stage(france.frontignan_la_peyrade(), france.carpentras(), 196.0)

    # Stage 14
    builder.road_stage(france.valreas(), france.grenoble(), 186.5)

    # Stage 15
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.les_deux_alpes(), ColCategory.C1, 189.0)

    # Stage 16
    builder.road_stage(france.vizelle(), france.albertville(), 204.0)

    # Stage 17
    builder.road_stage(france.albertville(), france.aix_les_bains(), 149.0)

    # Stage 18
    builder.road_stage(france.aix_les_bains(), switzerland.neuchatel(), 218.5)

    # Stage 19
    builder.road_stage(switzerland.la_chaux_de_fonds(), france.autun(), 242.0)

    # Stage 20
    builder.individual_time_trial(france.montceau_les_mines(), france.le_creusot(), 52.0)

    # Stage 21
    builder.road_stage(france.melun(), france.paris(), 147.5)

    return builder.build()

def tdf1999():

    builder = TourDeFranceBuilder(1999,7,3)

    # Prologue
    builder.out_and_back_prologue(france.le_puy_du_fou(), 6.8)

    # Stage 1
    builder.road_stage(france.montaigu(), france.challans(), 208.0)

    # Stage 2
    builder.road_stage(france.challans(), france.saint_nazaire(), 176.0)

    # Stage 3
    builder.road_stage(france.nantes(), france.laval(), 194.5)

    # Stage 4
    builder.road_stage(france.laval(), france.blois(), 194.5)

    # Stage 5
    builder.road_stage(france.bonneval(), france.amiens(), 233.5)

    # Stage 6
    builder.road_stage(france.amiens(), france.mauberge(), 171.5)

    # Stage 7
    builder.road_stage(france.avesnes_sur_helpe(), france.thionville(), 227.0)

    # Stage 8
    builder.out_and_back_individual_time_trial(france.metz(), 56.5)

    # Rest day
    builder.rest_day(france.le_grand_bornand())

    # Stage 9
    builder.mountain_stage(france.le_grand_bornand())
    builder.summit_finish(mountains.alps.sestriere(), ColCategory.C1, 213.5)

    # Stage 10
    builder.mountain_stage(mountains.alps.sestriere())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 220.5)

    # Stage 11
    builder.road_stage(france.le_bourg_d_oisans(), france.saint_etienne(), 198.5)

    # Stage 12
    builder.road_stage(france.saint_galmier(), france.saint_flour(), 201.5)

    # Stage 13
    builder.road_stage(france.saint_flour(), france.albi(), 236.5)

    # Stage 14
    builder.road_stage(france.castres(), france.saint_gaudens(), 199.0)

    # Rest day
    builder.rest_day(france.saint_gaudens())

    # Stage 15
    builder.mountain_stage(france.saint_gaudens())
    builder.summit_finish(mountains.pyrenees.piau_engaly(), ColCategory.C1, 173.0)

    # Stage 16
    builder.road_stage(france.lannemezan(), france.pau(), 192.0)

    # Stage 17
    builder.road_stage(france.mourenx(), france.bordeaux(), 200.0)

    # Stage 18
    builder.road_stage(france.jonzac(), france.futuroscope(), 187.5)

    # Stage 19
    builder.out_and_back_individual_time_trial(france.futuroscope(), 57.0)

    # Stage 20
    builder.road_stage(france.arpajon(), france.paris(), 143.5)

    return builder.build()

def tdf2000():

    builder = TourDeFranceBuilder(2000,7,1)

    # Stage 1
    builder.out_and_back_individual_time_trial(france.futuroscope(), 16.5)

    # Stage 2
    builder.road_stage(france.futuroscope(), france.loudon(), 194.0)

    # Stage 3
    builder.road_stage(france.loudon(), france.nantes(), 161.5)

    # Stage 4
    builder.team_time_trial(france.nantes(), france.saint_nazaire(), 70.0)

    # Stage 5
    builder.road_stage(france.vannes(), france.vitre(), 202.0)

    # Stage 6
    builder.road_stage(france.vitre(), france.tours(), 198.5)

    # Stage 7
    builder.road_stage(france.tours(), france.limoges(), 205.5)

    # Stage 8
    builder.road_stage(france.limoges(), france.villeneuve_sur_lot(), 203.5)

    # Stage 9
    builder.road_stage(france.agen(), france.dax(), 181.0)

    # Stage 10
    builder.mountain_stage(france.dax())
    builder.summit_finish(mountains.pyrenees.hautacam(), ColCategory.HC, 205.0)

    # Stage 11
    builder.road_stage(france.bagneres_de_bigorre(), france.revel(), 218.5)

    # Rest day
    builder.rest_day(france.provence())

    # Stage 12
    builder.mountain_stage(france.carpentras())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 149.0)

    # Stage 13
    builder.road_stage(france.avignon(), france.draguignan(), 185.5)

    # Stage 14
    builder.road_stage(france.draguignan(), france.briancon(), 249.5)

    # Stage 15
    builder.mountain_stage(france.briancon())
    builder.summit_finish(mountains.alps.courchevel(), ColCategory.C1, 173.5)

    # Rest day
    builder.rest_day(mountains.alps.courchevel())

    # Stage 16
    builder.road_stage(mountains.alps.courchevel(), france.morzine(), 196.5)

    # Stage 17
    builder.road_stage(france.evian_les_bains(), switzerland.lausanne(), 155.0)

    # Stage 18
    builder.road_stage(switzerland.lausanne(), germany.freiburg(), 246.5)

    # Stage 19
    builder.individual_time_trial(germany.freiburg(), france.mulhouse(), 58.5)

    # Stage 20
    builder.road_stage(france.belfort(), france.troyes(), 254.5)

    # Stage 21
    builder.criterium(france.paris(), 138.0)

    return builder.build()

def tdf2001():

    builder = TourDeFranceBuilder(2001,7,7)

    # Prologue
    builder.out_and_back_prologue(france.dunkerque(), 8.2)

    # Stage 1
    builder.road_stage(france.saint_omer(), france.boulogne_sur_mer(), 194.5)

    # Stage 2
    builder.road_stage(france.calais(), belgium.antwerp(), 220.5)

    # Stage 3
    builder.road_stage(belgium.antwerp(), belgium.seraing(), 198.5)

    # Stage 4
    builder.road_stage(belgium.huy(), france.verdun(), 215.0)

    # Stage 5
    builder.team_time_trial(france.verdun(), france.bar_le_duc(), 67.0)

    # Stage 6
    builder.road_stage(france.commercy(), france.strasbourg(), 211.5)

    # Stage 7
    builder.road_stage(france.strasbourg(), france.colmar(), 162.5)

    # Stage 8
    builder.road_stage(france.colmar(), france.pontarlier(), 222.5)

    # Stage 9
    builder.road_stage(france.pontarlier(), france.aix_les_bains(), 185.0)

    # Stage 10
    builder.mountain_stage(france.aix_les_bains())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 209.0)

    # Stage 11
    builder.mountain_time_trial(france.grenoble())
    builder.summit_finish(mountains.alps.chamrousse(), ColCategory.C1, 32.0)

    # Rest day
    builder.rest_day(france.perpignan())

    # Stage 12
    builder.mountain_stage(france.perpignan())
    builder.summit_finish(mountains.pyrenees.plateau_de_bonascre(), ColCategory.C1, 165.5)

    # Stage 13
    builder.road_stage(france.foix(), france.saint_lary_soulan_pla_d_adet(), 194.0)

    # Stage 14
    builder.mountain_stage(france.tarbes())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 141.5)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 15
    builder.road_stage(france.pau(), france.lavaur(), 232.5)

    # Stage 16
    builder.road_stage(france.castelsarrasin(), france.sarran(), 229.5)

    # Stage 17
    builder.road_stage(france.brive_la_gaillarde(), france.montlucon(), 194.0)

    # Stage 18
    builder.individual_time_trial(france.montlucon(), france.saint_amand_montrond(), 61.0)

    # Stage 19
    builder.road_stage(france.orleans(), france.evry(), 149.5)

    # Stage 20
    builder.road_stage(france.corbeil_essonnes(), france.paris(), 160.5)

    return builder.build()

def tdf2002():

    builder = TourDeFranceBuilder(2002,7,6)

    # Prologue
    builder.out_and_back_prologue(luxembourg.luxembourg_city(), 7.0)

    # Stage 1
    builder.criterium(luxembourg.luxembourg_city(), 192.5)

    # Stage 2
    builder.road_stage(luxembourg.luxembourg_city(), germany.saarbrucken(), 181.0)

    # Stage 3
    builder.road_stage(france.metz(), france.reims(), 174.5)

    # Stage 4
    builder.team_time_trial(france.epernay(), france.chateau_thierry(), 67.5)

    # Stage 5
    builder.road_stage(france.soissons(), france.rouen(), 195.0)

    # Stage 6
    builder.road_stage(france.forges_les_eaux(), france.alencon(), 199.5)

    # Stage 7
    builder.road_stage(france.bagnoles_de_l_orne(), france.avranches(), 176.0)

    # Stage 8
    builder.road_stage(france.saint_martin_de_landelles(), france.plouay(), 217.5)

    # Stage 9
    builder.individual_time_trial(france.lanester(), france.lorient(), 52.0)

    # Rest day
    builder.rest_day(france.bordeaux())

    # Stage 10
    builder.road_stage(france.bazas(), france.pau(), 147.0)

    # Stage 11
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.la_mongie(), ColCategory.C1, 158.0)

    # Stage 12
    builder.mountain_stage(france.lannemezan())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 199.5)

    # Stage 13
    builder.road_stage(france.lavelanet(), france.beziers(), 171.0)

    # Stage 14
    builder.mountain_stage(france.lodeve())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 221.0)

    # Rest day
    builder.rest_day(france.vaucluse())

    # Stage 15
    builder.mountain_stage(france.vaison_la_romaine())

    builder.summit_finish(mountains.alps.les_deux_alpes(), ColCategory.C1, 226.5)

    # Stage 16
    builder.mountain_stage(mountains.alps.les_deux_alpes())
    builder.summit_finish(mountains.alps.la_plagne(), ColCategory.HC, 179.5)

    # Stage 17
    builder.road_stage(france.aime(), france.cluses(), 142.0)

    # Stage 18
    builder.road_stage(france.cluses(), france.bourg_en_bresse(), 176.5)

    # Stage 19
    builder.individual_time_trial(france.regnie_durette(), france.macon(), 50.0)

    # Stage 20
    builder.road_stage(france.melun(), france.paris(), 144.0)

    return builder.build()

def tdf2003():

    builder = TourDeFranceBuilder(2003,7,5)

    # Prologue
    builder.out_and_back_prologue(france.paris(), 6.5)

    # Stage 1
    builder.road_stage(france.saint_denis(), france.meaux(), 168.0)

    # Stage 2
    builder.road_stage(france.la_ferte_sous_jouarre(), france.sedan(), 204.5)

    # Stage 3
    builder.road_stage(france.charleville_mezieres(), france.saint_dizier(), 167.5)

    # Stage 4
    builder.team_time_trial(france.joinville(), france.saint_dizier(), 69.0)

    # Stage 5
    builder.road_stage(france.troyes(), france.nevers(), 196.5)

    # Stage 6
    builder.road_stage(france.nevers(), france.lyon(), 230.0)

    # Stage 7
    builder.road_stage(france.lyon(), france.morzine(), 230.5)

    # Stage 8
    builder.mountain_stage(france.sallanches())

    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 219.0)

    # Stage 9
    builder.road_stage(france.le_bourg_d_oisans(), france.gap(), 184.5)

    # Stage 10
    builder.road_stage(france.gap(), france.marseille(), 219.5)

    # Rest day
    builder.rest_day(france.narbonne())

    # Stage 11
    builder.road_stage(france.narbonne(), france.toulouse(), 153.5)

    # Stage 12
    builder.individual_time_trial(france.gaillac(), france.cap_decouverte(), 47.0)

    # Stage 13
    builder.mountain_stage(france.toulouse())

    builder.summit_finish(mountains.pyrenees.ax_3_domaines(), ColCategory.C1, 197.5)

    # Stage 14
    builder.road_stage(france.saint_girons(), france.loudenvielle(), 191.5)

    # Stage 15
    builder.mountain_stage(france.bagneres_de_bigorre())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 159.5)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 16
    builder.road_stage(france.pau(), france.bayonne(), 197.5)

    # Stage 17
    builder.road_stage(france.dax(), france.bordeaux(), 181.0)

    # Stage 18
    builder.road_stage(france.bordeaux(), france.saint_maixent_l_ecole(), 203.5)

    # Stage 19
    builder.individual_time_trial(france.pornic(), france.nantes(), 49.0)

    # Stage 20
    builder.road_stage(france.ville_d_avray(), france.paris(), 152.0)

    return builder.build()

def tdf2004():

    builder = TourDeFranceBuilder(2004,7,3)

    # Prologue
    builder.out_and_back_prologue(belgium.liege(), 6.1)

    # Stage 1
    builder.road_stage(belgium.liege(), belgium.charleroi(), 202.5)

    # Stage 2
    builder.road_stage(belgium.charleroi(), belgium.namur(), 197.0)

    # Stage 3
    builder.road_stage(belgium.waterloo(), france.wasquehal(), 210.0)

    # Stage 4
    builder.team_time_trial(france.cambrai(), france.arras(), 64.5)

    # Stage 5
    builder.road_stage(france.amiens(), france.chartres(), 200.5)

    # Stage 6
    builder.road_stage(france.bonneval(), france.angers(), 196.0)

    # Stage 7
    builder.road_stage(france.chateaubriant(), france.saint_brieuc(), 204.5)

    # Stage 8
    builder.road_stage(france.lamballe(), france.quimper(), 168.0)

    # Rest day
    builder.rest_day(france.limoges())

    # Stage 9
    builder.road_stage(france.saint_leonard_de_noblat(), france.gueret(), 160.5)

    # Stage 10
    builder.road_stage(france.limoges(), france.saint_flour(), 237.0)

    # Stage 11
    builder.road_stage(france.saint_flour(), france.figeac(), 164.0)

    # Stage 12
    builder.mountain_stage(france.castelsarrasin())
    builder.summit_finish(mountains.pyrenees.la_mongie(), ColCategory.C1, 197.5)

    # Stage 13
    builder.mountain_stage(france.lannemezan())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 205.5)

    # Stage 14
    builder.road_stage(france.carcassonne(), france.nimes(), 192.5)

    # Rest day
    builder.rest_day(france.nimes())

    # Stage 15
    builder.mountain_stage(france.valreas())
    builder.summit_finish(mountains.alps.villard_de_lans(), ColCategory.C1, 180.5)

    # Stage 16
    builder.mountain_time_trial(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 15.5)

    # Stage 17
    builder.road_stage(france.le_bourg_d_oisans(), france.le_grand_bornand(), 204.5)

    # Stage 18
    builder.road_stage(france.annemasse(), france.lons_le_saunier(), 166.5)

    # Stage 19
    builder.out_and_back_individual_time_trial(france.besancon(), 55.0)

    # Stage 20
    builder.road_stage(france.montereau_fault_yonne(), france.paris(), 163.0)

    return builder.build()

def tdf2005():

    builder = TourDeFranceBuilder(2005,7,2)

    # Stage 1
    builder.individual_time_trial(france.fromentine(), france.noirmoutier_en_l_ile(), 19.0)

    # Stage 2
    builder.road_stage(france.challans(), france.les_essarts(), 181.5)

    # Stage 3
    builder.road_stage(france.la_chataigneraie(), france.tours(), 212.5)

    # Stage 4
    builder.team_time_trial(france.tours(), france.blois(), 67.5)

    # Stage 5
    builder.road_stage(france.chambord(), france.montargis(), 183.0)

    # Stage 6
    builder.road_stage(france.troyes(), france.nancy(), 199.0)

    # Stage 7
    builder.road_stage(france.luneville(), germany.karlsruhe(), 228.5)

    # Stage 8
    builder.road_stage(germany.pforzheim(), france.gerardmer(), 231.5)

    # Stage 9
    builder.road_stage(france.gerardmer(), france.mulhouse(), 171.0)

    # Stage 10
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.courchevel(), ColCategory.C1, 177.0)

    # Rest day
    builder.rest_day(france.grenoble())

    # Stage 11
    builder.road_stage(mountains.alps.courchevel(), france.briancon(), 173.0)

    # Stage 12
    builder.road_stage(france.briancon(), france.digne_les_bains(), 187.0)

    # Stage 13
    builder.road_stage(france.miramas(), france.montpellier(), 173.5)

    # Stage 14
    builder.mountain_stage(france.agde())
    builder.summit_finish(mountains.pyrenees.ax_3_domaines(), ColCategory.C1, 220.5)

    # Stage 15
    builder.road_stage(france.lezat_sur_leze(), france.saint_lary_soulan_pla_d_adet(), 205.5)

    # Stage 16
    builder.road_stage(france.mourenx(), france.pau(), 180.5)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 17
    builder.road_stage(france.pau(), france.revel(), 239.5)

    # Stage 18
    builder.road_stage(france.albi(), france.mende(), 189.0)

    # Stage 19
    builder.road_stage(france.issoire(), france.le_puy_en_velay(), 153.5)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.saint_etienne(), 55.5)

    # Stage 21
    builder.road_stage(france.corbeil_essonnes(), france.paris(), 144.5)

    return builder.build()

def tdf2006():

    builder = TourDeFranceBuilder(2006,7,1)

    # Prologue
    builder.out_and_back_prologue(france.strasbourg(), 7.1)

    # Stage 1
    builder.criterium(france.strasbourg(), 184.5)

    # Stage 2
    builder.road_stage(france.obernai(), luxembourg.esch_sur_alzette(), 228.5)

    # Stage 3
    builder.road_stage(luxembourg.esch_sur_alzette(), netherlands.valkenburg(), 216.5)

    # Stage 4
    builder.road_stage(belgium.huy(), france.saint_quentin(), 207.0)

    # Stage 5
    builder.road_stage(france.beauvais(), france.caen(), 225.0)

    # Stage 6
    builder.road_stage(france.lisieux(), france.vitre(), 189.0)

    # Stage 7
    builder.individual_time_trial(france.saint_gregoire(), france.rennes(), 52.0)

    # Stage 8
    builder.road_stage(france.saint_meen_le_grand(), france.lorient(), 181.0)

    # Rest day
    builder.rest_day(france.bordeaux())

    # Stage 9
    builder.road_stage(france.bordeaux(), france.dax(), 169.5)

    # Stage 10
    builder.road_stage(france.cambo_les_bains(), france.pau(), 190.5)

    # Stage 11
    builder.mountain_stage(france.tarbes())
    builder.summit_finish(mountains.pyrenees.val_d_aran_pla_de_beret(), ColCategory.C1, 206.5)

    # Stage 12
    builder.road_stage(france.luchon(), france.carcassonne(), 211.5)

    # Stage 13
    builder.road_stage(france.beziers(), france.montelimar(), 230.0)

    # Stage 14
    builder.road_stage(france.montelimar(), france.gap(), 180.5)

    # Rest day
    builder.rest_day(france.gap())

    # Stage 15
    builder.mountain_stage(france.gap())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 187.0)

    # Stage 16
    builder.mountain_stage(france.le_bourg_d_oisans())
    builder.summit_finish(mountains.alps.la_toussuire(), ColCategory.C1, 182.0)

    # Stage 17
    builder.road_stage(france.saint_jean_de_maurienne(), france.morzine(), 200.5)

    # Stage 18
    builder.road_stage(france.morzine(), france.macon(), 197.0)

    # Stage 19
    builder.individual_time_trial(france.le_creusot(), france.montceau_les_mines(), 57.0)

    # Stage 20
    builder.road_stage(france.antony_parc_de_sceaux(), france.paris(), 154.5)

    return builder.build()

def tdf2007():

    builder = TourDeFranceBuilder(2007,7,7)

    # Prologue
    builder.out_and_back_prologue(united_kingdom.london(), 7.9)

    # Stage 1
    builder.road_stage(united_kingdom.london(), united_kingdom.canterbury(), 203.0)

    # Stage 2
    builder.road_stage(france.dunkerque(), belgium.ghent(), 168.5)

    # Stage 3
    builder.road_stage(belgium.waregem(), france.compiegne(), 236.5)

    # Stage 4
    builder.road_stage(france.villers_cotterets(), france.joigny(), 193.0)

    # Stage 5
    builder.road_stage(france.chablis(), france.autun(), 182.5)

    # Stage 6
    builder.road_stage(france.semur_en_auxois(), france.bourg_en_bresse(), 199.5)

    # Stage 7
    builder.road_stage(france.bourg_en_bresse(), france.le_grand_bornand(), 197.5)

    # Stage 8
    builder.road_stage(france.le_grand_bornand(), france.tignes(), 165.0)

    # Rest day
    builder.rest_day(france.tignes())

    # Stage 9
    builder.road_stage(mountains.alps.val_d_isere(), france.briancon(), 159.5)

    # Stage 10
    builder.road_stage(france.tallard(), france.marseille(), 229.5)

    # Stage 11
    builder.road_stage(france.marseille(), france.montpellier(), 182.5)

    # Stage 12
    builder.road_stage(france.montpellier(), france.castres(), 178.5)

    # Stage 13
    builder.out_and_back_individual_time_trial(france.albi(), 54.0)

    # Stage 14
    builder.mountain_stage(france.mazamet())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 197.0)

    # Stage 15
    builder.road_stage(france.foix(), france.loudenvielle(), 196.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 16
    builder.road_stage(france.orthez(), france.gourette_col_d_aubisque(), 218.5)

    # Stage 17
    builder.road_stage(france.pau(), france.castelsarrasin(), 188.5)

    # Stage 18
    builder.road_stage(france.cahors(), france.angouleme(), 211.0)

    # Stage 19
    builder.individual_time_trial(france.cognac(), france.angouleme(), 55.5)

    # Stage 20
    builder.road_stage(france.marcoussis(), france.paris(), 146.0)

    return builder.build()

def tdf2008():

    builder = TourDeFranceBuilder(2008,7,5)

    # Stage 1
    builder.road_stage(france.brest(), france.plumelec(), 197.5)

    # Stage 2
    builder.road_stage(france.aulay(), france.saint_brieuc(), 164.5)

    # Stage 3
    builder.road_stage(france.saint_malo(), france.nantes(), 208.0)

    # Stage 4
    builder.out_and_back_individual_time_trial(france.cholet(), 29.5)

    # Stage 5
    builder.road_stage(france.cholet(), france.chateauroux(), 232.0)

    # Stage 6
    builder.mountain_stage(france.aigurande())
    builder.summit_finish(mountains.massif_central.super_besse(), ColCategory.C2, 195.0)

    # Stage 7
    builder.road_stage(france.brioude(), france.aurillac(), 159.0)

    # Stage 8
    builder.road_stage(france.figeac(), france.toulouse(), 172.5)

    # Stage 9
    builder.road_stage(france.toulouse(), france.bagneres_de_bigorre(), 224.0)

    # Stage 10
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.hautacam(), ColCategory.HC, 156.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 11
    builder.road_stage(france.lannemezan(), france.foix(), 167.5)

    # Stage 12
    builder.road_stage(france.lavalanet(), france.narbonne(), 168.5)

    # Stage 13
    builder.road_stage(france.narbonne(), france.nimes(), 182.0)

    # Stage 14
    builder.road_stage(france.nimes(), france.digne_les_bains(), 194.5)

    # Stage 15
    builder.road_stage(france.embrun(), italy.prato_nevoso(), 183.0)

    # Rest day
    builder.rest_day(italy.cuneo())

    # Stage 16
    builder.road_stage(italy.cuneo(), france.jausiers(), 157.0)

    # Stage 17
    builder.mountain_stage(france.embrun())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 210.5)

    # Stage 18
    builder.road_stage(france.le_bourg_d_oisans(), france.saint_etienne(), 196.5)

    # Stage 19
    builder.road_stage(france.roanne(), france.montlucon(), 165.5)

    # Stage 20
    builder.individual_time_trial(france.cerilly(), france.saint_amand_montrond(), 53.0)

    # Stage 21
    builder.road_stage(france.etampes(), france.paris(), 143.0)

    return builder.build()

def tdf2009():

    builder = TourDeFranceBuilder(2009,7,4)

    # Stage 1
    builder.out_and_back_individual_time_trial(monaco.monaco(), 15.5)

    # Stage 2
    builder.road_stage(monaco.monaco(), france.brignoles(), 187.0)

    # Stage 3
    builder.road_stage(france.marseille(), france.la_grande_motte(), 196.5)

    # Stage 4
    builder.out_and_back_team_time_trial(france.montpellier(), 39.0)

    # Stage 5
    builder.road_stage(france.cap_d_agde(), france.perpignan(), 196.5)

    # Stage 6
    builder.road_stage(spain.girona(), spain.barcelona(), 181.5)

    # Stage 7
    builder.mountain_stage(spain.barcelona())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 224.0)

    # Stage 8
    builder.road_stage(andorra.andorra_la_vella(), france.saint_girons(), 176.5)

    # Stage 9
    builder.road_stage(france.saint_girons(), france.tarbes(), 160.5)

    # Rest day
    builder.rest_day(france.limoges())

    # Stage 10
    builder.road_stage(france.limoges(), france.issoudun(), 194.5)

    # Stage 11
    builder.road_stage(france.vatan(), france.saint_fargeau(), 192.0)

    # Stage 12
    builder.road_stage(france.tonnerre(), france.vittel(), 211.5)

    # Stage 13
    builder.road_stage(france.vittel(), france.colmar(), 200.0)

    # Stage 14
    builder.road_stage(france.colmar(), france.besancon(), 199.0)

    # Stage 15
    builder.mountain_stage(france.pontarlier())
    builder.summit_finish(mountains.alps.verbier(), ColCategory.C1, 207.5)

    # Rest day
    builder.rest_day(mountains.alps.verbier())

    # Stage 16
    builder.road_stage(switzerland.martigny(), france.bourg_saint_maurice(), 159.0)

    # Stage 17
    builder.road_stage(france.bourg_saint_maurice(), france.le_grand_bornand(), 169.5)

    # Stage 18
    builder.out_and_back_individual_time_trial(france.annecy(), 40.5)

    # Stage 19
    builder.road_stage(france.bourgoin_jallieu(), france.aubenas(), 178.0)

    # Stage 20
    builder.mountain_stage(france.montelimar())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 167.0)

    # Stage 21
    builder.road_stage(france.montereau_fault_yonne(), france.paris(), 164.0)

    return builder.build()

def tdf2010():

    builder = TourDeFranceBuilder(2010,7,3)

    # Prologue
    builder.out_and_back_prologue(netherlands.rotterdam(), 8.9)

    # Stage 1
    builder.road_stage(netherlands.rotterdam(), belgium.brussels(), 223.5)

    # Stage 2
    builder.road_stage(belgium.brussels(), belgium.spa(), 201.0)

    # Stage 3
    builder.road_stage(belgium.wanze(), france.arenberg_porte_du_hainaut(), 213.0)

    # Stage 4
    builder.road_stage(france.cambrai(), france.reims(), 153.5)

    # Stage 5
    builder.road_stage(france.epernay(), france.montargis(), 187.5)

    # Stage 6
    builder.road_stage(france.montargis(), france.gueugnon(), 227.5)

    # Stage 7
    builder.road_stage(france.tournus(), france.station_des_rousses(), 165.6)

    # Stage 8
    builder.road_stage(france.station_des_rousses(), france.morzine_avoriaz(), 189.0)

    # Rest day
    builder.rest_day(france.morzine_avoriaz())

    # Stage 9
    builder.road_stage(france.morzine_avoriaz(), france.saint_jean_de_maurienne(), 204.5)

    # Stage 10
    builder.road_stage(france.chambery(), france.gap(), 179.0)

    # Stage 11
    builder.road_stage(france.sisteron(), france.bourg_les_valence(), 184.5)

    # Stage 12
    builder.road_stage(france.bourg_de_peage(), france.mende(), 210.5)

    # Stage 13
    builder.road_stage(france.rodez(), france.revel(), 196.0)

    # Stage 14
    builder.mountain_stage(france.revel())
    builder.summit_finish(mountains.pyrenees.ax_3_domaines(), ColCategory.C1, 184.5)

    # Stage 15
    builder.road_stage(france.pamiers(), france.bagneres_de_luchon(), 187.5)

    # Stage 16
    builder.road_stage(france.bagneres_de_luchon(), france.pau(), 199.5)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 17
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.col_du_tourmalet(), ColCategory.HC, 174.0)

    # Stage 18
    builder.road_stage(france.salies_de_bearn(), france.bordeaux(), 198.0)

    # Stage 19
    builder.individual_time_trial(france.bordeaux(), france.pauillac(), 52.0)

    # Stage 20
    builder.road_stage(france.longjumeau(), france.paris(), 102.5)

    return builder.build()

def tdf2011():

    builder = TourDeFranceBuilder(2011,7,2)

    # Stage 1
    builder.road_stage(france.passage_du_gois(), france.mont_des_alouettes(), 191.5)

    # Stage 2
    builder.out_and_back_team_time_trial(france.les_essarts(), 23.0)

    # Stage 3
    builder.road_stage(france.olonne_sur_mer(), france.redon(), 198.0)

    # Stage 4
    builder.mountain_stage(france.lorient())
    builder.summit_finish(mountains.massif_amorican.mur_de_bretagne(), ColCategory.C3, 172.5)

    # Stage 5
    builder.road_stage(france.carhaix(), france.cap_frehel(), 164.5)

    # Stage 6
    builder.road_stage(france.dinan(), france.lisieux(), 226.5)

    # Stage 7
    builder.road_stage(france.le_mans(), france.chateauroux(), 218.0)

    # Stage 8
    builder.mountain_stage(france.aigurande())
    builder.summit_finish(mountains.massif_central.super_besse(), ColCategory.C3, 189.0)

    # Stage 9
    builder.road_stage(france.issoire(), france.saint_flour(), 208.0)

    # Rest day
    builder.rest_day(mountains.massif_central.le_lioran())

    # Stage 10
    builder.road_stage(france.aurillac(), france.carmaux(), 158.0)

    # Stage 11
    builder.road_stage(france.blaye_les_mines(), france.lavaur(), 167.5)

    # Stage 12
    builder.mountain_stage(france.cugnaux())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.HC, 211.0)

    # Stage 13
    builder.road_stage(france.pau(), france.lourdes(), 152.5)

    # Stage 14
    builder.mountain_stage(france.saint_gaudens())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 168.5)

    # Stage 15
    builder.road_stage(france.limoux(), france.montpellier(), 192.5)

    # Rest day
    builder.rest_day(france.drome())

    # Stage 16
    builder.road_stage(france.saint_paul_trois_chateaux(), france.gap(), 162.5)

    # Stage 17
    builder.road_stage(france.gap(), italy.pinerolo(), 179.0)

    # Stage 18
    builder.mountain_stage(italy.pinerolo())
    builder.summit_finish(mountains.alps.col_du_galibier_serre_chevalier(), ColCategory.HC, 200.5)

    # Stage 19
    builder.mountain_stage(france.modane())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 109.5)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.grenoble(), 42.5)

    # Stage 21
    builder.road_stage(france.creteil(), france.paris(), 95.0)

    return builder.build()

def tdf2012():

    builder = TourDeFranceBuilder(2012,6,30)

    # Stage 1
    builder.criterium(belgium.liege(), 6.4)

    # Stage 2
    builder.road_stage(belgium.liege(), belgium.seraing(), 198.0)

    # Stage 3
    builder.road_stage(belgium.vise(), belgium.tournai(), 198.0)

    # Stage 4
    builder.road_stage(france.orchies(), france.boulogne_sur_mer(), 197.0)

    # Stage 5
    builder.road_stage(france.abbeville(), france.rouen(), 214.5)

    # Stage 6
    builder.road_stage(france.rouen(), france.saint_quentin(), 196.5)

    # Stage 7
    builder.road_stage(france.epernay(), france.metz(), 207.5)

    # Stage 8
    builder.mountain_stage(france.tomblaine())
    builder.summit_finish(mountains.vosges.la_planche_des_belles_filles(), ColCategory.C1, 199.0)

    # Stage 9
    builder.road_stage(france.belfort(), france.porrentruy(), 157.5)

    # Stage 10
    builder.individual_time_trial(france.arc_et_senans(), france.besancon(), 41.5)

    # Rest day
    builder.rest_day(france.macon())

    # Stage 11
    builder.road_stage(france.macon(), france.bellegarde_sue_valserine(), 194.5)

    # Stage 12
    builder.road_stage(france.albertville(), france.la_toussuire_les_sybelles(), 148.0)

    # Stage 13
    builder.road_stage(france.saint_jean_de_maurienne(), france.annonay_davezieux(), 226.0)

    # Stage 14
    builder.road_stage(france.saint_paul_trois_chateaux(), france.cap_d_agde(), 217.0)

    # Stage 15
    builder.road_stage(france.limoux(), france.foix(), 191.0)

    # Stage 16
    builder.road_stage(france.samatan(), france.pau(), 158.5)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 17
    builder.road_stage(france.pau(), france.bagneres_de_luchon(), 197.0)

    # Stage 18
    builder.mountain_stage(france.bagneres_de_luchon())
    builder.summit_finish(mountains.pyrenees.peyragudes(), ColCategory.C1, 143.5)

    # Stage 19
    builder.road_stage(france.blagnac(), france.brive_la_gaillarde(), 222.5)

    # Stage 20
    builder.individual_time_trial(france.bonneval(), france.chartres(), 53.5)

    # Stage 21
    builder.road_stage(france.rambouillet(), france.paris(), 120.0)

    return builder.build()

def tdf2013():

    builder = TourDeFranceBuilder(2013,6,29)

    # Stage 1
    builder.road_stage(france.porto_vecchio(), france.bastia(), 213.0)

    # Stage 2
    builder.road_stage(france.bastia(), france.ajaccio(), 156.0)

    # Stage 3
    builder.road_stage(france.ajaccio(), france.calvi(), 145.5)

    # Stage 4
    builder.out_and_back_team_time_trial(france.nice(), 25.0)

    # Stage 5
    builder.road_stage(france.cagnes_sur_mer(), france.marseille(), 228.5)

    # Stage 6
    builder.road_stage(france.aix_en_provence(), france.montpellier(), 176.5)

    # Stage 7
    builder.road_stage(france.montpellier(), france.albi(), 205.5)

    # Stage 8
    builder.mountain_stage(france.castres())
    builder.summit_finish(mountains.pyrenees.ax_3_domaines(), ColCategory.C1, 195.0)

    # Stage 9
    builder.road_stage(france.saint_girons(), france.bagneres_de_bigorre(), 168.5)

    # Rest day
    builder.rest_day(france.saint_nazaire())

    # Stage 10
    builder.road_stage(france.saint_gildas_des_bois(), france.saint_malo(), 197.0)

    # Stage 11
    builder.individual_time_trial(france.avranches(), france.mont_saint_michel(), 33.0)

    # Stage 12
    builder.road_stage(france.fougeres(), france.tours(), 218.0)

    # Stage 13
    builder.road_stage(france.tours(), france.saint_amand_montrond(), 173.0)

    # Stage 14
    builder.road_stage(france.saint_pourcain_sur_sioule(), france.lyon(), 191.0)

    # Stage 15
    builder.mountain_stage(france.givors())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 242.5)

    # Rest day
    builder.rest_day(france.vaucluse())

    # Stage 16
    builder.road_stage(france.vaison_la_romaine(), france.gap(), 168.0)

    # Stage 17
    builder.individual_time_trial(france.embrun(), france.chorges(), 32.0)

    # Stage 18
    builder.mountain_stage(france.gap())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 172.5)

    # Stage 19
    builder.road_stage(france.le_bourg_d_oisans(), france.le_grand_bornand(), 204.5)

    # Stage 20
    builder.road_stage(france.annecy(), france.semnoz(), 125.0)

    # Stage 21
    builder.road_stage(france.versailles(), france.paris(), 133.5)

    return builder.build()

def tdf2014():

    builder = TourDeFranceBuilder(2014,7,5)

    # Stage 1
    builder.road_stage(united_kingdom.leeds(), united_kingdom.harrogate(), 190.5)

    # Stage 2
    builder.road_stage(united_kingdom.york(), united_kingdom.sheffield(), 201.0)

    # Stage 3
    builder.road_stage(united_kingdom.cambridge(), united_kingdom.london(), 155.0)

    # Stage 4
    builder.road_stage(france.le_touquet_paris_plage(), france.lille_metropole(), 163.5)

    # Stage 5
    builder.road_stage(belgium.ypres(), france.arenberg_porte_du_hainaut(), 152.5)

    # Stage 6
    builder.road_stage(france.arras(), france.reims(), 194.0)

    # Stage 7
    builder.road_stage(france.epernay(), france.nancy(), 234.5)

    # Stage 8
    builder.road_stage(france.tomblaine(), france.gerardmer_las_mauselaine(), 161.0)

    # Stage 9
    builder.road_stage(france.gerardmer(), france.mulhouse(), 170.0)

    # Stage 10
    builder.mountain_stage(france.mulhouse())
    builder.summit_finish(mountains.vosges.la_planche_des_belles_filles(), ColCategory.C1, 161.5)

    # Rest day
    builder.rest_day(france.besancon())

    # Stage 11
    builder.road_stage(france.besancon(), france.oyonnax(), 187.5)

    # Stage 12
    builder.road_stage(france.bourg_en_bresse(), france.saint_etienne(), 185.5)

    # Stage 13
    builder.mountain_stage(france.saint_etienne())
    builder.summit_finish(mountains.alps.chamrousse(), ColCategory.C1, 197.5)

    # Stage 14
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.risoul(), ColCategory.C1, 177.0)

    # Stage 15
    builder.road_stage(france.tallard(), france.nimes(), 222.0)

    # Rest day
    builder.rest_day(france.carcassonne())

    # Stage 16
    builder.road_stage(france.carcassonne(), france.bagneres_de_luchon(), 237.5)

    # Stage 17
    builder.road_stage(france.saint_gaudens(), france.saint_lary_pla_d_adet(), 124.5)

    # Stage 18
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.hautacam(), ColCategory.HC, 145.5)

    # Stage 19
    builder.road_stage(france.maubourguet_pays_du_val_d_adour(), france.bergerac(), 208.5)

    # Stage 20
    builder.individual_time_trial(france.bergerac(), france.perigueux(), 54.0)

    # Stage 21
    builder.road_stage(france.evry(), france.paris(), 137.5)

    return builder.build()

def tdf2015():

    builder = TourDeFranceBuilder(2015,7,4)

    # Stage 1
    builder.out_and_back_individual_time_trial(netherlands.utrecht(), 13.8)

    # Stage 2
    builder.road_stage(netherlands.utrecht(), netherlands.zeeland(), 166.0)

    # Stage 3
    builder.road_stage(belgium.antwerp(), belgium.huy(), 159.5)

    # Stage 4
    builder.road_stage(belgium.seraing(), france.cambrai(), 223.5)

    # Stage 5
    builder.road_stage(france.arras(), france.amiens(), 189.5)

    # Stage 6
    builder.road_stage(france.abbeville(), france.le_havre(), 191.5)

    # Stage 7
    builder.road_stage(france.livarot(), france.fougeres(), 190.5)

    # Stage 8
    builder.mountain_stage(france.rennes())
    builder.summit_finish(mountains.massif_amorican.mur_de_bretagne(), ColCategory.C3, 181.5)

    # Stage 9
    builder.team_time_trial(france.vannes(), france.plumelec(), 28.0)

    # Rest day
    builder.rest_day(france.pau())

    # Stage 10
    builder.mountain_stage(france.tarbes())
    builder.summit_finish(mountains.pyrenees.la_pierre_saint_martin(), ColCategory.C1, 167.0)

    # Stage 11
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.cauterets(), ColCategory.HC, 188.0)

    # Stage 12
    builder.mountain_stage(france.lannemezan())
    builder.summit_finish(mountains.pyrenees.plateau_de_beille(), ColCategory.C1, 195.0)

    # Stage 13
    builder.road_stage(france.muret(), france.rodez(), 198.5)

    # Stage 14
    builder.road_stage(france.rodez(), france.mende(), 178.5)

    # Stage 15
    builder.road_stage(france.mende(), france.valence(), 183.0)

    # Stage 16
    builder.road_stage(france.bourg_de_peage(), france.gap(), 201.0)

    # Rest day
    builder.rest_day(france.gap())

    # Stage 17
    builder.mountain_stage(france.digne_les_bains())
    builder.summit_finish(mountains.alps.pra_loup(), ColCategory.C1, 161.0)

    # Stage 18
    builder.road_stage(france.gap(), france.saint_jean_de_maurienne(), 186.5)

    # Stage 19
    builder.road_stage(france.saint_jean_de_maurienne(), france.la_toussuire_les_sybelles(), 138.0)

    # Stage 20
    builder.mountain_stage(france.modane())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 110.5)

    # Stage 21
    builder.road_stage(france.sevres(), france.paris(), 109.5)

    return builder.build()

def tdf2016():

    builder = TourDeFranceBuilder(2016,7,2)

    # Stage 1
    builder.road_stage(france.mont_saint_michel(), france.utah_beach(), 188.0)

    # Stage 2
    builder.road_stage(france.saint_lo(), france.cherbourg_en_cotentin(), 183.0)

    # Stage 3
    builder.road_stage(france.granville(), france.angers(), 223.5)

    # Stage 4
    builder.road_stage(france.saumur(), france.limoges(), 237.5)

    # Stage 5
    builder.mountain_stage(france.limoges())
    builder.summit_finish(mountains.massif_central.le_lioran(), ColCategory.C1, 216.0)

    # Stage 6
    builder.road_stage(france.arpajon_sur_cere(), france.montauban(), 190.5)

    # Stage 7
    builder.road_stage(france.l_isle_jourdain(), france.lac_de_payolle(), 162.5)

    # Stage 8
    builder.road_stage(france.pau(), france.bagneres_de_luchon(), 184.0)

    # Stage 9
    builder.mountain_stage(spain.vielha_val_d_aran())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 184.5)

    # Rest day
    builder.rest_day(mountains.pyrenees.arcalis())

    # Stage 10
    builder.road_stage(andorra.escaldes_engordany(), france.revel(), 197.0)

    # Stage 11
    builder.road_stage(france.carcassonne(), france.montpellier(), 162.5)

    # Stage 12
    builder.road_stage(france.montpellier(), france.chalet_reynard(), 178.0)

    # Stage 13
    builder.individual_time_trial(france.bourg_saint_andeol(), france.la_caverne_du_pont_d_arc(), 37.5)

    # Stage 14
    builder.road_stage(france.montelimar(), france.villar_les_dombes(), 208.5)

    # Stage 15
    builder.road_stage(france.bourg_en_bresse(), france.culoz(), 160.0)

    # Stage 16
    builder.road_stage(france.moirans_en_montagne(), switzerland.bern(), 209.0)

    # Rest day
    builder.rest_day(switzerland.bern())

    # Stage 17
    builder.mountain_stage(switzerland.bern())
    builder.summit_finish(mountains.alps.finhaut_emosson(), ColCategory.C1, 184.5)

    # Stage 18
    builder.individual_time_trial(france.sallanches(), france.megeve(), 17.0)

    # Stage 19
    builder.road_stage(france.abbeville(), france.saint_gervais_les_bains(), 146.0)

    # Stage 20
    builder.road_stage(france.megeve(), france.morzine(), 146.5)

    # Stage 21
    builder.road_stage(france.chantilly(), france.paris(), 113.0)

    return builder.build()

def tdf2017():

    builder = TourDeFranceBuilder(2017,7,1)

    # Stage 1
    builder.out_and_back_individual_time_trial(germany.dusseldorf(), 14.0)

    # Stage 2
    builder.road_stage(germany.dusseldorf(), belgium.liege(), 203.5)

    # Stage 3
    builder.road_stage(belgium.verviers(), france.longwy(), 212.5)

    # Stage 4
    builder.road_stage(luxembourg.mondorf_les_bains(), france.vittel(), 207.5)

    # Stage 5
    builder.mountain_stage(france.vittel())
    builder.summit_finish(mountains.vosges.la_planche_des_belles_filles(), ColCategory.C1, 160.5)

    # Stage 6
    builder.road_stage(france.vesoul(), france.troyes(), 216.0)

    # Stage 7
    builder.road_stage(france.troyes(), france.nuits_saint_georges(), 213.5)

    # Stage 8
    builder.road_stage(france.dole(), france.station_des_rousses(), 187.5)

    # Stage 9
    builder.road_stage(france.nantua(), france.chambery(), 181.5)

    # Rest day
    builder.rest_day(france.dordogne())

    # Stage 10
    builder.road_stage(france.perigueux(), france.bergerac(), 178.0)

    # Stage 11
    builder.road_stage(france.eymet(), france.pau(), 203.5)

    # Stage 12
    builder.mountain_stage(france.pau())
    builder.summit_finish(mountains.pyrenees.peyragudes(), ColCategory.C1, 214.5)

    # Stage 13
    builder.road_stage(france.saint_girons(), france.foix(), 101.0)

    # Stage 14
    builder.road_stage(france.blagnac(), france.rodez(), 181.5)

    # Stage 15
    builder.road_stage(france.laissac_severac_l_eglise(), france.le_puy_en_velay(), 189.5)

    # Rest day
    builder.rest_day(france.le_puy_en_velay())

    # Stage 16
    builder.road_stage(france.le_puy_en_velay(), france.romans_sur_isere(), 165.0)

    # Stage 17
    builder.road_stage(france.la_mure(), france.serre_chevalier(), 183.0)

    # Stage 18
    builder.mountain_stage(france.briancon())
    builder.summit_finish(mountains.alps.col_d_izoard(), ColCategory.HC, 179.5)

    # Stage 19
    builder.road_stage(france.embrun(), france.salon_de_provence(), 222.5)

    # Stage 20
    builder.out_and_back_individual_time_trial(france.marseille(), 22.5)

    # Stage 21
    builder.road_stage(france.montgeron(), france.paris(), 103.0)

    return builder.build()
def tdf2018():

    builder = TourDeFranceBuilder(2018,7,7)

    # Stage 1
    builder.road_stage(france.noirmoutier_en_l_ile(), france.fontenay_le_comte(), 201)

    # Stage 2
    builder.road_stage(france.mouilleron_saint_germain(), france.la_roche_sur_yon(), 182.5)

    # Stage 3
    builder.out_and_back_team_time_trial(france.cholet(), 35.5)

    # Stage 4
    builder.road_stage(france.la_baule(), france.sarzeau(), 195)

    # Stage 5
    builder.road_stage(france.lorient(), france.quimper(), 204.5)

    # Stage 6
    builder.mountain_stage(france.brest())
    builder.summit_finish(mountains.massif_amorican.mur_de_bretagne(), ColCategory.C3, 181)

    # Stage 7
    builder.road_stage(france.fougres(), france.chartres(), 231)

    # Stage 8
    builder.road_stage(france.dreux(), france.amiens(), 181)

    # Stage 9
    builder.road_stage(france.arras(), france.roubaix(), 156.5)

    # Rest day 1
    annecy = france.annecy()
    builder.rest_day(annecy)

    # Stage 10
    builder.road_stage(annecy, france.le_grand_bornand(), 158.5)

    # Stage 11
    builder.mountain_stage(france.albertville())
    builder.summit_finish(mountains.alps.la_rosiere(), ColCategory.C1, 108.5)

    # Stage 12
    builder.mountain_stage(france.bourg_saint_maurice())
    builder.summit_finish(mountains.alps.alpe_d_huez(), ColCategory.HC, 175.5)

    # Stage 13
    builder.road_stage(france.le_bourg_d_oisans(), france.valence(), 169.5)

    # Stage 14
    builder.road_stage(france.saint_paul_trois_chateaux(), france.mende(), 188)

    # Stage 15
    builder.road_stage(france.millau(), france.carcassonne(), 181.5)

    # Rest day 2
    builder.rest_day(france.lourdes())

    # Stage 16
    builder.road_stage(france.carcassonne(), france.bagneres_de_luchon(), 218)

    # Stage 17
    builder.mountain_stage(france.bagneres_de_luchon())
    builder.summit_finish(mountains.pyrenees.col_de_portet(), ColCategory.HC, 65)

    # Stage 18
    builder.road_stage(france.trie_sur_basie(), france.pau(), 171)

    # Stage 19
    builder.road_stage(france.lourdes(), france.laruns(), 200.5)

    # Stage 20
    builder.individual_time_trial(france.saint_pee_sur_nivelle(), france.espelette(), 31)

    # Stage 21
    builder.road_stage(france.houilles(), france.paris(), 116)

    return builder.build()
