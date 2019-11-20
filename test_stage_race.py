import country
import pytest
from datetime   import datetime
from location   import Location
from stage      import Criterium, IndividualTimeTrial, Prologue, RestDay, RoadStage, TeamTimeTrial
from stage_race import Dauphine, StageRace, TourDeFrance

class TestStageRace:

    def test_stage_race_length(self):

        france = country.France()
        paris  = Location("Paris", france)
        tours  = Location("Tours", france)

        july_1st = datetime(2018,7,1)
        july_2nd = datetime(2018,7,2)
        july_3rd = datetime(2018,7,3)
        july_4th = datetime(2018,7,4)
        july_5th = datetime(2018,7,5)

        prologue = Prologue(july_1st, paris, paris, 6.6)
        stage1   = RoadStage(july_2nd, "1", paris, tours, 256)
        stage2   = Criterium(july_3rd, "2", tours, 237 )
        rest_day = RestDay(july_4th, tours)
        stage3   = TeamTimeTrial(july_5th, "3", tours, tours, 35.7)

        tdf = TourDeFrance()
        tdf.add_stage(prologue)
        tdf.add_stage(stage1)
        tdf.add_stage(stage2)
        tdf.add_stage(rest_day)
        tdf.add_stage(stage3)

        assert len(tdf) == 4

        distance = tdf.prologue_kilometres + \
            tdf.road_stage_kilometres + \
            tdf.team_time_trial_kilometres + \
            tdf.individual_time_trial_kilometres

        assert tdf.distance == distance

        assert tdf.number_of_road_stages == 2
        assert tdf.number_of_team_time_trials == 1
        assert tdf.number_of_individual_time_trials == 0
        assert tdf.number_of_rest_days == 1

        assert tdf.first_stage == prologue
        assert tdf.depart == prologue.start
        assert tdf.last_stage == stage3
        assert tdf.arrive == stage3.finish

    def test_dauphine(self):
        dauphine = Dauphine()
        with pytest.raises(Exception):
            dauphine.name

    def test_dauphine_pre_2010(self):
        france = country.France()
        nancy = Location("Nancy", france)
        itt = IndividualTimeTrial(datetime(2009,6,7), "1", nancy, nancy, 12.1)
        dauphine = Dauphine()
        dauphine.add_stage(itt)
        assert dauphine.name == "Critérium du Dauphiné Libéré"

    def test_dauphine_post_2010(self):
        france = country.France()
        valence = Location("Valence", france)
        prologue = Prologue(datetime(2018,6,3), valence, valence, 6.6)
        dauphine = Dauphine()
        dauphine.add_stage(prologue)
        assert dauphine.name == "Critérium du Dauphiné"
