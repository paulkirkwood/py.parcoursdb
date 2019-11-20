import country
import andorra
import spain
import mountains.asturias
import mountains.pyrenees
import mountains.sierra_nevada
from col                import Col, ColCategory
from stage_race_builder import TourOfSpainBuilder

def vuelta1991():

    builder = TourOfSpainBuilder(1991,4,29)
    
    # Stage 1
    builder.three_man_team_time_trial(spain.merida(), 8.8)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(spain.merida(), spain.caceres(), 134.5)
    builder.team_time_trial(spain.montigo(), spain.badajoz(), 40.4)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(spain.badajoz(), spain.seville(), 233.2)

    # Stage 4
    builder.road_stage(spain.seville(), spain.jaen(), 292)

    # Stage 5
    builder.road_stage(spain.linares(), spain.albacete(), 227.8)

    # Stage 6
    builder.road_stage(spain.albacete(), spain.valencia(), 236.5)

    # Stage 7
    builder.criterium(spain.palma_de_mallorca(), 188)

    # Stage 8
    builder.out_and_back_individual_time_trial(spain.cala_d_or(), 47)

    # Stage 9
    builder.road_stage(spain.sant_cugat_del_valles(), spain.lloret_de_mar(), 140)

    # Stage 10
    builder.road_stage(spain.lloret_de_mar(), andorra.andorra_la_vella(), 229)

    # Stage 11
    builder.road_stage(andorra.andorra_la_vella(), spain.pla_de_beret(), 0.0)

    # Stage 12
    builder.mountain_stage(spain.bossost())
    builder.summit_finish(mountains.sierra_nevada.cerler(), ColCategory.C1, 111)

    # Stage 13
    builder.road_stage(spain.benasque(), spain.zaragoza(), 219)

    # Stage 14
    builder.individual_time_trial(spain.ezcaray(), spain.valdezcaray(), 24.1)

    # Stage 15
    builder.road_stage(spain.santo_domingo_de_la_calzada(), spain.santander(), 219.5)

    # Stage 16
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 186.6)

    # Stage 17
    builder.road_stage(spain.cangas_de_onis(), spain.alto_del_naranco(), 152)

    # Stage 18
    builder.road_stage(spain.leon(), spain.valladolid(), 137.5)

    # Stage 19
    builder.out_and_back_individual_time_trial(spain.valladolid(), 53.2)

    # Stage 20
    builder.criterium(spain.palazuelos_de_eresma_destilerias_dyc(), 212.7)

    # Stages 21
    builder.road_stage(spain.collado_villalba(), spain.madrid(), 169.6)

    return builder.build()
