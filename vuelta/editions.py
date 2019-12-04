import country
import andorra
import belgium
import france
import portugal
import spain
import mountains.asturias
import mountains.cantabria
import mountains.galicia
import mountains.la_rioja
import mountains.prebaetic
import mountains.pyrenees
import mountains.sierra_de_guadarrama
import mountains.sierra_de_los_filabres
import mountains.sierra_nevada
import mountains.sierra_morena
import mountains.sierra_sur_de_jaen
import mountains.sistema_central
import netherlands
from col                import Col, ColCategory
from location           import vicinity
from stage_race_builder import TourOfSpainBuilder

def vuelta1935():

    builder = TourOfSpainBuilder(1935,4,29)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.valladolid(), 185.0)

    # Stage 2
    builder.road_stage(spain.valladolid(), spain.santander(), 251.0)

    # Transfer day
    builder.rest_day()

    # Stage 3
    builder.road_stage(spain.santander(), spain.bilbao(), 199.0)

    # Stage 4
    builder.road_stage(spain.bilbao(), spain.san_sebastian(), 235.0)

    # Stage 5
    builder.road_stage(spain.san_sebastian(), spain.zaragoza(), 264.0)

    # Stage 6
    builder.road_stage(spain.zaragoza(), spain.barcelona(), 310.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(spain.barcelona(), spain.tortosa(), 188.0)

    # Stage 8
    builder.road_stage(spain.tortosa(), spain.valencia(), 188.0)

    # Stage 9
    builder.road_stage(spain.valencia(), spain.murcia(), 265.0)

    # Stage 10
    builder.road_stage(spain.murcia(), spain.granada(), 285.0)

    # Stage 11
    builder.road_stage(spain.granada(), spain.seville(), 260.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(spain.seville(), spain.caceres(), 270.0)

    # Stage 13
    builder.road_stage(spain.caceres(), spain.zamora(), 275.0)

    # Stage 14
    builder.road_stage(spain.zamora(), spain.madrid(), 250.0)

    return builder.build()

def vuelta1936():

    builder = TourOfSpainBuilder(1936,5,5)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.salamanca(), 210.0)

    # Stage 2
    builder.road_stage(spain.salamanca(), spain.caceres(), 214.0)

    # Stage 3
    builder.road_stage(spain.caceres(), spain.seville(), 270.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(spain.seville(), spain.malaga(), 212.0)

    # Stage 5
    builder.road_stage(spain.malaga(), spain.granada(), 132.0)

    # Stage 6
    builder.road_stage(spain.granada(), spain.almeria(), 185.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(spain.almeria(), spain.alicante(), 306.0)

    # Stage 8
    builder.road_stage(spain.alicante(), spain.valencia(), 184.0)

    # Stage 9
    builder.road_stage(spain.valencia(), spain.tarragona(), 279.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(spain.tarragona(), spain.barcelona(), 129.0)

    # Stage 11
    builder.road_stage(spain.barcelona(), spain.zaragoza(), 293.0)

    # Stage 12
    builder.road_stage(spain.zaragoza(), spain.san_sebastian(), 265.0)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 160.0)

    # Stage 14
    builder.road_stage(spain.bilbao(), spain.santander(), 199.0)

    # Transfer day
    builder.rest_day()

    # Stage 15
    builder.road_stage(spain.santander(), spain.gijon(), 194.0)

    # Stage 16
    builder.road_stage(spain.gijon(), spain.ribadeo(), 155.0)

    # Stage 17
    builder.road_stage(spain.ribadeo(), spain.a_coruna(), 157.0)

    # Stage 18
    builder.road_stage(spain.a_coruna(), spain.vigo(), 175.0)

    # Transfer day
    builder.rest_day()

    # Stage 19
    builder.road_stage(spain.vigo(), spain.verin(), 178.0)

    # Stage 20
    builder.road_stage(spain.verin(), spain.zamora(), 207.0)

    # Stage 21
    builder.road_stage(spain.zamora(), spain.madrid(), 250.0)

    return builder.build()

def vuelta1941():

    builder = TourOfSpainBuilder(1941,6,12)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.salamanca(), 210.0)

    # Stage 2
    builder.road_stage(spain.salamanca(), spain.caceres(), 214.0)

    # Stage 3
    builder.road_stage(spain.caceres(), spain.seville(), 270.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(spain.seville(), spain.malaga(), 212.0)

    # Stage 5
    builder.road_stage(spain.malaga(), spain.almeria(), 220.0)

    # Stage 6
    builder.road_stage(spain.almeria(), spain.murcia(), 223.0)

    # Stage 7
    builder.road_stage(spain.murcia(), spain.valencia(), 248.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(spain.valencia(), spain.tarragona(), 279.0)

    # Stage 9
    builder.road_stage(spain.tarragona(), spain.barcelona(), 112.0)

    # Stage 10
    builder.road_stage(spain.barcelona(), spain.zaragoza(), 294.0)

    # Stage 11
    builder.road_stage(spain.zaragoza(), spain.logrono(), 172.0)

    # Stage 12
    builder.road_stage(spain.logrono(), spain.san_sebastian(), 213.0)

    # Stage 13
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 160.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(spain.bilbao(), spain.santander(), 165.0)

    # Stage 15
    builder.road_stage(spain.santander(), spain.gijon(), 192.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.gijon(), spain.oviedo(), 53.0)
    builder.road_stage(spain.oviedo(), spain.luarca(), 101.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(spain.luarca(), spain.a_coruna(), 219.0)

    # Stage 18
    builder.road_stage(spain.a_coruna(), spain.vigo(), 175.0)

    # Transfer day
    builder.rest_day()

    # Stage 19
    builder.road_stage(spain.vigo(), spain.verin(), 178.0)

    # Stage 20
    builder.road_stage(spain.verin(), spain.valladolid(), 301.0)

    # Stage 21
    builder.road_stage(spain.valladolid(), spain.madrid(), 198.0)

    return builder.build()

def vuelta1942():

    builder = TourOfSpainBuilder(1942,6,30)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.albacete(), 245.0)

    # Stage 2
    builder.road_stage(spain.albacete(), spain.murcia(), 160.0)

    # Stage 3
    builder.road_stage(spain.murcia(), spain.valencia(), 248.0)

    # Transfer day
    builder.rest_day()

    # Stage 4
    builder.road_stage(spain.valencia(), spain.tarragona(), 278.0)

    # Stage 5
    builder.road_stage(spain.tarragona(), spain.barcelona(), 120.0)

    # Stage 6
    builder.road_stage(spain.barcelona(), spain.huesca(), 279.0)

    # Stage 7
    builder.road_stage(spain.huesca(), spain.san_sebastian(), 305.0)

    # Stage 8
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 160.0)

    # Stage 9
    builder.individual_time_trial(spain.bilbao(), spain.castro_urdiales(), 53.0)

    # Stage 10
    builder.road_stage(spain.castro_urdiales(), spain.santander(), 151.0)

    # Stage 11
    builder.road_stage(spain.santander(), spain.reinosa(), 120.0)

    # Stage 12
    builder.road_stage(spain.reinosa(), spain.gijon(), 199.0)

    # Stage 13
    builder.road_stage(spain.gijon(), spain.oviedo(), 75.0)

    # Stage 14
    builder.road_stage(spain.oviedo(), spain.luarca(), 129.0)

    # Stage 15
    builder.road_stage(spain.luarca(), spain.a_coruna(), 219.0)

    # Stage 16a & 16b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.a_coruna(), spain.santiago_de_compostela(), 63.0)
    builder.road_stage(spain.santiago_de_compostela(), spain.vigo(), 110.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(spain.vigo(), spain.ponferrada(), 270.0)

    # Stage 18
    builder.road_stage(spain.ponferrada(), spain.salamanca(), 251.0)

    # Stage 19
    builder.road_stage(spain.salamanca(), spain.madrid(), 248.0)

    return builder.build()

def vuelta1945():

    builder = TourOfSpainBuilder(1945,5,10)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.salamanca(), 212.0)

    # Stage 2
    builder.road_stage(spain.salamanca(), spain.caceres(), 214.0)

    # Stage 3
    builder.road_stage(spain.caceres(), spain.badajoz(), 132.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.badajoz(), spain.almendralejo(), 57.0)
    builder.road_stage(spain.almendralejo(), spain.seville(), 171.0)
    builder.disable_split_stages()

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(spain.seville(), spain.granada(), 251.0)

    # Stage 6
    builder.road_stage(spain.granada(), spain.murcia(), 285.0)

    # Stage 7
    builder.road_stage(spain.murcia(), spain.valencia(), 244.0)

    # Transfer day
    builder.rest_day()

    # Stage 8
    builder.road_stage(spain.valencia(), spain.tortosa(), 188.0)

    # Stage 9
    builder.road_stage(spain.tortosa(), spain.barcelona(), 288.0)

    # Stage 10
    builder.road_stage(spain.barcelona(), spain.zaragoza(), 306.0)

    # Stage 11
    builder.road_stage(spain.zaragoza(), spain.san_sebastian(), 276.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 207.0)

    # Stage 13
    builder.road_stage(spain.bilbao(), spain.santander(), 188.0)

    # Stage 14
    builder.road_stage(spain.santander(), spain.reinosa(), 110.0)

    # Stage 15
    builder.road_stage(spain.reinosa(), spain.gijon(), 200.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.gijon(), spain.leon(), 172.0)

    # Stage 17
    builder.road_stage(spain.leon(), spain.valladolid(), 132.0)

    # Stage 18
    builder.road_stage(spain.valladolid(), spain.madrid(), 185.0)

    return builder.build()

def vuelta1946():

    builder = TourOfSpainBuilder(1946,5,7)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.salamanca(), 212.0)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.salamanca(), spain.bejar(), 73.0)
    builder.road_stage(spain.bejar(), spain.caceres(), 141.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(spain.caceres(), spain.badajoz(), 132.0)

    # Stage 4
    builder.road_stage(spain.badajoz(), spain.seville(), 218.0)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(spain.seville(), spain.granada(), 251.0)

    # Stage 6
    builder.road_stage(spain.granada(), spain.baza(), 107.0)

    # Stage 7
    builder.road_stage(spain.baza(), spain.murcia(), 178.0)

    # Stage 8
    builder.road_stage(spain.murcia(), spain.valencia(), 264.0)

    # Transfer day
    builder.rest_day()

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.team_time_trial(spain.valencia(), spain.castellon(), 67.0)
    builder.road_stage(spain.castellon(), spain.tortosa(), 123.0)
    builder.disable_split_stages()

    # Stage 10
    builder.road_stage(spain.tortosa(), spain.barcelona(), 215.0)

    # Stage 11
    builder.road_stage(spain.barcelona(), spain.lleida(), 162.0)

    # Stage 12
    builder.road_stage(spain.lleida(), spain.zaragoza(), 144.0)

    # Stage 13
    builder.road_stage(spain.zaragoza(), spain.san_sebastian(), 276.0)

    # Transfer day
    builder.rest_day()

    # Stage 14
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 207.0)

    # Stage 15
    builder.road_stage(spain.bilbao(), spain.santander(), 226.0)

    # Stage 16
    builder.road_stage(spain.santander(), spain.reinosa(), 110.0)

    # Stage 17
    builder.road_stage(spain.reinosa(), spain.gijon(), 204.0)

    # Transfer day
    builder.rest_day()

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.gijon(), spain.oviedo(), 53.0)
    builder.road_stage(spain.oviedo(), spain.leon(), 119.0)
    builder.disable_split_stages()

    # Stage 19
    builder.road_stage(spain.leon(), spain.valladolid(), 134.0)

    # Stage 20
    builder.road_stage(spain.valladolid(), spain.madrid(), 200.0)

    return builder.build()

def vuelta1947():

    builder = TourOfSpainBuilder(1947,5,12)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.albacete(), 243.0)

    # Stage 2
    builder.road_stage(spain.albacete(), spain.murcia(), 146.0)

    # Stage 3
    builder.road_stage(spain.murcia(), spain.alcoy(), 135.0)

    # Stage 4
    builder.road_stage(spain.alcoy(), spain.castellon(), 175.0)

    # Stage 5
    builder.road_stage(spain.castellon(), spain.tarragona(), 222.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(spain.tarragona(), spain.barcelona(), 119.0)

    # Stage 7
    builder.road_stage(spain.barcelona(), spain.lleida(), 162.0)

    # Stage 8
    builder.road_stage(spain.lleida(), spain.zaragoza(), 144.0)

    # Stage 9
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 176.0)

    # Stage 10
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 107.0)

    # Stage 11
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 229.0)

    # Stage 12
    builder.road_stage(spain.bilbao(), spain.santander(), 212.0)

    # Stage 13
    builder.road_stage(spain.santander(), spain.reinosa(), 201.0)

    # Stage 14
    builder.road_stage(spain.reinosa(), spain.gijon(), 204.0)

    # Stage 15
    builder.road_stage(spain.gijon(), spain.oviedo(), 105.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(spain.oviedo(), spain.luarca(), 101.0)
    builder.individual_time_trial(spain.luarca(), spain.ribadeo(), 70.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(spain.ribadeo(), spain.ferrol(), 159.0)

    # Stage 18
    builder.road_stage(spain.ferrol(), spain.a_coruna(), 70.0)

    # Stage 19
    builder.road_stage(spain.a_coruna(), spain.vigo(), 180.0)

    # Stage 20
    builder.road_stage(spain.vigo(), spain.ourense(), 105.0)

    # Stage 21
    builder.road_stage(spain.ourense(), spain.astorga(), 228.0)

    # Stage 22
    builder.individual_time_trial(spain.astorga(), spain.leon(), 47.0)

    # Stage 23
    builder.road_stage(spain.leon(), spain.valladolid(), 133.0)

    # Stage 24
    builder.road_stage(spain.valladolid(), spain.madrid(), 220.0)

    return builder.build()

def vuelta1948():

    builder = TourOfSpainBuilder(1948,6,13)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(spain.madrid(), 14.0)
    builder.road_stage(spain.madrid(), spain.valdepenas(), 198.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.valdepenas(), spain.granada(), 232.0)

    # Stage 3
    builder.road_stage(spain.granada(), spain.murcia(), 285.0)

    # Stage 4
    builder.road_stage(spain.murcia(), spain.alicante(), 230.0)

    # Stage 5
    builder.road_stage(spain.alicante(), spain.valencia(), 163.0)

    # Transfer day
    builder.rest_day()

    # Stage 6
    builder.road_stage(spain.valencia(), spain.tortosa(), 201.0)

    # Stage 7
    builder.road_stage(spain.tortosa(), spain.barcelona(), 209.0)

    # Stage 8
    builder.road_stage(spain.barcelona(), spain.lleida(), 203.0)

    # Stage 9
    builder.road_stage(spain.lleida(), spain.zaragoza(), 144.0)

    # Stage 10
    builder.road_stage(spain.zaragoza(), spain.san_sebastian(), 276.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 259.0)

    # Stage 12
    builder.road_stage(spain.bilbao(), spain.santander(), 212.0)

    # Stage 13
    builder.road_stage(spain.santander(), spain.gijon(), 225.0)

    # Stage 14
    builder.road_stage(spain.gijon(), spain.ribadeo(), 200.0)

    # Stage 15
    builder.road_stage(spain.ribadeo(), spain.a_coruna(), 156.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.a_coruna(), spain.ourense(), 156.0)

    # Stage 17
    builder.road_stage(spain.ourense(), spain.leon(), 276.0)

    # Stage 18
    builder.road_stage(spain.leon(), spain.segovia(), 269.0)

    # Stage 19
    builder.road_stage(spain.segovia(), spain.madrid(), 100.0)

    return builder.build()

def vuelta1950():

    builder = TourOfSpainBuilder(1950,8,17)

    # Stage 1
    builder.road_stage(spain.madrid(), spain.valladolid(), 190.0)

    # Stage 2
    builder.road_stage(spain.valladolid(), spain.leon(), 133.0)

    # Stage 3
    builder.road_stage(spain.leon(), spain.gijon(), 148.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.road_stage(spain.gijon(), spain.torrelavega(), 167.0)
    builder.road_stage(spain.torrelavega(), spain.santander(), 78.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(spain.santander(), spain.bilbao(), 177.0)

    # Stage 6
    builder.road_stage(spain.bilbao(), spain.irun(), 240.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(spain.irun(), spain.pamplona(), 109.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.pamplona(), spain.tudela(), 90.0)
    builder.road_stage(spain.tudela(), spain.zaragoza(), 176.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(spain.zaragoza(), spain.lleida(), 144.0)

    # Stage 10
    builder.road_stage(spain.lleida(), spain.barcelona(), 167.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.barcelona(), spain.tarragona(), 150.0)

    # Stage 12
    builder.road_stage(spain.tarragona(), spain.castellon(), 194.0)

    # Stage 13
    builder.individual_time_trial(spain.castellon(), spain.valencia(), 65.0)

    # Stage 14
    builder.road_stage(spain.valencia(), spain.murcia(), 265.0)

    # Stage 15
    builder.road_stage(spain.murica(), spain.lorca(), 117.0)

    # Stage 16
    builder.road_stage(spain.lorca(), spain.granada(), 22.0)

    # Stage 17
    builder.road_stage(spain.granada(), spain.malaga(), 183.0)

    # Transfer day
    builder.rest_day()

    # Stage 18
    builder.road_stage(spain.malaga(), spain.cadiz(), 268.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.cadiz(), spain.jerez_de_la_frontera(), 56.0)
    builder.road_stage(spain.jerez_de_la_frontera(), spain.seville(), 100.0)
    builder.disable_split_stages()

    # Stage 20
    builder.road_stage(spain.seville(), spain.merida(), 200.0)

    # Stage 21
    builder.road_stage(spain.merida(), spain.talavera_de_la_reina(), 228.0)

    # Stage 22
    builder.road_stage(spain.talavera_de_la_reina(), spain.madrid(), 117.0)

    return builder.build()

def vuelta1955():

    builder = TourOfSpainBuilder(1955,4,23)

    # Stage 1
    builder.road_stage(spain.bilbao(), spain.san_sebastian(), 240.0)

    # Stage 2
    builder.road_stage(spain.san_sebastian(), france.bayonne(), 211.0)

    # Stage 3
    builder.road_stage(france.bayonne(), spain.pamplona(), 157.0)

    # Stage 4
    builder.road_stage(spain.pamplona(), spain.zaragoza(), 229.0)

    # Stage 5
    builder.road_stage(spain.zaragoza(), spain.lleida(), 195.0)

    # Stage 6
    builder.road_stage(spain.lleida(), spain.barcelona(), 230.0)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.out_and_back_individual_time_trial(spain.barcelona(), 29.0)

    # Stage 8
    builder.road_stage(spain.barcelona(), spain.tortosa(), 213.0)

    # Stage 9
    builder.road_stage(spain.tortosa(), spain.valencia(), 190.0)

    # Stage 10
    builder.road_stage(spain.valencia(), spain.cuenca(), 222.0)

    # Stage 11
    builder.road_stage(spain.cuenca(), spain.madrid(), 168.0)

    # Stage 12
    builder.out_and_back_team_time_trial(spain.madrid(), 15.0)

    # Stage 13
    builder.road_stage(spain.madrid(), spain.valladolid(), 222.0)

    # Stage 14
    builder.road_stage(spain.valladolid(), spain.bilbao(), 308.0)

    # Stage 15
    builder.criterium(spain.bilbao(), 147.0)

    return builder.build()

def vuelta1956():

    builder = TourOfSpainBuilder(1956,4,26)

    # Stage 1
    builder.road_stage(spain.bilbao(), spain.santander(), 203.0)

    # Stage 2
    builder.road_stage(spain.santander(), spain.oviedo(), 248.0)

    # Stage 3
    builder.road_stage(spain.oviedo(), spain.valladolid(), 175.0)

    # Stage 4
    builder.road_stage(spain.valladolid(), spain.madrid(), 212.0)

    # Stage 5
    builder.road_stage(spain.madrid(), spain.albacete(), 241.0)

    # Stage 6
    builder.road_stage(spain.albacete(), spain.alicante(), 227.0)

    # Stage 7
    builder.road_stage(spain.alicante(), spain.valencia(), 182.0)

    # Stage 8
    builder.road_stage(spain.valencia(), spain.tarragona(), 249.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(spain.tarragona(), spain.barcelona(), 163.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(spain.barcelona(), 21.0)
    builder.road_stage(spain.barcelona(), spain.tarrega(), 112.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(spain.tarrega(), spain.zaragoza(), 238.0)

    # Stage 12
    builder.road_stage(spain.zaragoza(), france.bayonne(), 274.0)

    # Stages 13a & 13b
    builder.enable_split_stages()
    builder.individual_time_trial(france.bayonne(), spain.irun(), 43.0)
    builder.road_stage(spain.irun(), spain.pamplona(), 111.0)
    builder.disable_split_stages()

    # Stage 14
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 195.0)

    # Stage 15
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 225.0)

    # Stage 16
    builder.road_stage(spain.bilbao(), spain.vitoria(), 207.0)

    # Stage 17
    builder.road_stage(spain.vitoria(), spain.bilbao(), 190.0)

    return builder.build()

def vuelta1957():

    builder = TourOfSpainBuilder(1957,4,26)

    # Stage 1
    builder.road_stage(spain.bilbao(), spain.vitoria(), 158.0)

    # Stage 2
    builder.road_stage(spain.vitoria(), spain.santander(), 220.0)

    # Stage 3
    builder.road_stage(spain.santander(), spain.mieres(), 259.0)

    # Stage 4
    builder.road_stage(spain.mieres(), spain.leon(), 0.0)

    # Stage 5
    builder.road_stage(spain.leon(), spain.valladolid(), 172.0)

    # Stage 6
    builder.road_stage(spain.valladolid(), spain.madrid(), 212.0)

    # Stage 7
    builder.criterium(spain.madrid(), 200.0)

    # Stage 8
    builder.road_stage(spain.madrid(), spain.cuenca(), 159.0)

    # Transfer day
    builder.rest_day()

    # Stage 9
    builder.road_stage(spain.cuenca(), spain.valencia(), 249.0)

    # Stage 10
    builder.road_stage(spain.valencia(), spain.tortosa(), 192.0)

    # Stage 11
    builder.road_stage(spain.tortosa(), spain.barcelona(), 199.0)

    # Stage 12
    builder.road_stage(spain.igualada(), spain.zaragoza(), 229.0)

    # Stage 13
    builder.individual_time_trial(spain.zaragoza(), spain.huesca(), 85.0)

    # Stage 14
    builder.road_stage(spain.huesca(), france.bayonne(), 249.0)

    # Stage 15
    builder.road_stage(france.bayonne(), spain.san_sebastian(), 199.0)

    # Stage 16
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 193.0)

    return builder.build()

def vuelta1958():

    builder = TourOfSpainBuilder(1958,4,30)

    # Stage 1
    builder.road_stage(spain.bilbao(), spain.san_sebastian(), 164.0)

    # Stage 2
    builder.road_stage(spain.san_sebastian(), spain.pamplona(), 150.0)

    # Stage 3
    builder.road_stage(spain.pamplona(), spain.zaragoza(), 245.0)

    # Stage 4
    builder.road_stage(spain.zaragoza(), spain.barcelona(), 229.0)

    # Stages 5a & 5b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(spain.barcelona(), 4.0)
    builder.road_stage(spain.barcelona(), spain.tarragona(), 119.0)
    builder.disable_split_stages()

    # Stage 6
    builder.road_stage(spain.tarragona(), spain.valencia(), 263.0)

    # Stage 7
    builder.road_stage(spain.valencia(), spain.cuenca(), 216.0)

    # Stage 8
    builder.road_stage(spain.cuenca(), spain.toledo(), 206.0)

    # Stage 9
    builder.road_stage(spain.toledo(), spain.madrid(), 241.0)

    # Stage 10
    builder.road_stage(spain.madrid(), spain.soria(), 225.0)

    # Stage 11
    builder.road_stage(spain.soria(), spain.vitoria(), 167.0)

    # Stage 12
    builder.road_stage(spain.vitoria(), spain.bilbao(), 169.0)

    # Stages 13a & 13b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.bilbao(), spain.castro_urdiales(), 35.0)
    builder.road_stage(spain.castro_urdiales(), spain.santander(), 105.0)
    builder.disable_split_stages()

    # Stage 14
    builder.road_stage(spain.santander(), spain.gijon(), 221.0)

    # Stage 15
    builder.road_stage(spain.oviedo(), spain.palencia(), 246.0)

    # Stage 16
    builder.road_stage(spain.palencia(), spain.madrid(), 241.0)

    return builder.build()

def vuelta1959():

    builder = TourOfSpainBuilder(1959,4,29)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(spain.madrid(), 9.0)
    builder.road_stage(spain.madrid(), spain.toledo(), 114.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.manzanares(), spain.cordoba(), 228.0)

    # Stage 3
    builder.road_stage(spain.cordoba(), spain.seville(), 140.0)

    # Stage 4
    builder.road_stage(spain.seville(), spain.granada(), 240.0)

    # Stage 5
    builder.road_stage(spain.guadix(), spain.murcia(), 225.0)

    # Stage 6
    builder.road_stage(spain.murcia(), spain.alicante(), 173.0)

    # Stage 7
    builder.road_stage(spain.alicante(), spain.castellon(), 233.0)

    # Stage 8
    builder.road_stage(spain.castellon(), spain.tortosa(), 130.0)

    # Stage 9
    builder.road_stage(spain.tortosa(), spain.barcelona(), 196.0)

    # Stage 10
    builder.road_stage(spain.granollers(), spain.lleida(), 183.0)

    # Stage 11
    builder.road_stage(spain.lleida(), spain.pamplona(), 242.0)

    # Stage 12
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 210.0)

    # Stage 13
    builder.out_and_back_team_time_trial(spain.san_sebastian(), 9.0)

    # Stage 14
    builder.individual_time_trial(spain.eibar(), spain.vitoria(), 62.0)

    # Stage 15
    builder.road_stage(spain.vitoria(), spain.santander(), 230.0)

    # Stage 16
    builder.road_stage(spain.santander(), spain.bilbao(), 187.0)

    # Stage 17
    builder.criterium(spain.bilbao(), 222.0)

    return builder.build()

def vuelta1960():

    builder = TourOfSpainBuilder(1960,4,29)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.gijon(), 8.0)

    # Stage 2
    builder.road_stage(spain.gijon(), spain.a_coruna(), 235.0)

    # Stage 3
    builder.road_stage(spain.a_coruna(), spain.vigo(), 187.0)

    # Stage 4
    builder.road_stage(spain.vigo(), spain.ourense(), 105.0)

    # Stage 5
    builder.road_stage(spain.ourense(), spain.zamora(), 287.0)

    # Stage 6
    builder.road_stage(spain.zamora(), spain.madrid(), 250.0)

    # Stage 7
    builder.criterium(spain.madrid(), 209.0)

    # Stage 8
    builder.road_stage(spain.guadalajara(), spain.zaragoza(), 264.0)

    # Stage 9
    builder.road_stage(spain.zaragoza(), spain.barcelona(), 269.0)

    # Stage 10
    builder.road_stage(spain.barcelona(), spain.barbastro(), 240.0)

    # Stage 11
    builder.road_stage(spain.barbastro(), spain.pamplona(), 267.0)

    # Stage 12
    builder.road_stage(spain.pamplona(), spain.logrono(), 179.0)

    # Stage 13
    builder.road_stage(spain.logrono(), spain.san_sebastian(), 211.0)

    # Stage 14
    builder.road_stage(spain.san_sebastian(), spain.vitoria(), 263.0)

    # Stage 15
    builder.road_stage(spain.vitoria(), spain.santander(), 232.0)

    # Stage 16
    builder.road_stage(spain.santander(), spain.bilbao(), 192.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(spain.bilbao(), spain.guernica(), 116.0)
    builder.individual_time_trial(spain.guernica(), spain.bilbao(), 53.0)
    builder.disable_split_stages()

    return builder.build()

def vuelta1961():

    builder = TourOfSpainBuilder(1961,4,26)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(spain.san_sebastian(), 10.5)
    builder.road_stage(spain.san_sebastian(), spain.pamplona(), 91.0)
    builder.disable_split_stages()

    # Stage 2
    builder.criterium(spain.pamplona(), 174.0)

    # Stage 3
    builder.road_stage(spain.pamplona(), spain.huesca(), 174.0)

    # Stage 4
    builder.road_stage(spain.binefar(), spain.barcelona(), 199.0)

    # Stage 5
    builder.road_stage(spain.barcelona(), spain.tortosa(), 185.0)

    # Stage 6
    builder.road_stage(spain.tortosa(), spain.valencia(), 188.0)

    # Stage 7
    builder.road_stage(spain.valencia(), spain.benidorm(), 141.0)

    # Stage 8
    builder.road_stage(spain.benidorm(), spain.albacete(), 211.0)

    # Stage 9
    builder.road_stage(spain.albacete(), spain.madrid(), 198.0)

    # Stage 10
    builder.criterium(spain.madrid(), 195.0)

    # Stage 11
    builder.road_stage(spain.madrid(), spain.valladolid(), 189.0)

    # Stage 12
    builder.individual_time_trial(spain.valladolid(), spain.palencia(), 48.0)

    # Stage 13
    builder.road_stage(spain.palencia(), spain.santander(), 220.0)

    # Stage 14
    builder.road_stage(spain.santander(), spain.vitoria(), 235.0)

    # Stage 15
    builder.road_stage(spain.vitoria(), spain.bilbao(), 179.0)

    # Stage 16
    builder.criterium(spain.bilbao(), 159.0)

    return builder.build()

def vuelta1962():

    builder = TourOfSpainBuilder(1962,4,27)

    # Stage 1
    builder.criterium(spain.barcelona(), 90.0)

    # Stage 2
    builder.road_stage(spain.barcelona(), spain.tortosa(), 185.0)

    # Stage 3
    builder.road_stage(spain.tortosa(), spain.valencia(), 188.0)

    # Stage 4
    builder.road_stage(spain.valencia(), spain.benidorm(), 141.0)

    # Stage 5
    builder.out_and_back_team_time_trial(spain.benidorm(), 21.0)

    # Stage 6
    builder.road_stage(spain.benidorm(), spain.cartagena(), 152.0)

    # Stage 7
    builder.road_stage(spain.murcia(), spain.almeria(), 223.0)

    # Stage 8
    builder.road_stage(spain.almeria(), spain.malaga(), 220.0)

    # Stage 9
    builder.road_stage(spain.malaga(), spain.cordoba(), 193.0)

    # Stage 10
    builder.road_stage(spain.valapenas(), spain.madrid(), 210.0)

    # Stage 11
    builder.road_stage(spain.madrid(), spain.valladolid(), 189.0)

    # Stage 12
    builder.road_stage(spain.valladolid(), spain.logrono(), 232.0)

    # Stage 13
    builder.road_stage(spain.logrono(), spain.pamplona(), 191.0)

    # Stage 14
    builder.road_stage(spain.pamplona(), france.bayonne(), 149.0)

    # Stage 15
    builder.individual_time_trial(france.bayonne(), spain.san_sebastian(), 82.0)

    # Stage 16
    builder.road_stage(spain.san_sebastian(), spain.vitoria(), 177.0)

    # Stage 17
    builder.road_stage(spain.vitoria(), spain.bilbao(), 171.0)

    return builder.build()

def vuelta1963():

    builder = TourOfSpainBuilder(1963,5,1)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(spain.gijon(), spain.mieres(), 45.0)
    builder.individual_time_trial(spain.mieres(), spain.gijon(), 52.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.gijon(), spain.torrelavega(), 175.0)

    # Stage 3
    builder.road_stage(spain.torrelavega(), spain.vitoria(), 249.0)

    # Stage 4
    builder.road_stage(spain.vitoria(), spain.bilbao(), 104.0)

    # Stage 5
    builder.criterium(spain.bilbao(), 191.0)

    # Stage 6
    builder.road_stage(spain.bilbao(), spain.eibar(), 165.0)

    # Stage 7
    builder.road_stage(spain.eibar(), spain.tolosa(), 138.0)

    # Stage 8
    builder.road_stage(spain.tolosa(), spain.pamplona(), 169.0)

    # Stage 9
    builder.road_stage(spain.pamplona(), spain.zaragoza(), 180.0)

    # Stage 10
    builder.road_stage(spain.zaragoza(), spain.lleida(), 144.0)

    # Stage 11
    builder.road_stage(spain.lleida(), spain.barcelona(), 182.0)

    # Stages 12a & 12b
    builder.enable_split_stages()
    builder.criterium(spain.barcelona(), 80.0)
    builder.individual_time_trial(spain.sitges(), spain.tarragona(), 52.0)
    builder.disable_split_stages()

    # Stage 13
    builder.road_stage(spain.tarragona(), spain.valencia(), 252.0)

    # Stage 14
    builder.road_stage(spain.cuenca(), spain.madrid(), 177.0)

    # Stage 15
    builder.criterium(spain.madrid(), 87.0)

    return builder.build()

def vuelta1964():

    builder = TourOfSpainBuilder(1964,4,30)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(spain.benidorm(), spain.barcelona(), 42.0)
    builder.out_and_back_individual_time_trial(spain.benidorm(), 11.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.benidorm(), spain.nules(), 199.0)

    # Stage 3
    builder.road_stage(spain.nules(), spain.salou(), 212.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.road_stage(spain.salou(), spain.barcelona(), 115.0)
    builder.criterium(spain.barcelona(), 49.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(spain.barcelona(), spain.puigcerda(), 174.0)

    # Stage 6
    builder.road_stage(spain.puigcerda(), spain.lleida(), 187.0)

    # Stage 7
    builder.road_stage(spain.lleida(), spain.jaca(), 201.0)

    # Stage 8
    builder.road_stage(spain.jaca(), spain.pamplona(), 205.0)

    # Stage 9
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 205.0)

    # Stage 10
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 197.0)

    # Stage 11
    builder.road_stage(spain.bilbao(), spain.vitoria(), 107.0)

    # Stage 12
    builder.road_stage(spain.vitoria(), spain.santander(), 211.0)

    # Stage 13
    builder.road_stage(spain.santander(), spain.aviles(), 230.0)

    # Stage 14
    builder.road_stage(spain.aviles(), spain.leon(), 163.0)

    # Stage 15
    builder.individual_time_trial(spain.becilla(), spain.valladolid(), 65.0)

    # Stage 16
    builder.road_stage(spain.valladolid(), spain.madrid(), 209.0)

    # Stage 17
    builder.criterium(spain.madrid(), 87.0)

    return builder.build()

def vuelta1965():

    builder = TourOfSpainBuilder(1965,4,29)

    # Stage 1
    builder.criterium(spain.vigo(), 168.0)

    # Stage 2
    builder.road_stage(spain.pontevedra(), spain.lugo(), 150.0)

    # Stage 3
    builder.road_stage(spain.lugo(), spain.gijon(), 247.0)

    # Stages 4a & 4b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.mieres(), spain.pajares(), 41.0)
    builder.road_stage(spain.pajares(), spain.palencia(), 189.0)
    builder.disable_split_stages()

    # Stage 5
    builder.road_stage(spain.palencia(), spain.madrid(), 238.0)

    # Stage 6
    builder.road_stage(spain.madrid(), spain.cuenca(), 161.0)

    # Stage 7
    builder.road_stage(spain.albacete(), spain.benidorm(), 212.0)

    # Stage 8
    builder.road_stage(spain.benidorm(), spain.sagunto(), 174.0)

    # Stage 9
    builder.road_stage(spain.sagunto(), spain.salou(), 237.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.road_stage(spain.salou(), spain.barcelona(), 115.0)
    builder.criterium(spain.barcelona(), 50.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(spain.barcelona(), andorra.andorra_la_vella(), 241.0)

    # Stage 12
    builder.road_stage(andorra.andorra_la_vella(), spain.lleida(), 158.0)

    # Stage 13
    builder.road_stage(spain.lleida(), spain.zaragoza(), 190.0)

    # Stage 14
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 193.0)

    # Stage 15
    builder.road_stage(spain.pamplona(), france.bayonne(), 149.0)

    # Stage 16
    builder.individual_time_trial(france.saint_pee_sur_nivelle(), spain.san_sebastian(), 61.0)

    # Stage 17
    builder.road_stage(spain.san_sebastian(), spain.vitoria(), 214.0)

    # Stage 18
    builder.road_stage(spain.vitoria(), spain.bilbao(), 222.0)

    return builder.build()

def vuelta1966():

    builder = TourOfSpainBuilder(1966,4,28)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.criterium(spain.murcia(), 111.0)
    builder.out_and_back_individual_time_trial(spain.murcia(), 3.5)
    builder.disable_split_stages()

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(spain.murcia(), spain.la_manga(), 81.0)
    builder.road_stage(spain.la_manga(), spain.benidorm(), 153.0)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(spain.benidorm(), spain.valencia(), 148.0)

    # Stage 4
    builder.road_stage(spain.cuenca(), spain.madrid(), 177.0)

    # Stage 5
    builder.criterium(spain.madrid(), 181.0)

    # Stage 6
    builder.road_stage(spain.madrid(), spain.calatayud(), 225.0)

    # Stage 7
    builder.road_stage(spain.calatayud(), spain.zaragoza(), 105.0)

    # Stage 8
    builder.road_stage(spain.zaragoza(), spain.lleida(), 144.0)

    # Stage 9
    builder.road_stage(spain.lleida(), spain.las_colinas(), 128.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.road_stage(spain.sitges(), spain.barcelona(), 40.0)
    builder.criterium(spain.barcelona(), 49.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(spain.barcelona(), spain.huesca(), 266.0)

    # Stage 12
    builder.road_stage(spain.huesca(), spain.pamplona(), 221.0)

    # Stage 13
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 178.0)

    # Stage 14
    builder.road_stage(spain.san_sebastian(), spain.vitoria(), 178.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.individual_time_trial(spain.vitoria(), spain.haro(), 61.0)
    builder.road_stage(spain.haro(), spain.logrono(), 52.0)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.logrono(), spain.burgos(), 116.0)

    # Stage 17
    builder.road_stage(spain.burgos(), spain.santander(), 226.0)

    # Stage 18
    builder.road_stage(spain.santander(), spain.bilbao(), 154.0)

    return builder.build()

def vuelta1967():

    builder = TourOfSpainBuilder(1967,4,27)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(spain.vigo(), spain.o_baixo_mino(), 110.0)
    builder.out_and_back_individual_time_trial(spain.vigo(), 4.1)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.pontevedra(), spain.ourense(), 186.0)

    # Stage 3
    builder.road_stage(spain.ourense(), spain.astorga(), 230.0)

    # Stage 4
    builder.road_stage(spain.astorga(), spain.salamanca(), 201.0)

    # Stage 5
    builder.road_stage(spain.salamanca(), spain.madrid(), 201.0)

    # Stage 6
    builder.road_stage(spain.albacete(), spain.benidorm(), 212.0)

    # Stage 7
    builder.road_stage(spain.benidorm(), spain.valencia(), 148.0)

    # Stage 8
    builder.road_stage(spain.valencia(), spain.vinaros(), 145.0)

    # Stage 9
    builder.road_stage(spain.vinaros(), spain.sitges(), 172.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.road_stage(spain.sitges(), spain.barcelona(), 39.0)
    builder.criterium(spain.barcelona(), 45.4)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(spain.barcelona(), andorra.andorra_la_vella(), 241.0)

    # Stage 12
    builder.road_stage(andorra.andorra_la_vella(), spain.lleida(), 158.0)

    # Stage 13
    builder.road_stage(spain.lleida(), spain.zaragoza(), 182.0)

    # Stage 14
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 193.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(spain.pamplona(), spain.logrono(), 92.0)
    builder.individual_time_trial(spain.laguardia(), spain.vitoria(), 44.0)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.vitoria(), spain.san_sebastian(), 139.0)

    # Stage 17
    builder.individual_time_trial(spain.villabona(), spain.zarautz(), 28.0)

    # Stage 18
    builder.road_stage(spain.zarautz(), spain.bilbao(), 175.0)

    return builder.build()

def vuelta1968():

    builder = TourOfSpainBuilder(1968,4,25)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.criterium(spain.zaragoza(), 130.0)
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 4.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.zaragoza(), spain.lleida(), 195.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.road_stage(spain.lleida(), spain.barcelona(), 165.0)
    builder.criterium(spain.barcelona(), 38.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(spain.barcelona(), spain.salou(), 108.0)

    # Stage 5
    builder.road_stage(spain.salou(), spain.vinaros(), 106.0)

    # Stage 6
    builder.road_stage(spain.vinaros(), spain.valencia(), 148.0)

    # Stage 7
    builder.road_stage(spain.valencia(), spain.benidorm(), 144.0)

    # Stage 8
    builder.road_stage(spain.benidorm(), spain.almansa(), 167.0)

    # Stage 9
    builder.road_stage(spain.almansa(), spain.alcazar_de_san_juan(), 230.0)

    # Stage 10
    builder.road_stage(spain.alcazar_de_san_juan(), spain.madrid(), 173.0)

    # Stage 11
    builder.road_stage(spain.madrid(), spain.palencia(), 242.0)

    # Stage 12
    builder.road_stage(spain.villalon_de_campos(), spain.gijon(), 236.0)

    # Stage 13
    builder.road_stage(spain.gijon(), spain.santander(), 203.0)

    # Stage 14
    builder.road_stage(spain.santander(), spain.vitoria(), 244.0)

    # Stage 15
    builder.road_stage(spain.vitoria(), spain.pamplona(), 0.0)

    # Stage 16
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 204.0)

    # Stage 17
    builder.individual_time_trial(spain.san_sebastian(), spain.tolosa(), 67.0)

    # Stage 18
    builder.road_stage(spain.tolosa(), spain.bilbao(), 206.0)

    return builder.build()

def vuelta1969():

    builder = TourOfSpainBuilder(1969,4,23)

    # Stages 1A & 1B
    builder.enable_a_b_stage()
    builder.out_and_back_individual_time_trial(spain.badajoz(), 6.5)
    builder.criterium(spain.badajoz(), 246.0)

    # Stage 2
    builder.road_stage(spain.badajoz(), spain.caceres(), 135.0)

    # Stage 3
    builder.road_stage(spain.caceres(), spain.talavera_de_la_reina(), 190.0)

    # Stage 4
    builder.road_stage(spain.talavera_de_la_reina(), spain.madrid(), 124.0)

    # Stage 5
    builder.road_stage(spain.madrid(), spain.alcazar_de_san_juan(), 162.0)

    # Stage 6
    builder.road_stage(spain.alcazar_de_san_juan(), spain.almansa(), 231.0)

    # Stage 7
    builder.road_stage(spain.almansa(), spain.nules(), 233.0)

    # Stage 8
    builder.road_stage(spain.nules(), spain.benicassim(), 199.0)

    # Stage 9
    builder.road_stage(spain.benicassim(), spain.reus(), 169.0)

    # Stage 10
    builder.road_stage(spain.reus(), spain.barcelona(), 146.0)

    # Stage 11
    builder.road_stage(spain.barcelona(), spain.sant_feliu_de_guixols(), 118.0)

    # Stage 12
    builder.road_stage(spain.sant_feliu_de_guixols(), spain.moia(), 151.0)

    # Stage 13
    builder.road_stage(spain.moia(), spain.barbastro(), 229.0)

    # Stages 14a & 14b
    builder.enable_split_stages()
    builder.road_stage(spain.barbastro(), spain.zaragoza(), 125.0)
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 4.0)
    builder.disable_split_stages()

    # Stage 15
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 176.0)

    # Stage 16
    builder.individual_time_trial(spain.irun(), spain.san_sebastian(), 25.0)

    # Stage 17
    builder.road_stage(spain.san_sebastian(), spain.vitoria(), 129.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(spain.vitoria(), spain.llodio(), 76.0)
    builder.individual_time_trial(spain.llodio(), spain.bilbao(), 29.0)
    builder.disable_split_stages()

    return builder.build()

def vuelta1970():

    builder = TourOfSpainBuilder(1970,4,23)

    # Prologue
    builder.out_and_back_prologue(spain.cadiz(), 6.0)

    # Stage 1
    builder.road_stage(spain.cadiz(), spain.jerez_de_la_frontera(), 170.0)

    # Stage 2
    builder.road_stage(spain.jerez_de_la_frontera(), spain.fuengirola(), 217.0)

    # Stage 3
    builder.road_stage(spain.fuengirola(), spain.almeria(), 249.0)

    # Stage 4
    builder.road_stage(spain.almeria(), spain.lorca(), 161.0)

    # Stage 5
    builder.road_stage(spain.lorca(), spain.calp(), 209.0)

    # Stage 6
    builder.road_stage(spain.calp(), spain.borriana(), 198.0)

    # Stage 7
    builder.road_stage(spain.borriana(), spain.tarragona(), 201.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(spain.tarragona(), spain.barcelona(), 100.0)
    builder.criterium(spain.barcelona(), 48.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(spain.barcelona(), spain.igualada(), 189.0)

    # Stage 10
    builder.road_stage(spain.igualada(), spain.zaragoza(), 237.0)

    # Stage 11
    builder.road_stage(spain.zaragoza(), spain.calatayud(), 118.0)

    # Stage 12
    builder.road_stage(spain.calatayud(), spain.madrid(), 204.0)

    # Stage 13
    builder.road_stage(spain.madrid(), spain.soria(), 221.0)

    # Stage 14
    builder.road_stage(spain.soria(), spain.valladolid(), 238.0)

    # Stage 15
    builder.road_stage(spain.valladolid(), spain.burgos(), 134.0)

    # Stage 16
    builder.road_stage(spain.burgos(), spain.santander(), 179.0)

    # Stage 17
    builder.road_stage(spain.santander(), spain.vitoria(), 191.0)

    # Stage 18
    builder.road_stage(spain.vitoria(), spain.san_sebastian(), 157.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(spain.san_sebastian(), spain.llodio(), 104.0)
    builder.individual_time_trial(spain.llodio(), spain.bilbao(), 29.0)
    builder.disable_split_stages()

    return builder.build()

def vuelta1971():

    builder = TourOfSpainBuilder(1971,4,29)

    # Prologue
    builder.out_and_back_prologue(spain.almeria(), 4.2)

    # Stage 1
    builder.criterium(spain.almeria(), 126.0)

    # Stage 2
    builder.road_stage(spain.aguilas(), spain.calp(), 245.0)

    # Stage 3
    builder.road_stage(spain.calp(), spain.la_pobla_de_farnals(), 164.0)

    # Stage 4
    builder.road_stage(spain.la_pobla_de_farnals(), spain.benicassim(), 175.0)

    # Stage 5
    builder.road_stage(spain.benicassim(), spain.salou(), 172.0)

    # Stage 6
    builder.road_stage(spain.salou(), spain.barcelona(), 149.0)

    # Stage 7
    builder.road_stage(spain.barcelona(), spain.manresa(), 179.0)

    # Stage 8
    builder.road_stage(spain.balaguer(), spain.jaca(), 211.0)

    # Stage 9
    builder.road_stage(spain.jaca(), spain.pamplona(), 175.0)

    # Stage 10
    builder.road_stage(spain.pamplona(), spain.san_sebastian(), 120.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(spain.san_sebastian(), spain.bilbao(), 140.0)
    builder.out_and_back_individual_time_trial(spain.bilbao(), 2.6)
    builder.disable_split_stages()

    # Stage 12
    builder.road_stage(spain.bilbao(), spain.vitoria(), 185.0)

    # Stage 13
    builder.road_stage(spain.vitoria(), spain.torrelavega(), 208.0)

    # Stage 14
    builder.road_stage(spain.torrelavega(), spain.burgos(), 192.0)

    # Stage 15
    builder.road_stage(spain.burgos(), spain.segovia(), 188.0)

    # Stage 16
    builder.road_stage(spain.segovia(), spain.avila(), 114.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(spain.avila(), spain.madrid(), 138.0)
    builder.out_and_back_individual_time_trial(spain.madrid(), 5.3)
    builder.disable_split_stages()

    return builder.build()

def vuelta1972():

    builder = TourOfSpainBuilder(1972,4,27)

    # Prologue
    builder.out_and_back_prologue(spain.fuengirola(), 6.0)

    # Stage 1
    builder.road_stage(spain.fuengirola(), spain.cabra(), 167.0)

    # Stage 2
    builder.road_stage(spain.cabra(), spain.granada(), 206.0)

    # Stage 3
    builder.road_stage(spain.granada(), spain.almeria(), 181.0)

    # Stage 4
    builder.road_stage(spain.almeria(), spain.dehesa_de_campoamor(), 251.0)

    # Stage 5
    builder.road_stage(spain.dehesa_de_campoamor(), spain.gandia(), 183.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(spain.gandia(), spain.el_saler(), 120.0)
    builder.out_and_back_team_time_trial(spain.el_saler(), 6.5)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(spain.valencia(), spain.vinaros(), 181.0)

    # Stage 8
    builder.road_stage(spain.vinaros(), spain.tarragona(), 189.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.road_stage(spain.tarragona(), spain.barcelona(), 118.0)
    builder.out_and_back_individual_time_trial(spain.barcelona(), 10.0)
    builder.disable_split_stages()

    # Stage 10
    builder.road_stage(spain.barcelona(), spain.banyoles(), 192.0)

    # Stage 11
    builder.road_stage(spain.manresa(), spain.zaragoza(), 259.0)

    # Stage 12
    builder.mountain_stage(spain.zaragoza())
    builder.summit_finish(mountains.pyrenees.formigal(), ColCategory.C1, 169)

    # Stage 13
    builder.road_stage(spain.sanguesa(), spain.arrate(), 201.0)

    # Stage 14
    builder.road_stage(spain.eibar(), spain.bilbao(), 145.0)

    # Stage 15
    builder.road_stage(spain.bilbao(), spain.torrelavega(), 148.0)

    # Stage 16
    builder.road_stage(spain.torrelavega(), spain.vitoria(), 219.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(spain.vitoria(), spain.san_sebastian(), 138.0)
    builder.out_and_back_individual_time_trial(spain.san_sebastian(), 20.0)
    builder.disable_split_stages()

    return builder.build()

def vuelta1973():

    builder = TourOfSpainBuilder(1973,4,26)

    # Prologue
    builder.out_and_back_prologue(spain.calp(), 5.0)

    # Stage 1
    builder.road_stage(spain.calp(), spain.murcia(), 187.0)

    # Stage 2
    builder.road_stage(spain.murcia(), spain.albacete(), 156.0)

    # Stage 3
    builder.road_stage(spain.albacete(), spain.alcazar_de_san_juan(), 146.0)

    # Stage 4
    builder.road_stage(spain.alcazar_de_san_juan(), spain.cuenca(), 169.0)

    # Stage 5
    builder.road_stage(spain.cuenca(), spain.teruel(), 191.0)

    # Stages 6a & 6b
    builder.enable_split_stages()
    builder.road_stage(spain.teruel(), spain.la_pobla_de_farnals(), 150.0)
    builder.out_and_back_team_time_trial(spain.la_pobla_de_farnals(), 5.0)
    builder.disable_split_stages()

    # Stage 7
    builder.road_stage(spain.la_pobla_de_farnals(), spain.castellon_de_la_plana(), 165.0)

    # Stage 8
    builder.road_stage(spain.castellon_de_la_plana(), spain.calafell(), 245.0)

    # Stages 9a & 9b
    builder.enable_split_stages()
    builder.road_stage(spain.calafell(), spain.barcelona(), 80.0)
    builder.out_and_back_individual_time_trial(spain.barcelona(), 37.9)
    builder.disable_split_stages()

    # Stage 10
    builder.road_stage(spain.barcelona(), spain.empuriabrava(), 171.0)

    # Stage 11
    builder.road_stage(spain.empuriabrava(), spain.manresa(), 225.0)

    # Stage 12
    builder.road_stage(spain.manresa(), spain.zaragoza(), 259.0)

    # Stage 13
    builder.road_stage(spain.mallen(), spain.irache(), 175.0)

    # Stage 14
    builder.road_stage(spain.irache(), spain.bilbao(), 182.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(spain.bilbao(), spain.torrelavega(), 154.0)
    builder.out_and_back_individual_time_trial(spain.torrelavega(), 17.4)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.torrelavega(), spain.miranda_de_ebro(), 203.0)

    # Stages 17a & 17b
    builder.enable_split_stages()
    builder.road_stage(spain.miranda_de_ebro(), spain.tortosa(), 127.0)
    builder.individual_time_trial(spain.hernani(), spain.san_sebastian(), 10.5)
    builder.disable_split_stages()

    return builder.build()

def vuelta1974():

    builder = TourOfSpainBuilder(1974,4,23)

    # Prologue
    builder.out_and_back_prologue(spain.almeria(), 5.0)

    # Stage 1
    builder.criterium(spain.almeria(), 98.0)

    # Stage 2
    builder.road_stage(spain.almeria(), spain.granada(), 187.0)

    # Stage 3
    builder.road_stage(spain.granada(), spain.fuengirola(), 161.0)

    # Stage 4
    builder.road_stage(spain.marbella(), spain.seville(), 206.0)

    # Stage 5
    builder.road_stage(spain.seville(), spain.cordoba(), 139.0)

    # Stage 6
    builder.road_stage(spain.cordoba(), spain.ciudad_real(), 211.0)

    # Stage 7
    builder.road_stage(spain.ciudad_real(), spain.toledo(), 126.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(spain.toledo(), spain.madrid(), 167.0)
    builder.out_and_back_team_time_trial(spain.circuito_del_jarama(), 4.0)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(spain.madrid(), spain.los_angeles_de_san_rafael(), 158.0)

    # Stages 10a & 10b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(spain.los_angeles_de_san_rafael(), 5.0)
    builder.road_stage(spain.los_angeles_de_san_rafael(), spain.avila(), 125.0)
    builder.disable_split_stages()

    # Stage 11
    builder.road_stage(spain.avila(), spain.valladolid(), 168.0)

    # Stage 12
    builder.road_stage(spain.valladolid(), spain.leon(), 203.0)

    # Stage 13
    builder.road_stage(spain.leon(), spain.monte_naranco(), 128.0)

    # Stage 14
    builder.road_stage(spain.oviedo(), spain.cangas_de_onis(), 134.0)

    # Stage 15
    builder.road_stage(spain.cangas_de_onis(), spain.laredo(), 210.0)

    # Stage 16
    builder.road_stage(spain.laredo(), spain.bilbao(), 133.0)

    # Stage 17
    builder.road_stage(spain.bilbao(), spain.miranda_de_ebro(), 157.0)

    # Stage 18
    builder.road_stage(spain.miranda_de_ebro(), spain.eibar(), 152.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(spain.eibar(), spain.san_sebastian(), 79.0)
    builder.out_and_back_individual_time_trial(spain.san_sebastian(), 35.9)
    builder.disable_split_stages()

    return builder.build()

def vuelta1975():

    builder = TourOfSpainBuilder(1975,4,22)

    # Prologue
    builder.out_and_back_prologue(spain.fuengirola(), 4.4)

    # Stage 1
    builder.criterium(spain.marbella(), 78.0)

    # Stage 2
    builder.road_stage(spain.malaga(), spain.granada(), 143.0)

    # Stage 3
    builder.criterium(spain.granada(), 179.0)

    # Stage 4
    builder.road_stage(spain.almeria(), spain.aguilas(), 178.0)

    # Stage 5
    builder.road_stage(spain.aguilas(), spain.murcia(), 176.0)

    # Stage 6
    builder.road_stage(spain.murcia(), spain.benidorm(), 217.0)

    # Stage 7
    builder.out_and_back_individual_time_trial(spain.benidorm(), 8.3)

    # Stage 8
    builder.road_stage(spain.benidorm(), spain.la_pobla_de_farnals(), 217.0)

    # Stage 9
    builder.road_stage(spain.la_pobla_de_farnals(), spain.vinaros(), 157.0)

    # Stage 10
    builder.road_stage(spain.vinaros(), spain.cambrils(), 173.0)

    # Stage 11
    builder.road_stage(spain.cambrils(), spain.barcelona(), 151.0)

    # Stage 12
    builder.criterium(spain.palma_de_mallorca(), 181.0)

    # Stage 13
    builder.road_stage(spain.barcelona(), spain.tremp(), 189.0)

    # Stage 14
    builder.mountain_stage(spain.tremp())
    builder.summit_finish(mountains.pyrenees.formigal(), ColCategory.C1, 233)

    # Stage 15
    builder.road_stage(spain.jaca(), spain.irache(), 160.0)

    # Stage 16
    builder.road_stage(spain.irache(), spain.urkiola(), 150.0)

    # Stage 17
    builder.road_stage(spain.durango(), spain.bilbao(), 123.0)

    # Stage 18
    builder.road_stage(spain.bilbao(), spain.miranda_de_ebro(), 186.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(spain.miranda_de_ebro(), spain.beasain(), 110.0)
    builder.out_and_back_individual_time_trial(spain.san_sebastian(), 31.7)
    builder.disable_split_stages()

    return builder.build()

def vuelta1976():

    builder = TourOfSpainBuilder(1976,4,27)

    # Prologue
    builder.out_and_back_prologue(spain.estepona(), 3.2)

    # Stage 1
    builder.criterium(spain.estepona(), 135.0)

    # Stage 2
    builder.road_stage(spain.estepona(), spain.priego_de_cordoba(), 224.0)

    # Stage 3
    builder.road_stage(spain.priego_de_cordoba(), spain.jaen(), 177.0)

    # Stage 4
    builder.road_stage(spain.jaen(), spain.baza(), 166.0)

    # Stage 5
    builder.road_stage(spain.baza(), spain.cartagena(), 201.0)

    # Stage 6
    builder.out_and_back_individual_time_trial(spain.cartagena(), 14.0)

    # Stage 7
    builder.road_stage(spain.cartagena(), spain.murcia(), 136.0)

    # Stage 8
    builder.road_stage(spain.murcia(), spain.almansa(), 219.0)

    # Stage 9
    builder.road_stage(spain.almansa(), spain.nules(), 208.0)

    # Stage 10
    builder.road_stage(spain.castellon(), spain.cambrils(), 226.0)

    # Stage 11
    builder.road_stage(spain.cambrils(), spain.barcelona(), 151.0)

    # Stage 12
    builder.road_stage(spain.pamplona(), spain.logrono(), 168.0)

    # Stage 13
    builder.road_stage(spain.logrono(), spain.palencia(), 209.0)

    # Stage 14
    builder.road_stage(spain.parades_de_nava(), spain.gijon(), 249.0)

    # Stage 15
    builder.road_stage(spain.gijon(), spain.cangas_de_onis(), 141.0)

    # Stage 16
    builder.road_stage(spain.cangas_de_onis(), spain.reinosa(), 156.0)

    # Stage 17
    builder.road_stage(spain.reinosa(), spain.bilbao(), 183.0)

    # Stage 18
    builder.road_stage(spain.galdacano(), spain.sanctuario_de_oro(), 204.0)

    # Stage 19
    builder.road_stage(spain.murgia(), spain.san_sebastian(), 139.0)

    # Stages 20a & 20b
    builder.enable_split_stages()
    builder.road_stage(spain.murgia(), spain.san_sebastian(), 139.0)
    builder.out_and_back_individual_time_trial(spain.san_sebastian(), 31.7)
    builder.disable_split_stages()

    return builder.build()

def vuelta1977():

    builder = TourOfSpainBuilder(1977,4,26)

    # Prologue
    builder.out_and_back_prologue(spain.dehesa_de_campoamor(), 8.0)

    # Stage 1
    builder.road_stage(spain.dehesa_de_campoamor(), spain.la_manga(), 115.0)

    # Stage 2
    builder.road_stage(spain.la_managa(), spain.murcia(), 161.0)

    # Stage 3
    builder.road_stage(spain.murcia(), spain.benidorm(), 200.0)

    # Stage 4
    builder.out_and_back_individual_time_trial(spain.benidorm(), 8.3)

    # Stage 5
    builder.road_stage(spain.benidorm(), spain.el_saler(), 159.0)

    # Stage 6
    builder.road_stage(spain.valencia(), spain.teruel(), 170.0)

    # Stage 7
    builder.road_stage(spain.teruel(), spain.alcala_de_xivert(), 204.0)

    # Stage 8
    builder.road_stage(spain.alcala_de_xivert(), spain.tortosa(), 141.0)

    # Stage 9
    builder.road_stage(spain.tortosa(), spain.salou(), 144.0)

    # Stage 10
    builder.road_stage(spain.salou(), spain.barcelona(), 144.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.out_and_back_individual_time_trial(spain.barcelona(), 3.8)
    builder.criterium(spain.barcelona(), 45.0)
    builder.disable_split_stages()

    # Stage 12
    builder.road_stage(spain.barcelona(), spain.la_tossa_de_montbui(), 198.0)

    # Stage 13
    builder.road_stage(spain.igualada(), spain.la_seu_d_urgell(), 135.0)

    # Stage 14
    builder.road_stage(spain.la_seu_d_urgell(), spain.monzon(), 200.0)

    # Stage 15
    builder.mountain_stage(spain.monzon())
    builder.summit_finish(mountains.pyrenees.formigal(), ColCategory.C1, 166)

    # Stage 16
    builder.road_stage(spain.formigal(), spain.cordovilla(), 170.0)

    # Stage 17
    builder.road_stage(spain.cordovilla(), spain.bilbao(), 183.0)

    # Stage 18
    builder.road_stage(spain.bilbao(), spain.urkiola(), 126.0)

    # Stage 19
    builder.road_stage(spain.durango(), spain.miranda_de_ebro(), 104.0)

    return builder.build()

def vuelta1978():

    builder = TourOfSpainBuilder(1978,4,25)

    # Prologue
    builder.out_and_back_prologue(spain.gijon(), 8.6)

    # Stage 1
    builder.criterium(spain.gijon(), 144.0)

    # Stage 2
    builder.road_stage(spain.gijon(), spain.cangas_de_onis(), 94.0)

    # Stage 3
    builder.road_stage(spain.cangas_de_onis(), spain.leon(), 187.0)

    # Stage 4
    builder.road_stage(spain.leon(), spain.valladolid(), 171.0)

    # Stage 5
    builder.road_stage(spain.valladolid(), spain.avila(), 136.0)

    # Stage 6
    builder.road_stage(spain.torrelaguna(), spain.torrejon_de_ardoz(), 46.0)

    # Stage 7
    builder.road_stage(spain.torrejon_de_ardoz(), spain.cuenca(), 160.0)

    # Stage 8
    builder.road_stage(spain.cuenca(), spain.benicassim(), 249.0)

    # Stage 9
    builder.road_stage(spain.benicassim(), spain.tortosa(), 156.0)

    # Stage 10
    builder.road_stage(spain.tortosa(), spain.calafell(), 201.0)

    # Stages 11a & 11b
    builder.enable_split_stages()
    builder.road_stage(spain.calafell(), spain.barcelona(), 67.0)
    builder.out_and_back_individual_time_trial(spain.barcelona(), 3.8)
    builder.disable_split_stages()

    # Stage 12
    bellaterra = vicinity(spain.bellaterra(), "Cerdanyola del Vallès")
    la_tossa_de_montbui = vicinity(spain.la_tossa_de_montbui(), "Santa Margarida de Montbui")
    builder.road_stage(bellaterra, la_tossa_de_montbui, 205)

    # Stage 13
    builder.road_stage(spain.igualada(), spain.jaca(), 243.0)

    # Stage 14
    builder.road_stage(spain.jaca(), spain.logrono(), 219.0)

    # Stage 15
    builder.road_stage(spain.logrono(), spain.miranda_de_ebro(), 131.0)

    # Stage 16
    builder.road_stage(spain.miranda_de_ebro(), spain.bien_aparecida_sanctuary(), 208.0)

    # Stage 17
    builder.road_stage(spain.ampuero(), spain.bilbao(), 123.0)

    # Stage 18
    builder.road_stage(spain.bilbao(), spain.amurrio(), 154.0)

    # Stages 19a & 19b
    builder.enable_split_stages()
    builder.road_stage(spain.amurrio(), spain.san_sebastian(), 84.0)
    builder.out_and_back_individual_time_trial(spain.san_sebastian(), 0.0)
    builder.disable_split_stages()

    return builder.build()

def vuelta1979():

    builder = TourOfSpainBuilder(1979,4,24)

    # Prologue
    builder.out_and_back_prologue(spain.jerez_de_la_frontera(), 6.3)

    # Stage 1
    builder.road_stage(spain.jerez_de_la_frontera(), spain.seville(), 156.0)

    # Stage 2
    builder.road_stage(spain.seville(), spain.cordoba(), 188.0)

    # Stage 3
    builder.mountain_stage(spain.cordoba())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 190)

    # Stage 4
    builder.road_stage(spain.granada(), spain.puerto_lumbreras(), 222.0)

    # Stage 5
    builder.road_stage(spain.puerto_lumbreras(), spain.murcia(), 139.0)

    # Stage 6
    builder.road_stage(spain.murcia(), spain.alcoy(), 171.0)

    # Stage 7
    builder.road_stage(spain.alcoy(), spain.sedavi(), 173.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(spain.sedavi(), spain.benicassim(), 145.0)
    builder.out_and_back_individual_time_trial(spain.benicassim(), 11.3)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(spain.benicassim(), spain.reus(), 193.0)

    # Stage 10
    builder.road_stage(spain.reus(), spain.zaragoza(), 230.0)

    # Stage 11
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 183.0)

    # Stage 12
    builder.road_stage(spain.pamplona(), spain.logrono(), 149.0)

    # Stage 13
    builder.road_stage(spain.haro(), spain.pena_cabarga(), 180.0)

    # Stage 14
    builder.road_stage(spain.torrelavega(), spain.gijon(), 178.0)

    # Stage 15
    builder.road_stage(spain.gijon(), spain.leon(), 156.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(spain.leon(), spain.valladolid(), 134.0)
    builder.out_and_back_individual_time_trial(spain.valladolid(), 22.0)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(spain.valladolid(), spain.avila(), 204.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(spain.avila(), spain.colmenar_viejo(), 155.0)
    builder.road_stage(spain.colmenar_viejo(), spain.azuqueca_de_henares(), 104.0)
    builder.disable_split_stages()

    # Stage 19
    builder.criterium(spain.madrid(), 84.0)

    return builder.build()

def vuelta1980():

    builder = TourOfSpainBuilder(1980,4,22)

    # Prologue
    builder.out_and_back_prologue(spain.la_manga(), 10.0)

    # Stage 1
    builder.road_stage(spain.la_manga(), spain.benidorm(), 155.0)

    # Stage 2
    builder.road_stage(spain.benidorm(), spain.cuenca(), 170.0)

    # Stage 3
    builder.road_stage(spain.cullera(), spain.vinaros(), 207.0)

    # Stage 4
    builder.road_stage(spain.vinaros(), spain.sant_quirze_del_valles(), 214.0)

    # Stage 5
    builder.road_stage(spain.sant_quirze_del_valles(), spain.la_seu_d_urgell(), 200.0)

    # Stage 6
    builder.road_stage(spain.la_seu_d_urgell(), spain.viella(), 131.0)

    # Stage 7
    builder.road_stage(spain.viella(), spain.jaca(), 216.0)

    # Stage 8
    builder.road_stage(spain.monastery_of_leyre(), spain.logrono(), 160.0)

    # Stage 9
    builder.road_stage(spain.logrono(), spain.burgos(), 138.0)

    # Stage 10
    builder.road_stage(spain.burgos(), spain.santander(), 178.0)

    # Stage 11
    builder.road_stage(spain.santander(), spain.gijon(), 219.0)

    # Stage 12
    builder.road_stage(spain.santiago_de_compostela(), spain.pontevedra(), 133.0)

    # Stage 13
    builder.road_stage(spain.pontevedra(), spain.vigo(), 195.0)

    # Stage 14
    builder.road_stage(spain.vigo(), spain.ourense(), 156.0)

    # Stage 15
    builder.road_stage(spain.ourense(), spain.ponferrada(), 164.0)

    # Stages 16a & 16b
    builder.enable_split_stages()
    builder.road_stage(spain.ponferrada(), spain.leon(), 131.0)
    builder.out_and_back_individual_time_trial(spain.leon(), 22.8)
    builder.disable_split_stages()

    # Stage 17
    builder.road_stage(spain.leon(), spain.valladolid(), 138.0)

    # Stage 18
    builder.road_stage(spain.valladolid(), spain.los_angeles_de_san_rafael(), 197.0)

    # Stage 19
    builder.criterium(spain.madrid(), 84.0)

    return builder.build()

def vuelta1981():

    builder = TourOfSpainBuilder(1981,4,21)

    # Prologue
    builder.out_and_back_prologue(spain.santander(), 6.3)

    # Stage 1
    builder.road_stage(spain.santander(), spain.aviles(), 221.0)

    # Stage 2
    builder.road_stage(spain.aviles(), spain.leon(), 159.0)

    # Stage 3
    builder.road_stage(spain.leon(), spain.salamanca(), 195.0)

    # Stage 4
    builder.road_stage(spain.salamanca(), spain.caceres(), 206.0)

    # Stage 5
    builder.road_stage(spain.caceres(), spain.merida(), 152.0)

    # Stage 6
    builder.road_stage(spain.merida(), spain.seville(), 199.0)

    # Stage 7
    builder.road_stage(spain.ecija(), spain.jaen(), 181.0)

    # Stages 8a & 8b
    builder.enable_split_stages()
    builder.road_stage(spain.jaen(), spain.granada(), 100.0)
    builder.mountain_time_trial(spain.granada())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 30.5)
    builder.disable_split_stages()

    # Stage 9
    builder.road_stage(spain.baza(), spain.murcia(), 204.0)

    # Stage 10
    builder.road_stage(spain.murcia(), spain.almussafes(), 223.0)

    # Stage 11
    builder.road_stage(spain.almussafes(), spain.peniscola(), 193.0)

    # Stage 12
    builder.road_stage(spain.peniscola(), spain.esparreguera(), 217.0)

    # Stage 13
    builder.road_stage(spain.esparreguera(), spain.rasos_de_peguera(), 187.0)

    # Stage 14
    builder.road_stage(spain.gironella(), spain.balaguer(), 197.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(spain.balaguer(), spain.alfajarin(), 146.0)
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 11.3)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.calatayud(), spain.torrejon_de_ardoz(), 209.0)

    # Stage 17
    builder.road_stage(spain.torrejon_de_ardoz(), spain.segovia(), 150.0)

    # Stage 18
    builder.road_stage(spain.segovia(), spain.los_angeles_de_san_rafael(), 175.0)

    # Stage 19
    builder.criterium(spain.madrid(), 84.0)

    return builder.build()

def vuelta1982():

    builder = TourOfSpainBuilder(1982,4,20)

    # Prologue
    builder.out_and_back_prologue(spain.santiago_de_compostela(), 6.7)

    # Stages 1a & 1b
    builder.enable_split_stages()
    builder.road_stage(spain.santiago_de_compostela(), spain.a_coruna(), 97.0)
    builder.road_stage(spain.a_coruna(), spain.lugo(), 97.0)
    builder.disable_split_stages()

    # Stage 2
    builder.road_stage(spain.lugo(), spain.gijon(), 240.0)

    # Stage 3
    builder.road_stage(spain.gijon(), spain.santander(), 208.0)

    # Stage 4
    builder.road_stage(spain.santander(), spain.reinosa(), 196.0)

    # Stage 5
    builder.road_stage(spain.reinosa(), spain.logrono(), 230.0)

    # Stage 6
    builder.road_stage(spain.logrono(), spain.zaragoza(), 190.0)

    # Stage 7
    builder.road_stage(spain.zaragoza(), spain.sabinanigo(), 146.0)

    # Stage 8
    builder.road_stage(spain.zaragoza(), spain.lleida(), 216.0)

    # Stage 9
    builder.road_stage(spain.artesa_de_segre(), spain.puigcerda(), 182.0)

    # Stage 10
    builder.road_stage(spain.puigcerda(), spain.sant_quirze_del_valles(), 181.0)

    # Stage 11
    builder.road_stage(spain.sant_quirze_del_valles(), spain.barcelona(), 143.0)

    # Stage 12
    builder.road_stage(spain.salou(), spain.nules(), 200.0)

    # Stage 13
    builder.road_stage(spain.nules(), spain.antella(), 195.0)

    # Stage 14
    builder.road_stage(spain.antella(), spain.albacete(), 153.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(spain.albacete(), spain.tomelloso(), 119.0)
    builder.individual_time_trial(spain.tomelloso(), spain.campo_de_criptana(), 35.0)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.campo_de_criptana(), spain.san_fernando_de_henares(), 176.0)

    # Stage 17
    builder.mountain_stage(spain.san_fernando_de_henares())
    builder.summit_finish(mountains.sierra_de_guadarrama.puerto_de_navacerrada(), ColCategory.C1, 178)

    # Stage 18
    builder.criterium(spain.palazuelos_de_eresma_destilerias_dyc(), 184.0)

    # Stage 19
    builder.criterium(spain.madrid(), 84.0)

    return builder.build()

def vuelta1983():

    builder = TourOfSpainBuilder(1983,4,19)

    # Prologue
    builder.out_and_back_prologue(spain.almussafes(), 6.8)

    # Stage 1
    builder.road_stage(spain.almussafes(), spain.cuenca(), 235.0)

    # Stage 2
    builder.road_stage(spain.cuenca(), spain.teruel(), 152.0)

    # Stage 3
    builder.road_stage(spain.teruel(), spain.sant_carles_de_la_rapita(), 241.0)

    # Stage 4
    builder.road_stage(spain.sant_carles_de_la_rapita(), spain.sant_quirze_del_valles(), 192.0)

    # Stage 5
    builder.road_stage(spain.sant_quirze_del_valles(), spain.castellar_de_n_hug(), 195.0)

    # Stage 6
    builder.road_stage(spain.la_pobla_de_lillet(), spain.viella(), 235.0)

    # Stage 7
    builder.road_stage(spain.les(), spain.sabinanigo(), 137.0)

    # Stage 8
    builder.individual_time_trial(spain.sabinanigo(), spain.balneario_de_panticosa(), 38.0)

    # Stage 9
    builder.road_stage(spain.panticosa(), spain.alfajarin(), 183.0)

    # Stage 10
    builder.road_stage(spain.zaragoza(), spain.soria(), 174.0)

    # Stage 11
    builder.road_stage(spain.soria(), spain.logrono(), 185.0)

    # Stage 12
    builder.road_stage(spain.logrono(), spain.burgos(), 147.0)

    # Stage 13
    builder.mountain_stage(spain.aguilar_de_campoo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 188.0)

    # Stage 14
    builder.road_stage(spain.cangas_de_onis(), spain.leon(), 195.0)

    # Stages 15a & 15b
    builder.enable_split_stages()
    builder.road_stage(spain.leon(), spain.valladolid(), 134.0)
    builder.out_and_back_individual_time_trial(spain.valladolid(), 22.0)
    builder.disable_split_stages()

    # Stage 16
    builder.road_stage(spain.valladolid(), spain.salamanca(), 162.0)

    # Stage 17
    builder.road_stage(spain.salamanca(), spain.avila(), 216.0)

    # Stage 18
    builder.road_stage(spain.avila(), spain.palazuelos_de_eresma_destilerias_dyc(), 204.0)

    # Stage 19
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.madrid(), 135.0)

    return builder.build()

def vuelta1984():

    builder = TourOfSpainBuilder(1984,4,17)

    # Prologue
    builder.out_and_back_prologue(spain.jerez_de_la_frontera(), 6.6)

    # Stage 1
    builder.road_stage(spain.jerez_de_la_frontera(), spain.malaga(), 272.0)

    # Stage 2
    builder.road_stage(spain.malaga(), spain.almeria(), 202.0)

    # Stage 3
    builder.road_stage(spain.mojacar(), spain.elche(), 204.0)

    # Stage 4
    builder.road_stage(spain.elche(), spain.valencia(), 197.0)

    # Stage 5
    builder.road_stage(spain.valencia(), spain.salou(), 245.0)

    # Stage 6
    builder.road_stage(spain.salou(), spain.sant_quirze_del_valles(), 113.0)

    # Stage 7
    builder.road_stage(spain.sant_quirze_del_valles(), spain.rasos_de_peguera(), 184.0)

    # Stage 8
    builder.road_stage(spain.cardona(), spain.zaragoza(), 269.0)

    # Stage 9
    builder.road_stage(spain.zaragoza(), spain.soria(), 159.0)

    # Stage 10
    builder.road_stage(spain.soria(), spain.burgos(), 148.0)

    # Stage 11
    builder.road_stage(spain.burgos(), spain.santander(), 182.0)

    # Stage 12
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 199.0)

    # Stage 13
    builder.road_stage(spain.cangas_de_onis(), spain.oviedo(), 170.0)

    # Stage 14
    builder.individual_time_trial(spain.lugones(), spain.monte_naranco(), 12.0)

    # Stage 15
    builder.road_stage(spain.oviedo(), spain.leon(), 121.0)

    # Stage 16
    builder.road_stage(spain.leon(), spain.valladolid(), 138.0)

    # Stage 17
    builder.road_stage(spain.valladolid(), spain.segovia(), 258.0)

    # Stages 18a & 18b
    builder.enable_split_stages()
    builder.road_stage(spain.segovia(), spain.torrejon_de_ardoz(), 145.0)
    builder.out_and_back_individual_time_trial(spain.torrejon_de_ardoz(), 33.0)
    builder.disable_split_stages()

    # Stage 19
    builder.road_stage(spain.torrejon_de_ardoz(), spain.madrid(), 139.0)

    return builder.build()

def vuelta1985():

    builder = TourOfSpainBuilder(1985,4,23)

    # Prologue
    builder.out_and_back_prologue(spain.valladolid(), 5.6)

    # Stage 1
    builder.road_stage(spain.valladolid(), spain.zamora(), 177.0)

    # Stage 2
    builder.road_stage(spain.zamora(), spain.ourense(), 262.0)

    # Stage 3
    builder.road_stage(spain.ourense(), spain.santiago_de_compostela(), 197.0)

    # Stage 4
    builder.road_stage(spain.santiago_de_compostela(), spain.lugo(), 162.0)

    # Stage 5
    builder.road_stage(spain.lugo(), spain.oviedo(), 238.0)

    # Stage 6
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 145.0)

    # Stage 7
    builder.mountain_stage(spain.cangas_de_onis())
    builder.summit_finish(mountains.cantabria.alto_campoo(), ColCategory.HC, 190)

    # Stage 8
    builder.road_stage(spain.aguilar_de_campoo(), spain.logrono(), 224.0)

    # Stage 9
    builder.road_stage(spain.logrono(), spain.balneario_de_panticosa(), 253.0)

    # Stage 10
    builder.road_stage(spain.sabinanigo(), spain.tremp(), 209.0)

    # Stage 11
    builder.road_stage(spain.tremp(), andorra.andorra_la_vella(), 124.0)

    # Stage 12
    builder.individual_time_trial(andorra.andorra_la_vella(), andorra.pal(), 16.0)

    # Stage 13
    builder.road_stage(andorra.andorra_la_vella(), spain.sant_quirze_del_valles(), 193.0)

    # Stage 14
    builder.road_stage(spain.valencia(), spain.benidorm(), 201.0)

    # Stage 15
    builder.road_stage(spain.benidorm(), spain.albacete(), 208.0)

    # Stage 16
    builder.road_stage(spain.albacete(), spain.alcala_de_henares(), 252.0)

    # Stage 17
    builder.out_and_back_individual_time_trial(spain.alcala_de_henares(), 43.0)

    # Stage 18
    builder.road_stage(spain.alcala_de_henares(), spain.palazuelos_de_eresma_destilerias_dyc(), 200.0)

    # Stage 19
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.salamanca(), 175.0)

    return builder.build()

def vuelta1986():

    builder = TourOfSpainBuilder(1986,4,22)

    # Prologue
    builder.out_and_back_prologue(spain.palma_de_mallorca(), 5.7)

    # Stage 1
    builder.criterium(spain.palma_de_mallorca(), 190.0)

    # Stage 2
    builder.criterium(spain.barcelona(), 182.0)

    # Stage 3
    builder.road_stage(spain.lleida(), spain.zaragoza(), 212.0)

    # Stage 4
    builder.road_stage(spain.zaragoza(), spain.logrono(), 192.0)

    # Stage 5
    builder.road_stage(spain.haro(), spain.santander(), 202.0)

    # Stage 6
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 191.0)

    # Stage 7
    builder.road_stage(spain.cangas_de_onis(), spain.oviedo(), 180.0)

    # Stage 8
    builder.mountain_time_trial(spain.oviedo())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 9.7)

    # Stage 9
    builder.road_stage(spain.oviedo(), spain.san_isidro(), 180.0)

    # Stage 10
    builder.road_stage(spain.san_isidro(), spain.palencia(), 193.0)

    # Stage 11
    builder.out_and_back_individual_time_trial(spain.valladolid(), 29.1)

    # Stage 12
    builder.road_stage(spain.valladolid(), spain.segovia(), 258.0)

    # Stage 13
    builder.road_stage(spain.segovia(), spain.villalba(), 148.0)

    # Stage 14
    builder.road_stage(spain.casino_gran_madrid(), spain.leganes(), 165.0)

    # Stage 15
    builder.road_stage(spain.aranjuez(), spain.albacete(), 207.0)

    # Stage 16
    builder.road_stage(spain.albacete(), spain.jaen(), 264.0)

    # Stage 17
    builder.mountain_stage(spain.jaen())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 172)

    # Stage 18
    builder.road_stage(spain.granada(), spain.benalmadena(), 191.0)

    # Stage 19
    builder.road_stage(spain.benalmadena(), spain.puerto_real(), 234.0)

    # Stage 20
    builder.road_stage(spain.puerto_real(), spain.jerez_de_la_frontera(), 239.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.jerez_de_la_frontera(), 22.0)

    return builder.build()

def vuelta1987():

    builder = TourOfSpainBuilder(1987,4,23)

    # Prologue
    builder.out_and_back_prologue(spain.benidorm(), 6.6)

    # Stage 1
    builder.road_stage(spain.benidorm(), spain.albacete(), 219.0)

    # Stage 2
    builder.road_stage(spain.albacete(), spain.valencia(), 217.0)

    # Stage 3
    builder.out_and_back_individual_time_trial(spain.valencia(), 34.8)

    # Stage 4
    builder.road_stage(spain.valencia(), spain.villareal(), 169.0)

    # Stage 5
    builder.road_stage(spain.salou(), spain.barcelona(), 165.0)

    # Stage 6
    builder.mountain_stage(spain.barcelona())
    builder.summit_finish(mountains.pyrenees.grau_roig(), ColCategory.C1, 220.0)

    # Stage 7
    builder.mountain_stage(spain.la_seu_d_urgell())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 186.0)

    # Stage 8
    builder.road_stage(spain.benasque(), spain.zaragoza(), 219.0)

    # Stage 9
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 180.0)

    # Stage 10
    builder.mountain_stage(spain.miranda_de_ebro())
    builder.summit_finish(mountains.cantabria.alto_campoo(), ColCategory.HC, 213)

    # Stage 11
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 179.0)

    # Stage 12
    builder.road_stage(spain.cangas_de_onis(), spain.oviedo(), 142.0)

    # Stage 13
    builder.road_stage(spain.luarca(), spain.ferrol(), 223.0)

    # Stage 14
    builder.road_stage(spain.ferrol(), spain.a_coruna(), 220.0)

    # Stage 15
    builder.road_stage(spain.a_coruna(), spain.vigo(), 185.0)

    # Stage 16
    builder.road_stage(spain.ponteareas(), spain.ponferrada(), 237.0)

    # Stage 17
    builder.road_stage(spain.ponferrada(), spain.valladolid(), 221.0)

    # Stage 18
    builder.out_and_back_individual_time_trial(spain.valladolid(), 24.0)

    # Stage 19
    builder.road_stage(spain.el_barco_de_avila(), spain.avila(), 213.0)

    # Stage 20
    builder.road_stage(spain.avila(), spain.palazuelos_de_eresma_destilerias_dyc(), 183.0)

    # Stage 21
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.collado_villalba(), 160.0)

    # Stage 22
    builder.road_stage(spain.alcala_de_henares(), spain.madrid(), 173.0)

    return builder.build()

def vuelta1988():

    builder = TourOfSpainBuilder(1988,4,25)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.santa_cruz_de_tenerife(), 17.4)

    # Stage 2
    builder.road_stage(spain.san_cristobal_de_la_laguna(), spain.santa_cruz_de_tenerife(), 210.0)

    # Stage 3
    builder.out_and_back_team_time_trial(spain.las_palmas(), 34.0)

    # Stage 4
    builder.road_stage(spain.alcala_del_rio(), spain.badajoz(), 210.0)

    # Stage 5
    builder.road_stage(spain.badajoz(), spain.bejar(), 234.0)

    # Stage 6
    builder.road_stage(spain.bejar(), spain.valladolid(), 202.0)

    # Stage 7
    builder.road_stage(spain.valladolid(), spain.leon(), 160.0)

    # Stage 8
    builder.road_stage(spain.leon(), spain.branillin(), 176.7)

    # Stage 9
    builder.individual_time_trial(spain.oviedo(), spain.monte_naranco(), 6.8)

    # Stage 10
    builder.road_stage(spain.oviedo(), spain.santander(), 197.3)

    # Stage 11
    builder.road_stage(spain.santander(), spain.valdezcaray(), 217.2)

    # Stage 12
    builder.road_stage(spain.logrono(), spain.jaca(), 197.5)

    # Stage 13
    builder.mountain_stage(spain.jaca())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 178.2)

    # Stage 14
    builder.road_stage(spain.benasque(), andorra.andorra_la_vella(), 190.3)

    # Stage 15
    builder.road_stage(spain.la_seu_d_urgell(), spain.sant_quirze_del_valles(), 166.0)

    # Stage 16
    builder.road_stage(spain.valencia(), spain.albacete(), 192.0)

    # Stage 17
    builder.road_stage(spain.albacete(), spain.toledo(), 244.4)

    # Stage 18
    builder.road_stage(spain.toledo(), spain.avila(), 212.5)

    # Stage 19
    builder.road_stage(spain.avila(), spain.segovia(), 150.0)

    # Stage 20
    builder.individual_time_trial(spain.las_rozas(), spain.villalba(), 30.0)

    # Stage 21
    builder.road_stage(spain.villalba(), spain.madrid(), 202.0)

    return builder.build()

def vuelta1989():

    builder = TourOfSpainBuilder(1989,4,24)

    # Stage 1
    builder.criterium(spain.a_coruna(), 21.0)

    # Stage 2
    builder.road_stage(spain.a_coruna(), spain.santiago_de_compostela(), 222.0)

    # Stages 3a & 3b
    builder.enable_split_stages()
    builder.out_and_back_team_time_trial(spain.vigo(), 35.0)
    builder.road_stage(spain.vigo(), spain.ourense(), 105.0)
    builder.disable_split_stages()

    # Stage 4
    builder.road_stage(spain.ourense(), spain.pontevedra(), 163.0)

    # Stage 5
    builder.road_stage(spain.la_baneza(), spain.bejar(), 260.0)

    # Stage 6
    builder.road_stage(spain.bejar(), spain.avila(), 195.0)

    # Stage 7
    builder.road_stage(spain.avila(), spain.toledo(), 165.0)

    # Stage 8
    builder.road_stage(spain.toledo(), spain.albacete(), 226.0)

    # Stage 9
    builder.road_stage(spain.albacete(), spain.gandia(), 194.0)

    # Stage 10
    builder.road_stage(spain.gandia(), spain.benicassim(), 219.0)

    # Stage 11
    builder.road_stage(spain.vinaros(), spain.lleida(), 182.0)

    # Stage 12
    builder.mountain_stage(spain.lleida())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 190.0)

    # Stage 13
    builder.road_stage(spain.benasque(), spain.jaca(), 190.0)

    # Stage 14
    builder.road_stage(spain.jaca(), spain.zaragoza(), 166.0)

    # Stage 15
    builder.individual_time_trial(spain.ezcaray(), spain.valdezcaray(), 23.0)

    # Stage 16
    builder.road_stage(spain.haro(), spain.santona(), 193.0)

    # Stage 17
    builder.road_stage(spain.santona(), spain.lagos_de_enol(), 225.0)

    # Stage 18
    builder.road_stage(spain.cangas_de_onis(), spain.branillin(), 152.0)

    # Stage 19
    builder.road_stage(spain.leon(), spain.valladolid(), 157.0)

    # Stage 20
    builder.individual_time_trial(spain.valladolid(), spain.medina_del_campo(), 42.0)

    # Stage 21
    builder.road_stage(spain.collado_villalba(), spain.palazuelos_de_eresma_destilerias_dyc(), 187.0)

    # Stage 22
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.madrid(), 179.0)

    return builder.build()

def vuelta1990():

    builder = TourOfSpainBuilder(1990,4,24)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.benicassim(), 10.3)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(spain.oropesa(), spain.castellon(), 108.0)
    builder.team_time_trial(spain.benicassim(), spain.borriana(), 36.3)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(spain.denia(), spain.murcia(), 196.3)

    # Stage 4
    builder.road_stage(spain.murcia(), spain.almeria(), 226.2)

    # Stage 5
    builder.mountain_stage(spain.almeria())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 198)

    # Stage 6
    builder.road_stage(spain.loja(), spain.ubrique(), 195.2)

    # Stage 7
    builder.road_stage(spain.jerez(), spain.seville(), 190.3)

    # Stage 8
    builder.road_stage(spain.seville(), spain.merida(), 187.6)

    # Stage 9
    builder.road_stage(spain.caceres(), spain.guijuelo(), 192.7)

    # Stage 10
    builder.road_stage(spain.penaranda_de_bracamonte(), spain.leon(), 226.8)

    # Stage 11
    builder.road_stage(spain.leon(), spain.san_isidro(), 203.0)

    # Stage 12
    builder.road_stage(spain.san_isidro(), spain.naranco(), 156.0)

    # Stage 13
    builder.road_stage(spain.oviedo(), spain.santander(), 193.3)

    # Stage 14
    builder.road_stage(spain.santander(), spain.najera(), 207.5)

    # Stage 15
    builder.individual_time_trial(spain.ezcaray(), spain.valdezcaray(), 24.1)

    # Stage 16
    builder.road_stage(spain.logrono(), spain.pamplona(), 165.5)

    # Stage 17
    builder.road_stage(spain.pamplona(), spain.jaca(), 155.3)

    # Stage 18
    builder.mountain_stage(spain.jaca())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 178.5)

    # Stage 19
    builder.road_stage(spain.benasque(), spain.zaragoza(), 223.6)

    # Stage 20
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 40.0)

    # Stage 21
    builder.road_stage(spain.collado_villalba(), spain.palazuelos_de_eresma(), 188.6)

    # Stage 22
    builder.road_stage(spain.segovia(), spain.madrid(), 177.0)

    return builder.build()

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
    builder.road_stage(spain.seville(), spain.jaen(), 292.0)

    # Stage 5
    builder.road_stage(spain.linares(), spain.albacete(), 227.8)

    # Stage 6
    builder.road_stage(spain.albacete(), spain.valencia(), 236.5)

    # Stage 7
    builder.criterium(spain.palma_de_mallorca(), 188.0)

    # Stage 8
    builder.out_and_back_individual_time_trial(spain.cala_d_or(), 47.0)

    # Stage 9
    builder.road_stage(spain.sant_cugat_del_valles(), spain.lloret_de_mar(), 140.0)

    # Stage 10
    builder.road_stage(spain.lloret_de_mar(), andorra.andorra_la_vella(), 229.0)

    # Stage 11
    builder.road_stage(andorra.andorra_la_vella(), spain.pla_de_beret(), 0.0)

    # Stage 12
    builder.mountain_stage(spain.bossost())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 111.0)

    # Stage 13
    builder.road_stage(spain.benasque(), spain.zaragoza(), 219.0)

    # Stage 14
    builder.individual_time_trial(spain.ezcaray(), spain.valdezcaray(), 24.1)

    # Stage 15
    builder.road_stage(spain.santo_domingo_de_la_calzada(), spain.santander(), 219.5)

    # Stage 16
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 186.6)

    # Stage 17
    builder.mountain_stage(spain.cangas_de_onis())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 152.0)

    # Stage 18
    builder.road_stage(spain.leon(), spain.valladolid(), 137.5)

    # Stage 19
    builder.out_and_back_individual_time_trial(spain.valladolid(), 53.2)

    # Stage 20
    builder.criterium(spain.palazuelos_de_eresma_destilerias_dyc(), 212.7)

    # Stage 21
    builder.road_stage(spain.collado_villalba(), spain.madrid(), 169.6)

    return builder.build()

def vuelta1992():

    builder = TourOfSpainBuilder(1992,4,27)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.jerez_de_la_frontera(), 9.2)

    # Stages 2a & 2b
    builder.enable_split_stages()
    builder.road_stage(spain.san_fernando(), spain.jerez_de_la_frontera(), 135.5)
    builder.team_time_trial(spain.arcos_de_la_frontera(), spain.jerez_de_la_frontera(), 32.6)
    builder.disable_split_stages()

    # Stage 3
    builder.road_stage(spain.jerez_de_la_frontera(), spain.cordoba(), 205.0)

    # Stage 4
    builder.road_stage(spain.linares(), spain.albacete(), 229.0)

    # Stage 5
    builder.road_stage(spain.albacete(), spain.gandia(), 213.5)

    # Stage 6
    builder.road_stage(spain.gandia(), spain.benicassim(), 202.8)

    # Stage 7
    builder.individual_time_trial(spain.alquerias_del_nino_perdido(), spain.oropesa(), 49.5)

    # Stage 8
    builder.road_stage(spain.lleida(), spain.pla_de_beret(), 240.5)

    # Stage 9
    builder.mountain_stage(spain.vielha())
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.C1, 144.0)

    # Stage 10
    builder.road_stage(france.luz_saint_sauveur(), spain.sabinanigo(), 196.0)

    # Stage 11
    builder.road_stage(spain.sabinanigo(), spain.pamplona(), 162.9)

    # Stage 12
    builder.road_stage(spain.pamplona(), spain.burgos(), 200.1)

    # Stage 13
    builder.road_stage(spain.burgos(), spain.santander(), 178.3)

    # Stage 14
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 213.4)

    # Stage 15
    builder.mountain_stage(spain.cangas_de_onis())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 163)

    # Stage 16
    builder.road_stage(spain.oviedo(), spain.leon(), 162.0)

    # Stage 17
    builder.road_stage(spain.leon(), spain.salamanca(), 200.6)

    # Stage 18
    builder.road_stage(spain.salamanca(), spain.avila(), 218.9)

    # Stage 19
    builder.out_and_back_individual_time_trial(spain.fuenlabrada(), 37.9)

    # Stage 20
    builder.road_stage(spain.collado_villalba(), spain.palazuelos_de_eresma_destilerias_dyc(), 188.3)

    # Stage 21
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.madrid(), 175.0)

    return builder.build()

def vuelta1993():

    builder = TourOfSpainBuilder(1993,4,26)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.a_coruna(), 10.0)

    # Stage 2
    builder.road_stage(spain.a_coruna(), spain.vigo(), 251.1)

    # Stage 3
    builder.road_stage(spain.vigo(), spain.ourense(), 171.4)

    # Stage 4
    builder.road_stage(spain.a_gudina(), spain.salamanca(), 233.4)

    # Stage 5
    builder.road_stage(spain.salamanca(), spain.avila(), 219.8)

    # Stage 6
    builder.mountain_time_trial(spain.palazuelos_de_eresma_destilerias_dyc())
    builder.summit_finish(mountains.sierra_de_guadarrama.puerto_de_navacerrada(), ColCategory.C1, 24.1)

    # Stage 7
    builder.road_stage(spain.palazuelos_de_eresma_destilerias_dyc(), spain.madrid(), 184.0)

    # Stage 8
    builder.road_stage(spain.aranjuez(), spain.albacete(), 225.1)

    # Stage 9
    builder.road_stage(spain.albacete(), spain.valencia(), 224.0)

    # Stage 10
    builder.road_stage(spain.valencia(), spain.la_senia(), 206.0)

    # Stage 11
    builder.mountain_stage(spain.lleida())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 221.0)

    # Stage 12
    builder.road_stage(spain.benasque(), spain.zaragoza(), 220.7)

    # Stage 13
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 37.1)

    # Stage 14
    builder.mountain_stage(spain.tudela())
    builder.summit_finish(mountains.la_rioja.alto_de_la_cruz_de_la_demanda("Ezcaray"), ColCategory.C1, 197.2)

    # Stage 15
    builder.road_stage(spain.santo_domingo_de_la_calzada(), spain.santander(), 226.2)

    # Stage 16
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.cantabria.alto_campoo(), ColCategory.HC, 160)

    # Stage 17
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 179.5)

    # Stage 18
    builder.road_stage(spain.cangas_de_onis(), spain.gijon(), 170.0)

    # Stage 19
    builder.mountain_stage(spain.gijon())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 153)

    # Stage 20
    builder.road_stage(spain.salas(), spain.ferol(), 247.0)

    # Stage 21
    builder.individual_time_trial(spain.padron(), spain.santiago_de_compostela(), 44.6)

    return builder.build()

def vuelta1994():

    builder = TourOfSpainBuilder(1994,4,25)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.valladolid(), 9.0)

    # Stage 2
    builder.road_stage(spain.valladolid(), spain.salamanca(), 178.4)

    # Stage 3
    builder.road_stage(spain.salamanca(), spain.caceres(), 239.0)

    # Stage 4
    builder.road_stage(spain.almendralejo(), spain.cordoba(), 235.6)

    # Stage 5
    builder.road_stage(spain.cordoba(), spain.granada(), 166.9)

    # Stage 6
    builder.mountain_stage(spain.granada())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 151.7)

    # Stage 7
    builder.road_stage(spain.baza(), spain.alicante(), 256.5)

    # Stage 8
    builder.out_and_back_individual_time_trial(spain.benidorm(), 39.5)

    # Stage 9
    builder.road_stage(spain.benidorm(), spain.valencia(), 166.0)

    # Stage 10
    builder.mountain_stage(spain.igualada())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 205.0)

    # Stage 11
    builder.mountain_stage(andorra.andorra_la_vella())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 195.3)

    # Stage 12
    builder.road_stage(spain.benasque(), spain.zaragoza(), 226.7)

    # Stage 13
    builder.road_stage(spain.zaragoza(), spain.pamplona(), 201.6)

    # Stage 14
    builder.road_stage(spain.pamplona(), spain.sierra_de_la_demanda(), 174.0)

    # Stage 15
    builder.road_stage(spain.santo_domingo_de_la_calzada(), spain.santander(), 209.3)

    # Stage 16
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 147.7)

    # Stage 17
    builder.road_stage(spain.cangas_de_onis(), spain.monte_naranco(), 150.4)

    # Stage 18
    builder.criterium(spain.avila(), 189.0)

    # Stage 19
    builder.road_stage(spain.avila(), spain.palazuelos_de_eresma(), 171.0)

    # Stage 20
    builder.individual_time_trial(spain.segovia(), spain.palazuelos_de_eresma(), 53.0)

    # Stage 21
    builder.road_stage(spain.palazuelos_de_eresma(), spain.madrid(), 165.7)

    return builder.build()

def vuelta1995():

    builder = TourOfSpainBuilder(1995,9,2)

    # Prologue
    builder.out_and_back_prologue(spain.zaragoza(), 7.0)

    # Stage 1
    builder.road_stage(spain.zaragoza(), spain.logrono(), 186.6)

    # Stage 2
    builder.road_stage(spain.san_asensio(), spain.santander(), 223.5)

    # Stage 3
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 206)

    # Stage 4
    builder.road_stage(spain.tapia_de_casariego(), spain.a_coruna(), 82.6)

    # Stage 5
    builder.road_stage(spain.a_coruna(), spain.ourense(), 179.8)

    # Stage 6
    builder.road_stage(spain.ourense(), spain.zamora(), 264.0)

    # Stage 7
    builder.out_and_back_individual_time_trial(spain.salamanca(), 41.0)

    # Stage 8
    builder.road_stage(spain.salamanca(), spain.avila(), 219.8)

    # Stage 9
    builder.road_stage(spain.avila(), spain.palazuelos_de_eresma(), 122.5)

    # Stage 10
    builder.road_stage(spain.cordoba(), spain.seville(), 208.5)

    # Stage 11
    builder.road_stage(spain.seville(), spain.marbella(), 162.5)

    # Stage 12
    builder.mountain_stage(spain.marbella())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 238.5)

    # Stage 13
    builder.road_stage(spain.olula_del_rio(), spain.murcia(), 181.0)

    # Stage 14
    builder.road_stage(spain.elche(), spain.valencia(), 207.0)

    # Stage 15
    builder.road_stage(spain.barcelona(), spain.estadi_olimpic_lluis_companys(), 154.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.tarrega(), spain.pla_de_beret(), 197.3)

    # Stage 17
    salardu_naut_aran = vicinity(spain.salardu(), "Naut Aran")
    builder.mountain_stage(salardu_naut_aran)
    builder.summit_finish(mountains.pyrenees.luz_ardiden(), ColCategory.C1, 179.2)

    # Stage 18
    builder.road_stage(france.luz_saint_sauveur(), spain.sabinanigo(), 157.8)

    # Stage 19
    builder.road_stage(spain.sabinanigo(), spain.calatayud(), 227.7)

    # Stage 20
    builder.out_and_back_individual_time_trial(spain.alcala_de_henares(), 41.6)

    # Stage 21
    builder.road_stage(spain.alcala_de_henares(), spain.madrid(), 147.5)

    return builder.build()

def vuelta1996():

    builder = TourOfSpainBuilder(1996,9,7)

    # Stage 1
    builder.criterium(spain.valencia(), 162.0)

    # Stage 2
    builder.road_stage(spain.valencia(), spain.cuenca(), 210.0)

    # Stage 3
    builder.road_stage(spain.cuenca(), spain.albacete(), 167.2)

    # Stage 4
    builder.road_stage(spain.albacete(), spain.murcia(), 166.5)

    # Stage 5
    builder.road_stage(spain.murcia(), spain.almeria(), 208.4)

    # Stage 6
    builder.road_stage(spain.almeria(), spain.malaga(), 196.5)

    # Stage 7
    builder.road_stage(spain.malaga(), spain.marbella(), 171.1)

    # Stage 8
    builder.road_stage(spain.marbella(), spain.jerez_de_la_frontera(), 220.7)

    # Stage 9
    builder.road_stage(spain.jerez_de_la_frontera(), spain.cordoba(), 203.5)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.individual_time_trial(spain.el_tiemblo(), spain.avila(), 46.5)

    # Stage 11
    builder.road_stage(spain.avila(), spain.salamanca(), 188.0)

    # Stage 12
    builder.mountain_stage(spain.benavente())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 188.0)

    # Stage 13
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 159.0)

    # Stage 14
    builder.road_stage(spain.cangas_de_onis(), spain.cabarceno_natural_park(), 202.6)

    # Stage 15
    builder.mountain_stage(spain.cabarceno())
    builder.summit_finish(mountains.la_rioja.alto_de_la_cruz_de_la_demanda("Ezcaray"), ColCategory.C1, 220.0)

    # Stage 16
    builder.road_stage(spain.logrono(), spain.sabinanigo(), 220.9)

    # Stage 17
    builder.mountain_stage(spain.sabinanigo())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 165.7)

    # Stage 18
    builder.road_stage(spain.benasque(), spain.zaragoza(), 219.5)

    # Stage 19
    builder.road_stage(spain.getafe(), spain.avila(), 217.1)

    # Stage 20
    builder.road_stage(spain.avila(), spain.palazuelos_de_eresma_destilerias_dyc(), 209.5)

    # Stage 21
    builder.individual_time_trial(spain.segovia(), spain.palazuelos_de_eresma_destilerias_dyc(), 43.0)

    # Stage 22
    builder.criterium(spain.madrid(), 157.6)

    return builder.build()

def vuelta1997():

    builder = TourOfSpainBuilder(1997,9,6)

    # Stage 1
    builder.road_stage(portugal.lisbon(), portugal.estoril(), 155.0)

    # Stage 2
    builder.road_stage(portugal.evora(), portugal.vilamoura(), 225.0)

    # Stage 3
    builder.road_stage(portugal.loule(), spain.huelva(), 173.0)

    # Stage 4
    builder.road_stage(spain.huelva(), spain.jerez_de_la_frontera(), 192.0)

    # Stage 5
    builder.road_stage(spain.jerez_de_la_frontera(), spain.malaga(), 230.0)

    # Stage 6
    builder.road_stage(spain.malaga(), spain.granada(), 147.0)

    # Stage 7
    builder.mountain_stage(spain.guadix())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 219)

    # Stage 8
    builder.road_stage(spain.granada(), spain.cordoba(), 176.0)

    # Stage 9
    builder.out_and_back_individual_time_trial(spain.cordoba(), 35.0)

    # Stage 10
    builder.road_stage(spain.cordoba(), spain.almendralejo(), 224.0)

    # Stage 11
    builder.road_stage(spain.almendralejo(), spain.plasencia(), 194.0)

    # Stage 12
    builder.mountain_stage(spain.leon())
    builder.summit_finish(mountains.asturias.alto_del_morredero(), ColCategory.C1, 147.0)

    # Stage 13
    builder.road_stage(spain.ponferrada(), spain.estacion_valgrande_pajares(), 196.0)

    # Stage 14
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 169)

    # Stage 15
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 160.0)

    # Stage 16
    builder.road_stage(spain.cangas_de_onis(), spain.santander(), 170.0)

    # Stage 17
    builder.road_stage(spain.santander(), spain.burgos(), 183.0)

    # Stage 18
    builder.road_stage(spain.burgos(), spain.valladolid(), 184.0)

    # Stage 19
    builder.road_stage(spain.valladolid(), spain.los_angeles_de_san_rafael(), 193.0)

    # Stage 20
    builder.road_stage(spain.los_angeles_de_san_rafael(), spain.avila(), 199.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.alcobendas(), 43.0)

    # Stage 22
    builder.criterium(spain.madrid(), 154.0)

    return builder.build()

def vuelta1998():

    builder = TourOfSpainBuilder(1998,9,5)

    # Stage 1
    builder.criterium(spain.cordoba(), 161.7)

    # Stage 2
    builder.road_stage(spain.cordoba(), spain.cadiz(), 234.6)

    # Stage 3
    builder.road_stage(spain.cadiz(), spain.estepona(), 192.6)

    # Stage 4
    builder.road_stage(spain.malaga(), spain.granada(), 173.5)

    # Stage 5
    builder.road_stage(spain.olula_del_rio(), spain.murcia(), 165.5)

    # Stage 6
    builder.road_stage(spain.murcia(), spain.xorret_de_cati(), 201.5)

    # Stage 7
    builder.road_stage(spain.alicante(), spain.valencia(), 185.0)

    # Stage 8
    builder.criterium(spain.palma_de_mallorca(), 181.5)

    # Stage 9
    builder.out_and_back_individual_time_trial(spain.alcudia(), 39.5)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(spain.vic(), andorra.estacio_de_pal(), 199.3)

    # Stage 11
    builder.mountain_stage(andorra.andorra_la_vella())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 186.0)

    # Stage 12
    jaca = vicinity(spain.jaca(), "Canfranc International Station")
    builder.road_stage(spain.benasque(), jaca, 187)

    # Stage 13
    builder.criterium(spain.sabinanigo(), 208.5)

    # Stage 14
    builder.road_stage(spain.biescas(), spain.zaragoza(), 145.5)

    # Stage 15
    builder.road_stage(spain.zaragoza(), spain.soria(), 178.7)

    # Stage 16
    builder.road_stage(spain.soria(), spain.laguna_negra_de_neila(), 143.7)

    # Stage 17
    builder.road_stage(spain.burgos(), spain.leon(), 188.5)

    # Stage 18
    builder.road_stage(spain.leon(), spain.salamanca(), 223.0)

    # Stage 19
    builder.road_stage(spain.avila(), spain.segovia(), 170.4)

    # Stage 20
    builder.mountain_stage(spain.segovia())
    builder.summit_finish(mountains.sierra_de_guadarrama.puerto_de_navacerrada(), ColCategory.C1, 206.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.fuenlabrada(), 39.0)

    # Stage 22
    builder.criterium(spain.madrid(), 163.0)

    return builder.build()

def vuelta1999():

    builder = TourOfSpainBuilder(1999,9,4)

    # Prologue
    builder.out_and_back_prologue(spain.murcia(), 6.1)

    # Stage 1
    builder.road_stage(spain.murcia(), spain.benidorm(), 179.0)

    # Stage 2
    builder.road_stage(spain.alicante(), spain.albacete(), 206.0)

    # Stage 3
    builder.road_stage(spain.la_roda(), spain.fuenlabrada(), 229.5)

    # Stage 4
    builder.road_stage(spain.la_rozas(), spain.salamanca(), 185.6)

    # Stage 5
    builder.road_stage(spain.bejar(), spain.ciudad_rodrigo(), 160.0)

    # Stage 6
    builder.out_and_back_individual_time_trial(spain.salamanca(), 46.4)

    # Stage 7
    builder.road_stage(spain.salamanca(), spain.leon(), 217.0)

    # Stage 8
    builder.mountain_stage(spain.leon())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 175.6)

    # Stage 9
    builder.road_stage(spain.gijon(), spain.los_corrales_de_buelna(), 185.8)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.criterium(spain.zaragoza(), 183.2)

    # Stage 11
    builder.mountain_stage(spain.huesca())
    builder.summit_finish(mountains.pyrenees.val_d_aran_pla_de_beret(), ColCategory.C1, 201.0)

    # Stage 12
    builder.mountain_stage(spain.sort())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 147.4)

    # Stage 13
    castellar_del_riu = vicinity(spain.castellar_del_riu(), "Rasos de Peguera")
    builder.road_stage(andorra.andorra_la_vella(), castellar_del_riu, 149)

    # Stage 14
    builder.criterium(spain.barcelona(), 94.4)

    # Stage 15
    builder.road_stage(spain.la_senia(), spain.valencia(), 193.4)

    # Stage 16
    builder.road_stage(spain.valencia(), spain.teruel(), 200.4)

    # Stage 17
    builder.road_stage(spain.bronchales(), spain.guadalajara(), 225.0)

    # Stage 18
    builder.mountain_stage(spain.guadalajara())
    builder.summit_finish(mountains.sierra_de_guadarrama.alto_de_abantos(), ColCategory.C1, 166.3)

    # Stage 19
    builder.road_stage(spain.san_lorenzo_de_el_escorial(), spain.avila(), 184.6)

    # Stage 20
    builder.individual_time_trial(spain.el_tiemblo(), spain.avila(), 46.5)

    # Stage 21
    builder.criterium(spain.madrid(), 163.0)

    return builder.build()

def vuelta2000():

    builder = TourOfSpainBuilder(2000,8,26)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.malaga(), 13.3)

    # Stage 2
    builder.road_stage(spain.malaga(), spain.cordoba(), 167.5)

    # Stage 3
    builder.road_stage(spain.montoro(), spain.valdepenas(), 198.4)

    # Stage 4
    builder.road_stage(spain.valdepenas(), spain.albacete(), 159.0)

    # Stage 5
    builder.road_stage(spain.albacete(), spain.xorret_de_cati(), 152.3)

    # Stage 6
    builder.road_stage(spain.benidorm(), spain.valencia(), 155.5)

    # Stage 7
    builder.road_stage(spain.valencia(), spain.morella(), 175.0)

    # Stage 8
    builder.road_stage(spain.vinaros(), spain.port_aventura(), 168.5)

    # Stage 9
    builder.out_and_back_individual_time_trial(spain.tarragona(), 37.6)

    # Stage 10
    builder.road_stage(spain.sabadell(), spain.supermolina(), 165.8)

    # Stage 11
    builder.mountain_stage(spain.alp())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 136.5)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.criterium(spain.zaragoza(), 131.5)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.criterium(spain.santander(), 143.3)

    # Stage 14
    builder.mountain_stage(spain.santander())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 146.5)

    # Stage 15
    builder.road_stage(spain.cangas_de_onis(), spain.gijon(), 164.2)

    # Stage 16
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 168.0)

    # Stage 17
    builder.road_stage(spain.benavente(), spain.salamanca(), 155.5)

    # Stage 18
    builder.road_stage(spain.bejar(), spain.ciudad_rodrigo(), 159.0)

    # Stage 19
    builder.road_stage(spain.salamanca(), spain.avila(), 130.0)

    # Stage 20
    builder.mountain_stage(spain.avila())
    builder.summit_finish(mountains.sierra_de_guadarrama.alto_de_abantos(), ColCategory.C1, 128.2)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.madrid(), 38.0)

    return builder.build()

def vuelta2001():

    builder = TourOfSpainBuilder(2001,9,8)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.salamanca(), 12.0)

    # Stage 2
    builder.road_stage(spain.salamanca(), spain.valladolid(), 147.2)

    # Stage 3
    builder.road_stage(spain.valladolid(), spain.leon(), 140.5)

    # Stage 4
    builder.road_stage(spain.leon(), spain.gijon(), 175.0)

    # Stage 5
    builder.mountain_stage(spain.gijon())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 160.8)

    # Stage 6
    builder.road_stage(spain.cangas_de_onis(), spain.torrelavega(), 180.6)

    # Stage 7
    builder.out_and_back_individual_time_trial(spain.torrelavega(), 44.2)

    # Stage 8
    builder.mountain_stage(spain.reinosa())
    builder.summit_finish(mountains.la_rioja.alto_de_la_cruz_de_la_demanda("Valdezcaray"), ColCategory.C1, 195.0)

    # Stage 9
    builder.road_stage(spain.logrono(), spain.barcelona(), 179.2)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(spain.sabadell(), spain.la_molina(), 168.4)

    # Stage 11
    builder.road_stage(spain.alp(), andorra.estacio_de_pal(), 154.2)

    # Stage 12
    builder.individual_time_trial(andorra.ordino(), andorra.estacio_d_esqui_d_ordino_alcalis(), 17.1)

    # Stage 13
    builder.road_stage(andorra.andorra_la_vella(), spain.universal_studios_port_aventura(), 206.0)

    # Stage 14
    builder.road_stage(spain.tarragona(), spain.vinaros(), 170.5)

    # Stage 15
    builder.mountain_stage(spain.valencia())
    builder.summit_finish(mountains.prebaetic.alto_de_aitana(), ColCategory.HC, 207.2)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.alcoy(), spain.murcia(), 153.3)

    # Stage 17
    builder.road_stage(spain.murcia(), spain.albacete(), 159.5)

    # Stage 18
    builder.road_stage(spain.albacete(), spain.cuenca(), 154.2)

    # Stage 19
    builder.road_stage(spain.cuenca(), spain.guadalajara(), 168.0)

    # Stage 20
    builder.mountain_stage(spain.guadalajara())
    builder.summit_finish(mountains.sierra_de_guadarrama.alto_de_abantos(), ColCategory.C1, 176.3)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.madrid(), 38.0)

    return builder.build()

def vuelta2002():

    builder = TourOfSpainBuilder(2002,9,7)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.valencia(), 24.6)

    # Stage 2
    builder.road_stage(spain.valencia(), spain.alcoy(), 144.7)

    # Stage 3
    builder.road_stage(spain.san_vicente_del_raspeig(), spain.murcia(), 134.2)

    # Stage 4
    builder.road_stage(spain.aguilas(), spain.roquetas_de_mar(), 149.5)

    # Stage 5
    builder.mountain_stage(spain.el_ejido())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 198)

    # Stage 6
    builder.mountain_stage(spain.granada())
    builder.summit_finish(mountains.sierra_sur_de_jaen.sierra_de_la_pandera(), ColCategory.C1, 153.1)

    # Stage 7
    builder.road_stage(spain.jaen(), spain.malaga(), 196.8)

    # Stage 8
    builder.road_stage(spain.malaga(), spain.ubrique(), 173.6)

    # Stage 9
    builder.criterium(spain.cordoba(), 130.2)

    # Stage 10
    builder.out_and_back_individual_time_trial(spain.cordoba(), 36.5)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.alcobendas(), spain.collado_villalba(), 166.1)

    # Stage 12
    builder.road_stage(spain.segovia(), spain.burgos(), 210.5)

    # Stage 13
    builder.road_stage(spain.burgos(), spain.santander(), 189.8)

    # Stage 14
    builder.road_stage(spain.santander(), spain.gijon(), 190.2)

    # Stage 15
    builder.mountain_stage(spain.gijon())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 176.7)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.aviles(), spain.leon(), 154.7)

    # Stage 17
    builder.road_stage(spain.benavente(), spain.salamanca(), 146.6)

    # Stage 18
    builder.mountain_stage(spain.salamanca())
    builder.summit_finish(mountains.sistema_central.la_covatilla(), ColCategory.HC, 193.7)

    # Stage 19
    builder.road_stage(spain.bejar(), spain.avila(), 177.8)

    # Stage 20
    builder.road_stage(spain.avila(), spain.parque_warner_madrid(), 141.2)

    # Stage 21
    builder.individual_time_trial(spain.parque_warner_madrid(), spain.santiago_bernabeu_stadium_madrid(), 41.2)

    return builder.build()

def vuelta2003():

    builder = TourOfSpainBuilder(2003,9,6)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.gijon(), 28.0)

    # Stage 2
    builder.road_stage(spain.gijon(), spain.cangas_de_onis(), 148.0)

    # Stage 3
    builder.road_stage(spain.cangas_de_onis(), spain.santander(), 154.3)

    # Stage 4
    builder.road_stage(spain.santander(), spain.burgos(), 151.0)

    # Stage 5
    builder.road_stage(spain.soria(), spain.zaragoza(), 166.7)

    # Stage 6
    builder.out_and_back_individual_time_trial(spain.zaragoza(), 43.8)

    # Stage 7
    builder.mountain_stage(spain.huesca())
    builder.summit_finish(mountains.pyrenees.cauterets(), ColCategory.C1, 190.0)

    # Stage 8
    builder.road_stage(mountains.pyrenees.cauterets(), spain.pla_de_beret_val_d_aran(), 166.0)

    # Stage 9
    builder.road_stage(spain.vielha(), andorra.envalira(), 174.8)

    # Stage 10
    builder.road_stage(andorra.andorra_la_vella(), spain.sabadell(), 194.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.utiel(), spain.cuenca(), 162.0)

    # Stage 12
    builder.road_stage(spain.cuenca(), spain.albacete(), 168.8)

    # Stage 13
    builder.out_and_back_individual_time_trial(spain.albacete(), 53.3)

    # Stage 14
    builder.road_stage(spain.albacete(), spain.valdepenas(), 167.4)

    # Stage 15
    builder.road_stage(spain.valdepenas(), spain.la_pandera(), 172.1)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.mountain_stage(spain.jaen())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 162)

    # Stage 17
    builder.road_stage(spain.granada(), spain.cordoba(), 188.4)

    # Stage 18
    builder.criterium(spain.las_rozas(), 143.8)

    # Stage 19
    builder.road_stage(spain.alcobendas(), spain.collado_villalba(), 164.0)

    # Stage 20
    builder.mountain_time_trial(spain.san_lorenzo_de_el_escorial())
    builder.summit_finish(mountains.sierra_de_guadarrama.alto_de_abantos(), ColCategory.C1, 11.2)

    # Stage 21
    builder.criterium(spain.madrid(), 148.5)

    return builder.build()

def vuelta2004():

    builder = TourOfSpainBuilder(2004,9,4)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.leon(), 28.0)

    # Stage 2
    builder.road_stage(spain.leon(), spain.burgos(), 207.0)

    # Stage 3
    builder.road_stage(spain.burgos(), spain.soria(), 156.0)

    # Stage 4
    builder.road_stage(spain.soria(), spain.zaragoza(), 167.0)

    # Stage 5
    builder.road_stage(spain.zaragoza(), spain.morella(), 186.5)

    # Stage 6
    builder.road_stage(spain.benicarlo(), spain.castellon_de_la_plana(), 157.0)

    # Stage 7
    builder.road_stage(spain.castellon_de_la_plana(), spain.valencia(), 170.0)

    # Stage 8
    builder.out_and_back_individual_time_trial(spain.almussafes(), 40.1)

    # Stage 9
    builder.mountain_stage(spain.xativa())
    builder.summit_finish(mountains.prebaetic.alto_de_aitana(), ColCategory.HC, 162.0)

    # Stage 10
    builder.road_stage(spain.alcoy(), spain.xorret_de_cati(), 174.2)

    # Stage 11
    builder.road_stage(spain.san_vicente_del_raspeig(), spain.caravaca_de_la_cruz(), 165.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.mountain_stage(spain.almeria())
    builder.summit_finish(spain.calar_alto_observatory(), ColCategory.C1, 145.0)

    # Stage 13
    builder.road_stage(spain.el_ejido(), spain.malaga(), 172.0)

    # Stage 14
    builder.road_stage(spain.malaga(), spain.granada(), 167.0)

    # Stage 15
    builder.mountain_time_trial(spain.granada())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 29.6)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.olivenza(), spain.caceres(), 190.1)

    # Stage 17
    builder.mountain_stage(spain.plasencia())
    builder.summit_finish(mountains.sistema_central.la_covatilla(), ColCategory.HC, 170.0)

    # Stage 18
    builder.road_stage(spain.bejar(), spain.avila(), 196.0)

    # Stage 19
    builder.road_stage(spain.avila(), spain.collado_villalba(), 142.0)

    # Stage 20
    builder.mountain_stage(spain.alcobendas())
    builder.summit_finish(mountains.sierra_de_guadarrama.puerto_de_navacerrada(), ColCategory.C1, 178.0)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.madrid(), 28.0)

    return builder.build()

def vuelta2005():

    builder = TourOfSpainBuilder(2005,8,27)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.granada(), 7.0)

    # Stage 2
    builder.road_stage(spain.granada(), spain.cordoba(), 189.3)

    # Stage 3
    builder.road_stage(spain.cordoba(), spain.puertollano(), 153.3)

    # Stage 4
    builder.road_stage(spain.ciudad_real(), spain.argamasilla_de_alba(), 232.3)

    # Stage 5
    builder.road_stage(spain.alcazar_de_san_juan(), spain.cuenca(), 176.0)

    # Stage 6
    builder.road_stage(spain.cuenca(), spain.valdelinares(), 217.0)

    # Stage 7
    builder.road_stage(spain.teruel(), spain.vinaros(), 212.5)

    # Stage 8
    builder.road_stage(spain.tarragona(), spain.lloret_de_mar(), 189.0)

    # Stage 9
    builder.out_and_back_individual_time_trial(spain.lloret_de_mar(), 48.0)

    # Stage 10
    builder.road_stage(spain.la_vall_d_en_bas(), andorra.estacio_d_esqui_d_ordino_alcalis(), 206.3)

    # Stage 11
    builder.mountain_stage(andorra.andorra_la_vella())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 186.6)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.road_stage(spain.logrono(), spain.burgos(), 133.0)

    # Stage 13
    santuario_de_la_bien_aparecida = vicinity(spain.santuario_de_la_bien_aparecida(), "Ampuero")
    builder.road_stage(spain.burgos(), santuario_de_la_bien_aparecida, 196)

    # Stage 14
    builder.mountain_stage(spain.la_penilla())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 172.3)

    # Stage 15
    builder.road_stage(spain.cangas_de_onis(), spain.valgrande_pajares(), 191.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.leon(), spain.valladolid(), 162.5)

    # Stage 17
    builder.road_stage(spain.el_espinar(), spain.la_granja_de_san_ildefonso(), 165.6)

    # Stage 18
    builder.criterium(spain.avila(), 197.5)

    # Stage 19
    builder.road_stage(spain.san_martin_de_valdeiglesias(), spain.alcobendas(), 142.9)

    # Stage 20
    builder.individual_time_trial(spain.guadalajara(), spain.alcala_de_henares(), 38.9)

    # Stage 21
    builder.criterium(spain.madrid(), 136.5)

    return builder.build()

def vuelta2006():

    builder = TourOfSpainBuilder(2006,8,26)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.malaga(), 7.2)

    # Stage 2
    builder.road_stage(spain.malaga(), spain.cordoba(), 167.0)

    # Stage 3
    builder.road_stage(spain.cordoba(), spain.almendralejo(), 220.0)

    # Stage 4
    builder.road_stage(spain.almendralejo(), spain.caceres(), 142.0)

    # Stage 5
    la_covatilla = vicinity(spain.la_covatilla(), "Estacion de Esqui")
    builder.mountain_stage(spain.plasencia())
    builder.summit_finish(Col(la_covatilla.name, la_covatilla.country, la_covatilla.elevation), ColCategory.HC, 178.0)

    # Stage 6
    builder.road_stage(spain.zamora(), spain.leon(), 155.0)

    # Stage 7
    builder.mountain_stage(spain.leon())
    builder.summit_finish(mountains.asturias.alto_del_morredero("Ponferrada"), ColCategory.C1, 148.0)

    # Stage 8
    builder.road_stage(spain.ponferrada(), spain.lugo(), 173.0)

    # Stage 9
    builder.mountain_stage(spain.a_fonsagrada())
    builder.summit_finish(mountains.asturias.alto_de_la_cobertoria(), ColCategory.HC, 206.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    santillana_del_mar = vicinity(spain.santillana_del_mar(), "Museo de Altamira")
    builder.road_stage(spain.aviles(), santillana_del_mar, 190.0)

    # Stage 11
    builder.road_stage(spain.torrelavega(), spain.burgos(), 165.0)

    # Stage 12
    builder.road_stage(spain.aranda_de_duero(), spain.guadalajara(), 162.0)

    # Stage 13
    builder.road_stage(spain.guadalajara(), spain.cuenca(), 170.0)

    # Stage 14
    builder.out_and_back_individual_time_trial(spain.cuenca(), 33.0)

    # Stage 15
    builder.road_stage(spain.motilla_del_palancar(), spain.factoria_ford_almussafes(), 175.0)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.almeria(), spain.calar_alto_observatory(), 145.0)

    # Stage 17
    builder.road_stage(spain.adra(), spain.granada(), 167.0)

    # Stage 18
    builder.mountain_stage(spain.granada())
    builder.summit_finish(mountains.sierra_sur_de_jaen.sierra_de_la_pandera(), ColCategory.C1, 153.0)

    # Stage 19
    builder.road_stage(spain.jaen(), spain.ciudad_real(), 195.0)

    # Stage 20
    builder.individual_time_trial(spain.rivas_futura(), spain.rivas_vaciamadrid(), 28.0)

    # Stage 21
    builder.criterium(spain.madrid(), 150.0)

    return builder.build()

def vuelta2007():

    builder = TourOfSpainBuilder(2007,9,1)

    # Stage 1
    builder.criterium(spain.vigo(), 146.4)

    # Stage 2
    builder.road_stage(spain.allariz(), spain.santiago_de_compostela(), 148.7)

    # Stage 3
    builder.road_stage(spain.viveiro(), spain.luarca(), 153.0)

    # Stage 4
    builder.mountain_stage(spain.langreo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 185.1)

    # Stage 5
    builder.road_stage(spain.cangas_de_onis(), spain.reinosa(), 157.4)

    # Stage 6
    builder.road_stage(spain.reinosa(), spain.logrono(), 184.3)

    # Stage 7
    builder.road_stage(spain.calahora(), spain.zaragoza(), 176.3)

    # Stage 8
    builder.individual_time_trial(spain.carinena(), spain.zaragoza(), 52.2)

    # Stage 9
    builder.mountain_stage(spain.huesca())
    builder.summit_finish(spain.cerler(), ColCategory.C1, 167.6)

    # Stage 10
    builder.mountain_stage(spain.benasque())
    builder.summit_finish(mountains.pyrenees.arcalis(), ColCategory.C1, 214.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.oropesa_del_mar(), spain.algemesi(), 191.3)

    # Stage 12
    builder.road_stage(spain.algemesi(), spain.hellin(), 176.0)

    # Stage 13
    builder.road_stage(spain.hellin(), spain.torre_pacheco(), 176.4)

    # Stage 14
    builder.road_stage(spain.puerto_lumbreras(), spain.villacarrilo(), 207.0)

    # Stage 15
    builder.road_stage(spain.villacarrilo(), spain.granada(), 201.4)

    # Transfer day
    builder.rest_day()

    # Stage 16
    builder.road_stage(spain.jaen(), spain.puertollano(), 161.5)

    # Stage 17
    builder.road_stage(spain.ciudad_real(), spain.talavera_de_la_reina(), 175.0)

    # Stage 18
    builder.road_stage(spain.talavera_de_la_reina(), spain.avila(), 153.5)

    # Stage 19
    builder.mountain_stage(spain.avila())
    builder.summit_finish(mountains.sierra_de_guadarrama.alto_de_abantos(), ColCategory.C1, 133.0)

    # Stage 20
    builder.out_and_back_individual_time_trial(spain.collado_villalba(), 20.0)

    # Stage 21
    builder.road_stage(spain.rivas_vaciamadrid(), spain.madrid(), 104.2)

    return builder.build()

def vuelta2008():

    builder = TourOfSpainBuilder(2008,8,30)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.granada(), 7.7)

    # Stage 2
    builder.road_stage(spain.granada(), spain.jaen(), 167.3)

    # Stage 3
    builder.road_stage(spain.jaen(), spain.cordoba(), 168.6)

    # Stage 4
    builder.road_stage(spain.cordoba(), spain.puertollano(), 170.3)

    # Stage 5
    builder.out_and_back_individual_time_trial(spain.ciudad_real(), 42.5)

    # Stage 6
    builder.road_stage(spain.ciudad_real(), spain.toledo(), 150.1)

    # Transfer day
    builder.rest_day()

    # Stage 7
    builder.road_stage(spain.barbastro(), andorra.naturlandia(), 223.2)

    # Stage 8
    builder.road_stage(andorra.escaldes_engordany(), spain.pla_de_beret(), 151.0)

    # Stage 9
    builder.road_stage(spain.vielha_e_mijaran(), spain.sabinanigo(), 200.8)

    # Stage 10
    builder.road_stage(spain.sabinanigo(), spain.zaragoza(), 151.3)

    # Stage 11
    builder.road_stage(spain.calahorra(), spain.burgos(), 178.0)

    # Stage 12
    builder.road_stage(spain.burgos(), spain.suances(), 186.4)

    # Transfer day
    builder.rest_day()

    # Stage 13
    builder.mountain_stage(spain.san_vicente_de_la_barquera())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 209.5)

    # Stage 14
    builder.road_stage(spain.oviedo(), spain.fuentes_de_invierno(), 158.4)

    # Stage 15
    builder.road_stage(spain.cudillero(), spain.ponferrada(), 202.0)

    # Stage 16
    builder.road_stage(spain.ponferrada(), spain.zamora(), 186.3)

    # Stage 17
    builder.road_stage(spain.zamora(), spain.valladolid(), 148.2)

    # Stage 18
    builder.road_stage(spain.valladolid(), spain.las_rozas(), 167.4)

    # Stage 19
    builder.road_stage(spain.las_rozas(), spain.segovia(), 145.5)

    # Stage 20
    builder.mountain_time_trial(spain.la_granja_de_san_ildefonso())
    builder.summit_finish(mountains.sierra_de_guadarrama.puerto_de_navacerrada(), ColCategory.C1, 17.1)

    # Stage 21
    builder.road_stage(spain.san_sebastian_de_los_reyes(), spain.madrid(), 102.2)

    return builder.build()

def vuelta2009():

    builder = TourOfSpainBuilder(2009,8,29)

    # Stage 1
    builder.out_and_back_individual_time_trial(netherlands.assen(), 4.8)

    # Stage 2
    builder.road_stage(netherlands.assen(), netherlands.emmen(), 203.7)

    # Stage 3
    builder.road_stage(netherlands.zutphen(), netherlands.venlo(), 189.7)

    # Stage 4
    builder.road_stage(netherlands.venlo(), belgium.liege(), 225.5)

    # Transfer day
    builder.rest_day()

    # Stage 5
    builder.road_stage(spain.tarragona(), spain.vinaros(), 174.0)

    # Stage 6
    builder.criterium(spain.xativa(), 176.8)

    # Stage 7
    builder.out_and_back_individual_time_trial(spain.valencia(), 30.0)

    # Stage 8
    builder.mountain_stage(spain.alzira())
    builder.summit_finish(mountains.prebaetic.alto_de_aitana(), ColCategory.HC, 204.7)

    # Stage 9
    builder.road_stage(spain.alcoy(), spain.xorret_de_cati(), 188.8)

    # Stage 10
    builder.road_stage(spain.alicante(), spain.murcia(), 171.2)

    # Stage 11
    builder.road_stage(spain.murcia(), spain.caravaca_de_la_cruz(), 200.0)

    # Transfer day
    builder.rest_day()

    # Stage 12
    builder.mountain_stage(spain.almeria())
    builder.summit_finish(mountains.sierra_de_los_filabres.alto_de_velefique(), ColCategory.HC, 179.3)

    # Stage 13
    builder.mountain_stage(spain.berja())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 172.4)

    # Stage 14
    builder.mountain_stage(spain.granada())
    builder.summit_finish(mountains.sierra_sur_de_jaen.sierra_de_la_pandera(), ColCategory.C1, 157.0)

    # Stage 15
    builder.road_stage(spain.jaen(), spain.cordoba(), 167.7)

    # Stage 16
    builder.road_stage(spain.cordoba(), spain.puertollano(), 170.3)

    # Stage 17
    builder.road_stage(spain.ciudad_real(), spain.talavera_de_la_reina(), 193.6)

    # Stage 18
    builder.road_stage(spain.talavera_de_la_reina(), spain.avila(), 165.0)

    # Stage 19
    builder.road_stage(spain.avila(), spain.la_granja_de_san_ildefonso(), 179.8)

    # Stage 20
    builder.out_and_back_individual_time_trial(spain.toledo(), 27.8)

    # Stage 21
    builder.road_stage(spain.rivas_vaciamadrid(), spain.madrid(), 110.2)

    return builder.build()

def vuelta2010():

    builder = TourOfSpainBuilder(2010,8,28)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.seville(), 13.0)

    # Stage 2
    builder.road_stage(spain.alcala_de_guadaira(), spain.marbella(), 173.0)

    # Stage 3
    builder.road_stage(spain.marbella(), spain.malaga(), 156.0)

    # Stage 4
    builder.road_stage(spain.malaga(), spain.valdepenas_de_jaen(), 177.0)

    # Stage 5
    builder.road_stage(spain.guadix(), spain.lorca(), 194.0)

    # Stage 6
    builder.road_stage(spain.caravaca_de_la_cruz(), spain.murcia(), 144.0)

    # Stage 7
    builder.road_stage(spain.murcia(), spain.orihuela(), 170.0)

    # Stage 8
    builder.road_stage(spain.villena(), spain.xorret_de_cati(), 188.8)

    # Stage 9
    builder.road_stage(spain.calp(), spain.alcoi(), 187.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(spain.tarragona(), spain.vilanova_i_la_geltru(), 173.7)

    # Stage 11
    builder.road_stage(spain.vilanova_i_la_geltru(), andorra.pal(), 208.0)

    # Stage 12
    builder.road_stage(andorra.andorra_la_vella(), spain.lleida(), 175.0)

    # Stage 13
    builder.road_stage(spain.rincon_de_soto(), spain.burgos(), 193.7)

    # Stage 14
    builder.road_stage(spain.burgos(), spain.pena_cabarga(), 178.8)

    # Stage 15
    builder.mountain_stage(spain.solares())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 170.0)

    # Stage 16
    builder.mountain_stage(spain.gijon())
    builder.summit_finish(mountains.asturias.alto_de_cotobello(), ColCategory.C1, 179.3)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.out_and_back_individual_time_trial(spain.penafiel(), 46.0)

    # Stage 18
    builder.road_stage(spain.valladolid(), spain.salamanca(), 153.0)

    # Stage 19
    builder.road_stage(spain.piedrahita(), spain.toledo(), 200.0)

    # Stage 20
    builder.road_stage(spain.san_martin_de_valdeiglesias(), spain.bola_del_mundo(), 168.8)

    # Stage 21
    builder.road_stage(spain.san_sebastian_de_los_reyes(), spain.madrid(), 85.0)

    return builder.build()

def vuelta2011():

    builder = TourOfSpainBuilder(2011,8,20)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.benidorm(), 13.5)

    # Stage 2
    builder.road_stage(spain.la_nucia(), spain.playas_de_orihuela(), 175.5)

    # Stage 3
    builder.road_stage(spain.petrer(), spain.totana(), 163.0)

    # Stage 4
    builder.mountain_stage(spain.baza())
    builder.summit_finish(mountains.sierra_nevada.sierra_nevada(), ColCategory.C1, 170.2)

    # Stage 5
    builder.road_stage(spain.sierra_nevada(), spain.valdepenas_de_jaen(), 187.0)

    # Stage 6
    builder.road_stage(spain.ubeda(), spain.cordoba(), 196.8)

    # Stage 7
    builder.road_stage(spain.almaden(), spain.talavera_de_la_reina(), 187.6)

    # Stage 8
    builder.road_stage(spain.talavera_de_la_reina(), spain.san_lorenzo_de_el_escorial(), 177.3)

    # Stage 9
    builder.mountain_stage(spain.villacastin())
    builder.summit_finish(mountains.sistema_central.la_covatilla(), ColCategory.HC, 183.0)

    # Stage 10
    builder.out_and_back_individual_time_trial(spain.salamanca(), 47.0)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.road_stage(spain.verin(), spain.estacion_de_esqui_manzaneda(), 167.0)

    # Stage 12
    builder.road_stage(spain.ponteareas(), spain.pontevedra(), 167.3)

    # Stage 13
    builder.road_stage(spain.sarria(), spain.ponferrada(), 158.2)

    # Stage 14
    la_farrapona = vicinity(spain.la_farrapona(), "Lagos de Somiedo")
    builder.road_stage(spain.astorga(), la_farrapona, 172.8)

    # Stage 15
    builder.mountain_stage(spain.aviles())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 142.2)

    # Transfer day
    builder.rest_day()

    # Stage 16
    villa_romana_la_olmeda = vicinity(spain.villa_romana_la_olmeda(), "Palancia")
    builder.road_stage(villa_romana_la_olmeda, spain.haro(), 188.1)

    # Stage 17
    faustino_v_oyon = vicinity(spain.faustino_v(), "Oyon")
    builder.road_stage(faustino_v_oyon, spain.pena_cabarga(), 211.0)

    # Stage 18
    builder.road_stage(spain.solares(), spain.noja(), 174.6)

    # Stage 19
    builder.road_stage(spain.noja(), spain.bilbao(), 158.5)

    # Stage 20
    builder.road_stage(spain.bilbao(), spain.vitoria_gasteiz(), 185.0)

    # Stage 21
    builder.road_stage(spain.circuito_del_jarama(), spain.madrid(), 94.2)

    return builder.build()

def vuelta2012():

    builder = TourOfSpainBuilder(2012,8,18)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.pamplona(), 16.5)

    # Stage 2
    builder.road_stage(spain.pamplona(), spain.viana(), 181.4)

    # Stage 3
    arrate_eibar = vicinity(spain.arrate(), "Eibar")
    builder.road_stage(spain.oion(), arrate_eibar, 155.3)

    # Stage 4
    builder.road_stage(spain.barakaldo(), spain.valdezcaray(), 160.6)

    # Stage 5
    builder.criterium(spain.logrono(), 168.0)

    # Stage 6
    el_fuerte_del_rapitan = vicinity(spain.el_fuerte_del_rapitan(), "Jaca")
    builder.road_stage(spain.tarazona(), el_fuerte_del_rapitan, 175.4)

    # Stage 7
    builder.road_stage(spain.huesca(), spain.motorland_aragon_alcaniz(), 164.2)

    # Stage 8
    builder.mountain_stage(spain.lleida())
    builder.summit_finish(mountains.pyrenees.coll_de_la_gallina(), ColCategory.HC, 174.7)

    # Stage 9
    builder.road_stage(andorra.andorra_la_vella(), spain.barcelona(), 196.3)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.road_stage(spain.ponteareas(), spain.sanxenxo(), 190.0)

    # Stage 11
    builder.individual_time_trial(spain.cambados(), spain.pontevedra(), 39.4)

    # Stage 12
    builder.mountain_stage(spain.vilagarcia())
    builder.summit_finish(mountains.galicia.mirador_de_ezaro(), ColCategory.HC, 190.5)

    # Stage 13
    builder.road_stage(spain.santiago_de_compostela(), spain.ferrol(), 172.8)

    # Stage 14
    builder.road_stage(spain.palas_de_rei(), spain.los_ancares(), 149.2)

    # Stage 15
    builder.mountain_stage(spain.la_robla())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 186.5)

    # Stage 16
    builder.road_stage(spain.gijon(), spain.cuitu_negro(), 183.5)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(spain.santander(), spain.fuente_de(), 187.3)

    # Stage 18
    builder.road_stage(spain.aguilar_de_campoo(), spain.valladolid(), 204.5)

    # Stage 19
    builder.road_stage(spain.penafiel(), spain.la_lastrilla(), 178.4)

    # Stage 20
    builder.road_stage(spain.palazuelos_de_eresma(), spain.bola_del_mundo(), 170.7)

    # Stage 21
    builder.road_stage(spain.cercedilla(), spain.madrid(), 115.0)

    return builder.build()

def vuelta2013():

    builder = TourOfSpainBuilder(2013,8,24)

    # Stage 1
    builder.team_time_trial(spain.vilanova_de_arousa(), spain.sanxenxo(), 27.4)

    # Stage 2
    builder.road_stage(spain.pontevedra(), spain.monte_da_groba(), 177.7)

    # Stage 3
    builder.road_stage(spain.vigo(), spain.mirador_de_lobeira(), 184.8)

    # Stage 4
    builder.road_stage(spain.lalin(), spain.finisterra(), 189.0)

    # Stage 5
    builder.road_stage(spain.sober(), spain.lago_de_sanabria(), 174.3)

    # Stage 6
    builder.road_stage(spain.guijuelo(), spain.caceres(), 175.0)

    # Stage 7
    builder.road_stage(spain.almendralejo(), spain.mairena_del_aljarafe(), 205.9)

    # Stage 8
    builder.mountain_stage(spain.jerez_de_la_frontera())
    builder.summit_finish(mountains.sierra_morena.alto_de_penas_blancas(), ColCategory.C1, 166.6)

    # Stage 9
    builder.road_stage(spain.antequera(), spain.valdepenas_de_jaen(), 163.7)

    # Stage 10
    builder.mountain_stage(spain.torredelcampo())
    builder.summit_finish(mountains.sierra_nevada.alto_de_haza_llana(), ColCategory.HC, 186.8)

    # Transfer day
    builder.rest_day()

    # Stage 11
    builder.out_and_back_individual_time_trial(spain.tarrazona(), 38.8)

    # Stage 12
    builder.road_stage(spain.maella(), spain.tarragona(), 164.2)

    # Stage 13
    builder.road_stage(spain.valls(), spain.castelldefels(), 169.0)

    # Stage 14
    builder.mountain_stage(spain.baga())
    builder.summit_finish(mountains.pyrenees.coll_de_la_gallina(), ColCategory.HC, 155.7)

    # Stage 15
    builder.mountain_stage(andorra.andorra_la_vella())
    builder.summit_finish(mountains.pyrenees.peyragudes(), ColCategory.C1, 224.9)

    # Stage 16
    builder.mountain_stage(spain.graus())
    builder.summit_finish(mountains.pyrenees.formigal(), ColCategory.C1, 146.8)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(spain.calahorra(), spain.burgos(), 189.0)

    # Stage 18
    builder.road_stage(spain.burgos(), spain.pena_cabarga(), 186.5)

    # Stage 19
    builder.mountain_stage(spain.san_vicente_de_la_barquera())
    builder.summit_finish(mountains.asturias.alto_del_naranco(), ColCategory.C1, 181)

    # Stage 20
    builder.mountain_stage(spain.aviles())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 142.2)

    # Stage 21
    builder.road_stage(spain.leganes(), spain.madrid(), 109.6)

    return builder.build()

def vuelta2014():

    builder = TourOfSpainBuilder(2014,8,23)

    # Stage 1
    builder.out_and_back_team_time_trial(spain.jerez_de_la_frontera(), 12.6)

    # Stage 2
    builder.road_stage(spain.algerciras(), spain.san_fernando(), 174.4)

    # Stage 3
    builder.road_stage(spain.cadiz(), spain.arcos_de_la_frontera(), 197.8)

    # Stage 4
    builder.road_stage(spain.mairena_del_alcor(), spain.cordoba(), 164.7)

    # Stage 5
    builder.road_stage(spain.priego_de_cordoba(), spain.ronda(), 180.0)

    # Stage 6
    cumbres_verdes = vicinity(spain.cumbres_verdes(), "La Zubia")
    builder.road_stage(spain.benalmadena(), cumbres_verdes, 167.1)

    # Stage 7
    builder.road_stage(spain.alhendin(), spain.alcaudete(), 169.0)

    # Stage 8
    builder.road_stage(spain.baeza(), spain.albacete(), 207.0)

    # Stage 9
    builder.road_stage(spain.carboneras_de_guadazaon(), spain.aramon_valdelinares(), 185.0)

    # Transfer day
    builder.rest_day()

    # Stage 10
    builder.individual_time_trial(spain.monasterio_de_santa_maria_de_veruela(), spain.borja(), 36.7)

    # Stage 11
    builder.road_stage(spain.pamplona(), spain.santuario_de_san_miguel_de_aralar(), 153.4)

    # Stage 12
    builder.criterium(spain.logrono(), 166.4)

    # Stage 13
    parque_de_cabarceno = vicinity(spain.parque_de_cabarceno(), "Obregon")
    builder.road_stage(spain.belorado(), parque_de_cabarceno, 188.7)

    # Stage 14
    la_camperona = vicinity(spain.la_camperona(), "Valle de Sabero")
    builder.road_stage(spain.santander(), la_camperona, 200.8)

    # Stage 15
    builder.mountain_stage(spain.oviedo())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 152.2)

    # Stage 16
    la_farrapona = vicinity(spain.la_farrapona(), "Lagos de Somiedo")
    builder.road_stage(spain.san_martin_del_rey_aurelio(), la_farrapona, 160.5)

    # Transfer day
    builder.rest_day()

    # Stage 17
    builder.road_stage(spain.ortigueira(), spain.a_coruna(), 190.7)

    # Stage 18
    mont_castrove = vicinity(spain.mont_castrove(), "Meis")
    builder.road_stage(spain.a_estrada(), mont_castrove, 157.0)

    # Stage 19
    builder.road_stage(spain.salvaterra_de_mino(), spain.cangas_do_morrazo(), 180.5)

    # Stage 20
    builder.road_stage(spain.santo_estevo_de_ribas_de_sil(), spain.puerto_de_ancares(), 185.7)

    # Stage 21
    builder.out_and_back_individual_time_trial(spain.santiago_de_compostela(), 9.7)

    return builder.build()

def vuelta2015():

    builder = TourOfSpainBuilder(2015,8,22)

    # Stage 1
    builder.team_time_trial(spain.puerto_banus(), spain.marbella(), 7.4)

    # Stage 2
    builder.road_stage(spain.alhaurin_de_la_torre(), spain.caminito_del_ray(), 158.7)

    # Stage 3
    builder.road_stage(spain.mijas(), spain.malaga(), 158.4)

    # Stage 4
    builder.road_stage(spain.estepona(), spain.vejer_de_la_frontera(), 209.6)

    # Stage 5
    builder.road_stage(spain.rota(), spain.alcala_de_guadaira(), 167.3)

    # Stage 6
    builder.road_stage(spain.cordoba(), spain.sierra_de_cazorla(), 200.3)

    # Stage 7
    builder.road_stage(spain.jodar(), spain.la_alpujarra(), 191.1)

    # Stage 8
    builder.road_stage(spain.puebla_de_don_fadrique(), spain.murcia(), 182.5)

    # Stage 9
    cumbre_del_sol = vicinity(spain.cumbre_del_sol(), "Benitachell")
    builder.road_stage(spain.torrevieja(), cumbre_del_sol, 168.3)

    # Stage 10
    builder.road_stage(spain.valencia(), spain.castellon_de_la_plana(), 146.6)

    # Rest day
    builder.rest_day(andorra.andorra_la_vella())

    # Stage 11
    builder.road_stage(andorra.andorra_la_vella(), spain.cortals_d_encamp(), 138.0)

    # Stage 12
    builder.road_stage(andorra.escaldes_engordany(), spain.lleida(), 173.0)

    # Stage 13
    builder.road_stage(spain.calatayud(), spain.tarazona(), 178.0)

    # Stage 14
    builder.mountain_stage(spain.vitoria_gasteiz())
    builder.summit_finish(mountains.cantabria.alto_campoo(), ColCategory.HC, 215)

    # Stage 15
    builder.road_stage(spain.comillas(), spain.sotres(), 175.8)

    # Stage 16
    ermita_del_alba = vicinity(spain.ermita_del_alba(), "Quiros")
    builder.road_stage(spain.luarca(), ermita_del_alba, 185.0)

    # Rest day
    builder.rest_day(spain.burgos())

    # Stage 17
    builder.out_and_back_individual_time_trial(spain.burgos(), 38.7)

    # Stage 18
    builder.road_stage(spain.roa_de_duero(), spain.riaza(), 204.0)

    # Stage 19
    builder.road_stage(spain.medina_del_campo(), spain.avila(), 185.8)

    # Stage 20
    builder.road_stage(spain.san_lorenzo_de_el_escorial(), spain.cercedilla(), 175.8)

    # Stage 21
    builder.road_stage(spain.alcala_de_henares(), spain.madrid(), 98.8)

    return builder.build()

def vuelta2016():

    builder = TourOfSpainBuilder(2016,8,20)

    # Stage 1
    builder.team_time_trial(spain.laias(), spain.parque_nautico_castrelo_de_mino(), 7.4)

    # Stage 2
    builder.road_stage(spain.ourense(), spain.baiona(), 160.8)

    # Stage 3
    mirador_de_ezaro = vicinity(spain.mirador_de_ezaro(), "Dumbria")
    builder.mountain_stage(spain.marin())
    builder.summit_finish(Col(mirador_de_ezaro.name, mirador_de_ezaro.country, mirador_de_ezaro.elevation), ColCategory.C1, 176.4)

    # Stage 4
    builder.road_stage(spain.betanzos(), spain.san_andres_de_teixido(), 163.5)

    # Stage 5
    builder.road_stage(spain.viveiro(), spain.lugo(), 171.3)

    # Stage 6
    builder.road_stage(spain.monforte_de_lemos(), spain.ribeira_sacra(), 163.2)

    # Stage 7
    builder.road_stage(spain.maceda(), spain.puebla_de_sanabria(), 158.5)

    # Stage 8
    la_camperona = vicinity(spain.la_camperona(), "Valle de Sabero")
    builder.road_stage(spain.villalpando(), la_camperona, 181.5)

    # Stage 9
    builder.road_stage(spain.cistierna(), mountains.asturias.alto_del_naranco(), 164.5)

    # Stage 10
    builder.mountain_stage(spain.lugones())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.C1, 188.7)

    # Rest day
    builder.rest_day(spain.oviedo())

    # Stage 11
    jurassic_museum_of_asturias = vicinity(spain.jurassic_museum_of_asturias(), "Colunga")
    builder.road_stage(jurassic_museum_of_asturias, spain.pena_cabarga(), 168.6)

    # Stage 12
    builder.road_stage(spain.los_corrales_de_buelna(), spain.bilbao(), 193.2)

    # Stage 13
    builder.road_stage(spain.bilbao(), spain.urdax_dantxarinea(), 213.4)

    # Stage 14
    builder.mountain_stage(spain.urdax_dantxarinea())
    builder.summit_finish(mountains.pyrenees.col_d_aubisque(), ColCategory.HC, 196.0)

    # Stage 15
    aramon_formigal = vicinity(spain.aramon_formigal(), "Sallent de Gallego")
    builder.road_stage(spain.sabinanigo(), aramon_formigal, 118.5)

    # Stage 16
    builder.road_stage(spain.alcaniz(), spain.peniscola(), 156.4)

    # Rest day
    builder.rest_day(spain.castellon_de_la_plana())

    # Stage 17
    camins_del_penyagolosa = vicinity(spain.camins_del_penyagolosa(), "Llucena")
    builder.road_stage(spain.castellon_de_la_plana(), camins_del_penyagolosa, 177.5)

    # Stage 18
    builder.road_stage(spain.requena(), spain.gandia(), 200.6)

    # Stage 19
    builder.individual_time_trial(spain.xabia(), spain.calp(), 37.0)

    # Stage 20
    builder.mountain_stage(spain.benidorm())
    builder.summit_finish(mountains.prebaetic.alto_de_aitana(), ColCategory.HC, 193.2)

    # Stage 21
    builder.road_stage(spain.las_rozas(), spain.madrid(), 104.8)

    return builder.build()

def vuelta2017():

    builder = TourOfSpainBuilder(2017,8,19)

    # Stage 1
    builder.out_and_back_team_time_trial(france.nimes(), 13.7)

    # Stage 2
    builder.road_stage(france.nimes(), france.gruissan(), 203.4)

    # Stage 3
    builder.road_stage(france.prades(), andorra.andorra_la_vella(), 158.5)

    # Stage 4
    builder.road_stage(andorra.escaldes_engordany(), spain.tarragona(), 198.2)

    # Stage 5
    builder.road_stage(spain.benicassim(), spain.alcossebre(), 175.7)

    # Stage 6
    builder.road_stage(spain.villareal(), spain.sagunto(), 204.4)

    # Stage 7
    builder.road_stage(spain.lliria(), spain.cuenca(), 207.0)

    # Stage 8
    builder.road_stage(spain.hellin(), spain.xorret_de_cati(), 199.5)

    # Stage 9
    builder.road_stage(spain.orihuela(), spain.benitachell(), 174.0)

    # Rest day
    builder.rest_day(spain.alicante())

    # Stage 10
    builder.road_stage(spain.caravaca_de_la_cruz(), spain.el_pozo(), 164.8)

    # Stage 11
    builder.mountain_stage(spain.lorca())
    builder.summit_finish(spain.calar_alto_observatory(), ColCategory.C1, 187.5)

    # Stage 12
    builder.road_stage(spain.motril(), spain.antequera(), 160.1)

    # Stage 13
    builder.road_stage(spain.coin(), spain.tomares(), 198.4)

    # Stage 14
    builder.mountain_stage(spain.ecija())
    builder.summit_finish(mountains.sierra_sur_de_jaen.sierra_de_la_pandera(), ColCategory.C1, 175.0)

    # Stage 15
    builder.mountain_stage(spain.alcala_la_real())
    builder.summit_finish(mountains.sierra_nevada.alto_hoya_de_la_mora(), ColCategory.HC, 129.4)

    # Rest day
    builder.rest_day(spain.logrono())

    # Stage 16
    builder.individual_time_trial(spain.circuito_de_navarra(), spain.logrono(), 40.2)

    # Stage 17
    builder.mountain_stage(spain.villadiego())
    builder.summit_finish(mountains.cantabria.alto_de_los_machucos(), ColCategory.HC, 180.5)

    # Stage 18
    builder.road_stage(spain.suances(), spain.santo_toribo_de_liebana(), 169.0)

    # Stage 19
    builder.road_stage(spain.caso(), spain.gijon(), 149.7)

    # Stage 20
    builder.mountain_stage(spain.corvera_de_asturias())
    builder.summit_finish(mountains.asturias.alto_de_l_angliru(), ColCategory.HC, 117.5)

    # Stage 21
    builder.road_stage(spain.arroyomolinos(), spain.madrid(), 117.7)

    return builder.build()

def vuelta2018():

    builder = TourOfSpainBuilder(2018,8,25)

    # Stage 1
    builder.out_and_back_individual_time_trial(spain.malaga(), 8.0)

    # Stage 2
    builder.road_stage(spain.marbella(), spain.caminito_del_ray(), 163.9)

    # Stage 3
    builder.road_stage(spain.mijas(), spain.alhaurin_de_la_torre(), 182.5)

    # Stage 4
    builder.road_stage(spain.velez_malaga(), spain.alfacar(), 162.0)

    # Stage 5
    builder.road_stage(spain.granada(), spain.roquetas_de_mar(), 188.0)

    # Stage 6
    builder.road_stage(spain.huercal_overa(), spain.san_javier(), 153.0)

    # Stage 7
    builder.road_stage(spain.puerto_lumbreras(), spain.pozo_alcon(), 182.0)

    # Stage 8
    builder.road_stage(spain.linares(), spain.almaden(), 195.5)

    # Stage 9
    builder.mountain_stage(spain.talavera_de_la_reina())
    builder.summit_finish(mountains.sistema_central.la_covatilla(), ColCategory.HC, 195.0)

    # Rest day
    builder.rest_day(spain.salamanca())

    # Stage 10
    builder.road_stage(spain.salamanca(), spain.fermosella(), 172.5)

    # Stage 11
    builder.road_stage(spain.mombuey(), spain.ribeira_sacra(), 208.8)

    # Stage 12
    builder.road_stage(spain.mondonedo(), spain.punta_de_estaca_de_bars(), 177.5)

    # Stage 13
    builder.road_stage(spain.candas(), spain.la_camperona(), 175.5)

    # Stage 14
    builder.road_stage(spain.cistierna(), spain.les_praeres_de_nava(), 167.0)

    # Stage 15
    builder.mountain_stage(spain.ribera_de_arriba())
    builder.summit_finish(mountains.asturias.lagos_de_covadonga(), ColCategory.HC, 185.5)

    # Rest day
    builder.rest_day(spain.santander())

    # Stage 16
    builder.individual_time_trial(spain.santillana_del_mar(), spain.torrelavega(), 32.7)

    # Stage 17
    builder.road_stage(spain.getxo(), spain.oiz(), 166.4)

    # Stage 18
    builder.road_stage(spain.ejea_de_los_caballeros(), spain.lleida(), 180.5)

    # Stage 19
    builder.road_stage(spain.lleida(), andorra.naturlandia(), 157.0)

    # Stage 20
    builder.mountain_stage(andorra.escaldes_engordany())
    builder.summit_finish(mountains.pyrenees.coll_de_la_gallina(), ColCategory.C1, 105.8)

    # Stage 21
    builder.road_stage(spain.alcorcon(), spain.madrid(), 112.3)

    return builder.build()

