import country
import france
import mountains.alps
import mountains.alps.provence
from col                import ColCategory
from datetime           import datetime
from stage_race         import Dauphine
from stage_race_builder import StageRaceBuilder

def dauphine2009():

    builder = StageRaceBuilder(Dauphine(), datetime(2009,6,7))

    # Stage 1
    builder.out_and_back_individual_time_trial(france.nancy(), 12.1)

    # Stage 2
    builder.road_stage(france.nancy(), france.dijon(), 228)

    # Stage 3
    builder.road_stage(france.tournus(), france.saint_etienne(), 182)

    # Stage 4
    builder.individual_time_trial(france.bourg_les_valence(), france.valence(), 42.4)

    # Stage 5
    builder.mountain_stage(france.valence())
    builder.summit_finish(mountains.alps.provence.mont_ventoux(), ColCategory.HC, 154)

    # Stage 6
    builder.road_stage(france.gap(), france.briancon(), 106)

    # Stage 7
    builder.road_stage(france.briancon(), france.saint_francois_longchamp(), 157)

    # Stage 8
    builder.road_stage(france.faverges(), france.grenoble(), 146)

    return builder.build()

def dauphine2018():

    builder = StageRaceBuilder(Dauphine(), datetime(2018,6,3))

    # Prologue
    builder.out_and_back_prologue(france.valence(), 6.6)

    # Stage 1
    builder.road_stage(france.valence(), france.saint_just(), 179)

    # Stage 2
    builder.road_stage(france.montbrison(), france.belleville(), 181)

    # Stage 3
    builder.team_time_trial(france.pont_de_vaux(), france.louhans(), 35)

    # Stage 4
    builder.mountain_stage(france.chazey())
    builder.summit_finish(mountains.alps.lans_en_vercors(), ColCategory.C2, 181)

    # Stage 5
    builder.mountain_stage(france.grenoble())
    builder.summit_finish(mountains.alps.valmorel(), ColCategory.HC, 130)

    # Stage 6
    builder.mountain_stage(france.frontenex())
    builder.summit_finish(mountains.alps.la_rosiere(), ColCategory.C1, 110)

    # Stage 7
    builder.mountain_stage(france.moutiers())
    builder.summit_finish(mountains.alps.saint_gervais_mont_blanc(), ColCategory.C1, 136)

    return builder.build()
