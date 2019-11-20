import country
import france
import mountains.alps
import mountains.alps.maritime
from col                import ColCategory
from stage_race_builder import ParisNiceBuilder

def paris_nice2018():

    builder = ParisNiceBuilder(2018,3,4)

    # Stage 1
    builder.road_stage(france.chatou(), france.meudon(), 134.5)

    # Stage 2
    builder.road_stage(france.orsonville(), france.vierzon(), 187.5)

    # Stage 3
    builder.road_stage(france.bourges(), france.chatel_guyon(), 210)

    # Stage 4
    builder.individual_time_trial(france.la_fouillouse(), france.saint_etienne(), 18.4)

    # Stage 5
    builder.road_stage(france.salon_de_provence(), france.sisteron(), 165)

    # Stage 6
    builder.road_stage(france.sisteron(), france.vence(), 198)

    # Stage 7
    builder.mountain_stage(france.nice())
    builder.summit_finish(mountains.alps.maritime.valdeblore_la_colmiane(), ColCategory.C1, 175)

    # Stage 8
    builder.criterium(france.nice(), 110)

    return builder.build()
