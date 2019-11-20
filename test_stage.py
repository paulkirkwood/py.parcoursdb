import country
from datetime import datetime
from location import Location
from stage import Prologue, RoadStage, TeamTimeTrial, IndividualTimeTrial, Criterium, PrologueTeamTimeTrial, RestDay

class TestStage:

    def test_stage_id(self):
        france = country.France()
        paris = Location("Paris", france)
        tours = Location("Tours", france)
        prologue = Prologue(datetime(2018,7,1), paris, paris, 6.7)
        prologue_ttt = PrologueTeamTimeTrial(datetime(2018,7,1), paris, paris, 10.8)
        road_stage =  RoadStage(datetime(2018,7,1), "1", paris, tours, 265)
        assert prologue.id == "P"
        assert prologue_ttt.id == "P"
        assert road_stage.id == "1"

    def test_stage_description(self):
        france  = country.France()
        paris   = Location("Paris", france)
        nantes  = Location("Nantes", france)
        limoges = Location("Limoges", france)
        lemans  = Location("Le Mans", france)

        prologue              = Prologue(datetime(2018,7,1), paris, paris, 7.8)
        road_stage            = RoadStage(datetime(2018,7,2), "1", nantes, limoges, 257)
        team_time_trial       = TeamTimeTrial(datetime(2018,7,3), "2", nantes, nantes, 56.8)
        individual_time_trial = IndividualTimeTrial(datetime(2018,7,4), "3", limoges, limoges, 32.4)
        criterium             = Criterium(datetime(2018,7,5), "4", lemans, 234 )

        assert prologue.description == "Individual time trial"
        assert road_stage.description == "Road stage"
        assert team_time_trial.description == "Team time trial"
        assert individual_time_trial.description == "Individual time trial"
        assert criterium.description == "Road stage"

    def test_rest_day(self):
        france = country.France()
        limoges = Location("Limoges", france)
        rest_day = RestDay(datetime(2018,7,6), limoges)
        assert rest_day.route(france) == ',6 July,Rest day,Limoges'

        switzerland = country.Switzerland()
        basel = Location("Basel", switzerland)
        swiss_rest_day = RestDay(datetime(2018,7,6), basel)
        assert swiss_rest_day.route(france) == ',6 July,Rest day,Basel (Switzerland)'

        transfer_day = RestDay(datetime(2018,7,6))
        france = country.France()
        assert transfer_day.route(france) == ',6 July,Rest day'

    def test_route(self):
        france = country.France()
        lemans  = Location("Le Mans", france)
        criterium = Criterium(datetime(2018,7,7), "4", lemans, 234 )
        assert criterium.route(france) == '4,7 July,Le Mans,234.0 km,Road stage'

        nantes  = Location("Nantes", france)
        limoges = Location("Limoges", france)
        road_stage = RoadStage(datetime(2018,7,7), "1", nantes, limoges, 257)
        assert road_stage.route(france) == '1,7 July,Nantes to Limoges,257.0 km,Road stage'
