import country
import inspect
import pytest

from datetime           import datetime
from location           import Location
from stage              import Criterium, IndividualTimeTrial, Prologue, RestDay, RoadStage, TeamTimeTrial
from stage_race         import Dauphine, StageRace, TourDeFrance, TourOfItaly
from stage_race_builder import StageRaceBuilder

class TestStageRaceBuilder:

    def test_stage_race_builder(self):

        france  = country.France()
        amiens  = Location("Amiens", france)
        boulogne = Location("Boulogne", france)
        grenoble = Location("Grenoble", france)
        lehavre = Location("Le Havre", france)
        letouquet = Location("Le Touquet", france)
        morzine = Location("Morzine", france)
        limoges = Location("Limoges", france)
        nantes  = Location("Nantes", france)
        paris   = Location("Paris", france)
        quimper = Location("Quimper", france)
        rennes  = Location("Rennes", france)
        rouen   = Location("Rouen", france)
        tours   = Location("Tours", france)

        builder = StageRaceBuilder(TourDeFrance(), datetime(2018,7,1))
        builder.prologue(paris, paris, 6.6)
        builder.criterium(paris, 256)
        builder.road_stage(paris, tours, 265)
        builder.road_stage(tours, limoges, 248)
        builder.rest_day(limoges)
        builder.road_stage(limoges, nantes, 259)
        builder.out_and_back_team_time_trial(nantes, 48)
        builder.road_stage(nantes, quimper, 289)
        builder.road_stage(quimper, rennes, 239)
        builder.out_and_back_individual_time_trial(rennes, 65)
        builder.enable_split_stages()
        builder.criterium(lehavre, 100)
        builder.road_stage(lehavre, rouen, 150)
        builder.disable_split_stages()
        builder.road_stage(rouen, amiens, 187.2)
        builder.enable_morning_stage()
        builder.road_stage(amiens, boulogne, 189)
        builder.individual_time_trial(boulogne, letouquet, 40)
        builder.rest_day(grenoble)
        builder.road_stage(grenoble, morzine, 257.3)
        tdf = builder.build()

        route = """P,1 July,Paris,6.6 km,Individual time trial
        1,2 July,Paris,256.0 km,Road stage
        2,3 July,Paris to Tours,265.0 km,Road stage
        3,4 July,Tours to Limoges,248.0 km,Road stage
        ,5 July,Rest day,Limoges
        4,6 July,Limoges to Nantes,259.0 km,Road stage
        5,7 July,Nantes,48.0 km,Team time trial
        6,8 July,Nantes to Quimper,289.0 km,Road stage
        7,9 July,Quimper to Rennes,239.0 km,Road stage
        8,10 July,Rennes,65.0 km,Individual time trial
        9a,11 July,Le Havre,100.0 km,Road stage
        9b,11 July,Le Havre to Rouen,150.0 km,Road stage
        10,12 July,Rouen to Amiens,187.2 km,Road stage
        11,13 July,Amiens to Boulogne,189.0 km,Road stage
        12,13 July,Boulogne to Le Touquet,40.0 km,Individual time trial
        ,14 July,Rest day,Grenoble
        13,15 July,Grenoble to Morzine,257.3 km,Road stage"""

        assert tdf.route == inspect.cleandoc(route)

    def test_morning_stages(self):

        italy  = country.Italy()
        palermo = Location("Palermo", italy)
        sciacca = Location("Sciacca", italy)

        builder = StageRaceBuilder(TourOfItaly(), datetime(1986,5,12))
        builder.enable_morning_stage()
        builder.out_and_back_prologue(palermo, 1)
        builder.road_stage(palermo, sciacca, 140)
        giro = builder.build()

        route = """P,12 May,Palermo,1.0 km,Individual time trial
        1,12 May,Palermo to Sciacca,140.0 km,Road stage"""

        assert giro.route == inspect.cleandoc(route)

    def test_prologue_exceptions(self):

        """A Prologue must be the first stage"""
        italy  = country.Italy()
        palermo = Location("Palermo", italy)
        sciacca = Location("Sciacca", italy)
        builder = StageRaceBuilder(TourOfItaly(), datetime(1986,5,12))
        builder.road_stage(palermo, sciacca, 140)
        with pytest.raises(Exception):
            builder.out_and_back_prologue(palermo, 1)

    def test_rest_day_exceptions(self):

        """A rest day cannot be the first stage"""
        italy  = country.Italy()
        palermo = Location("Palermo", italy)
        sciacca = Location("Sciacca", italy)
        builder = StageRaceBuilder(TourOfItaly(), datetime(1986,5,12))
        with pytest.raises(Exception):
            builder.rest_day(palermo)

        """A rest day cannot be the morning stage"""
        builder.enable_morning_stage()
        with pytest.raises(Exception):
            builder.rest_day(palermo)

        """A rest day cannot be the afternoon stage"""
        builder.out_and_back_prologue(palermo, 1)
        with pytest.raises(Exception):
            builder.rest_day(palermo)

    def test_build_exceptions(self):

        """build() throws when there are no stages"""
        builder = StageRaceBuilder(TourOfItaly(), datetime(1986,5,12))
        with pytest.raises(Exception):
            builder.build()

        italy  = country.Italy()
        palermo = Location("Palermo", italy)
        sciacca = Location("Sciacca", italy)

        builder = StageRaceBuilder(TourOfItaly(), datetime(1986,5,12))
        builder.enable_morning_stage()
        builder.out_and_back_prologue(palermo, 1)
        builder.road_stage(palermo, sciacca, 140)
        builder.rest_day()
        with pytest.raises(Exception):
            builder.build()
