import copy
import stage
from col        import CategorisedCol
from datetime   import datetime, timedelta
from stage      import Criterium, IndividualTimeTrial
from stage      import Prologue, PrologueTeamTimeTrial, PrologueTwoManTeamTimeTrial
from stage      import RestDay, RoadStage, TeamTimeTrial, ThreeManTeamTimeTrial
from stage_race import Dauphine, ParisNice, TourDeFrance, TourOfItaly, TourOfSpain

class StageRaceBuilder(object):

    def __init__(self,stage_race,date):
            self._stage_race = stage_race
            self._date = date
            self._stage_number = 1
            self._stage_suffix = 'a'
            self._stages = []
            self._cols = {}
            self._split_stages = False
            self._new_state(ConsecutiveStageBuilder)

    def _new_state(self, state):
        self.__class__ = state

    def enable_split_stages(self):
        self._split_stages = True
        self._stage_suffix = 'a'

    def disable_split_stages(self):
        self._new_state(ConsecutiveStageBuilder)
        self._split_stages = False
        self._increment_stage_date()
        self._increment_stage_number()

    def enable_morning_stage(self):
        self._new_state(MorningStageBuilder)

    def enable_a_b_stage(self):
        self._new_state(StageABuilder)
        self._stage_suffix = 'A'

    def mountain_stage(self, start):
        self._stage_start = start
        self._new_state(MountainStageBuilder)

    def mountain_time_trial(self, start):
        self._stage_start = start
        self._new_state(MountainTimeTrialBuilder)

    def non_consecutive_stages(self):
        self._new_stage(NonConsecutiveStageRaceBuilder)

    def build(self):
        if len(self._stages) == 0:
            raise NotImplementedError( "No stages have been added")
        elif isinstance(self._stages[-1], RestDay):
            raise NotImplementedError( "A stage race cannot end with a rest day")
        for stage in self._stages:
            self._stage_race.add_stage(stage)
        return self._stage_race

    def _increment_stage_date(self):
        if self._split_stages == False:
          self._date = self._date + timedelta(days=1)

    def _increment_stage_number(self):
        if self._split_stages == False:
          self._stage_number += 1

    def _increment_stage_suffix(self):
        if self._split_stages == True:
          self._stage_suffix = chr(ord(self._stage_suffix) + 1)

    def prologue(self, start, finish, distance):
        if len(self._stages) > 0:
            raise NotImplementedError( "A prologue must be the first stage")
        prologue = Prologue(self._date, start, finish, distance)
        self._stages.append(prologue)
        self._increment_stage_date()

    def out_and_back_prologue(self, start, distance):
        self.prologue(start, start, distance)

    def prologue_team_time_trial(self, start, finish, distance):
        if len(self._stages) > 0:
            raise NotImplementedError( "A prologue must be the first stage")
        prologue = PrologueTeamTimeTrial(self._date, start, finish, distance)
        self._stages.append(prologue)
        self._increment_stage_date()

    def prologue_two_man_team_time_trial(self, start, distance):
        if len(self._stages) > 0:
            raise NotImplementedError( "A prologue must be the first stage")
        prologue = PrologueTwoManTeamTimeTrial(self._date, start, start, distance)
        self._stages.append(prologue)
        self._increment_stage_date()

    def road_stage(self, start, finish, distance):
        stage = RoadStage(self._date, self.stage_id(), start, finish, distance, copy.deepcopy(self._cols))
        self._stages.append(stage)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()

    def criterium(self,start,distance):
        self.road_stage(start, start, distance)

    def team_time_trial(self, start, finish, distance):
        ttt = TeamTimeTrial(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(ttt)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()

    def out_and_back_team_time_trial(self, start, distance):
        self.team_time_trial(start, start, distance)

    def three_man_team_time_trial(self, start, distance):
        ttt = ThreeManTeamTimeTrial(self._date, self.stage_id(), start, start, distance)
        self._stages.append(ttt)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()

    def individual_time_trial(self, start, finish, distance):
        ttt = IndividualTimeTrial(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(ttt)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()

    def out_and_back_individual_time_trial(self, start, distance):
        self.individual_time_trial(start, start, distance)

    def rest_day(self,location = None):
        if len(self._stages) == 0:
            raise NotImplementedError( "A rest day cannot be the first stage")
        elif len(self._stages) > 0 and isinstance(self._stages[-1], RestDay):
            raise NotImplementedError( "A rest day cannot follow a rest day" )
        rest_day = RestDay(self._date, location)
        self._stages.append(rest_day)
        self._increment_stage_date()

class ConsecutiveStageBuilder(StageRaceBuilder):

    def stage_id(self):
      if self._split_stages == True:
        id = '{i}{suffix}'
        return id.format(i = self._stage_number, suffix = self._stage_suffix)
      else:
        id = '{i}'
        return id.format(i = self._stage_number)

class MorningStageBuilder(ConsecutiveStageBuilder):

    def prologue(self, start, finish, distance):
        if len(self._stages) > 0:
            raise NotImplementedError( "A prologue must be the first stage")
        prologue = Prologue(self._date, start, finish, distance)
        self._stages.append(prologue)
        self._new_state(AfternoonStageBuilder)

    def road_stage(self, start, finish, distance):
        stage = RoadStage(self._date, self.stage_id(), start, finish, distance, copy.deepcopy(self._cols))
        self._stages.append(stage)
        self._increment_stage_number()
        self._new_state(AfternoonStageBuilder)

    def team_time_trial(self, start, finish, distance):
        ttt = TeamTimeTrial(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(ttt)
        self._increment_stage_number()
        self._new_state(AfternoonStageBuilder)

    def individual_time_trial(self, start, finish, distance):
        itt = IndividualTimeTrial(self._date, self.stage_id(), start, finish, distance, copy.deepcopy(self._cols))
        self._stages.append(itt)
        self._increment_stage_number()
        self._new_state(AfternoonStageBuilder)

    def _increment_stage_date(self):
        raise NotImplementedError( "Morning and afternoon stages are on the same date" )

    def rest_day(self,location):
        raise NotImplementedError( "A rest day cannot be the morning stage" )

class AfternoonStageBuilder(ConsecutiveStageBuilder):

    def road_stage(self, start, finish, distance):
        stage = RoadStage(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(stage)
        self._increment_stage_date()
        self._increment_stage_number()
        self._new_state(ConsecutiveStageBuilder)

    def team_time_trial(self, start, finish, distance):
        ttt = TeamTimeTrial(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(ttt)
        self._increment_stage_date()
        self._increment_stage_number()
        self._new_state(ConsecutiveStageBuilder)

    def individual_time_trial(self, start, finish, distance):
        itt = IndividualTimeTrial(self._date, self.stage_id(), start, finish, distance)
        self._stages.append(itt)
        self._increment_stage_date()
        self._increment_stage_number()
        self._new_state(ConsecutiveStageBuilder)

    def rest_day(self,location):
        raise NotImplementedError( "A rest day cannot be the afternoon stage" )

class MountainStageBuilder(ConsecutiveStageBuilder):

    def summit_finish(self, col, category, km):
        self.add_col_to_stage(col, category, km)
        stage = RoadStage(self._date, self.stage_id(), self._stage_start, col, km, copy.deepcopy(self._cols))
        self._cols.clear()
        self._stages.append(stage)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()
        self._new_state(ConsecutiveStageBuilder)

    def add_col_to_stage(self, col, category, km):
        if km < 0:
            raise InvalidKilometreError( "'km' must be greater than 0" )
        if km in self._cols:
            raise DuplicateColError( "There is already a Col at that point in the stage" )
        self._cols[km] = CategorisedCol(col, category)

    def road_stage(self):
        raise NotImplementedError( "A road stage cannot be added during a mountain stage" )

    def team_time_trial(self):
        raise NotImplementedError( "A team time trial cannot be added during a mountain stage" )

    def individual_time_trial(self):
        raise NotImplementedError( "A individual time trial cannot be added during a mountain stage" )

    def rest_day(self,location):
        raise NotImplementedError( "A rest day cannot be added during a mountain stage" )

class MountainTimeTrialBuilder(MountainStageBuilder):

    def summit_finish(self, col, category, km):
        self.add_col_to_stage(col, category, km)
        stage = IndividualTimeTrial(self._date, self.stage_id(), self._stage_start, col, km, copy.deepcopy(self._cols))
        self._cols.clear()
        self._stages.append(stage)
        self._increment_stage_date()
        self._increment_stage_number()
        self._increment_stage_suffix()
        self._new_state(ConsecutiveStageBuilder)

class StageABuilder(ConsecutiveStageBuilder):

    def out_and_back_individual_time_trial(self, start, distance):
        itt = IndividualTimeTrial(self._date, self.stage_id(), start, start, distance, copy.deepcopy(self._cols))
        self._stages.append(itt)
        self._increment_stage_date()
        self._stage_suffix = chr(ord(self._stage_suffix) + 1)
        self._new_state(StageBBuilder)

    def stage_id(self):
        id = '{i}{suffix}'
        return id.format(i = self._stage_number, suffix = self._stage_suffix)

class StageBBuilder(StageABuilder):

    def criterium(self, start, distance):
        stage = RoadStage(self._date, self.stage_id(), start, start, distance)
        self._stages.append(stage)
        self._increment_stage_date()
        self._increment_stage_number()
        self._new_state(ConsecutiveStageBuilder)

class NonConsecutiveStageRaceBuilder(object):

    def __init__(self,stage_race,year):
        self._stage_race   = stage_race
        self._year         = year
        self._stage_number = 1
        self._stages       = []

    def build(self):
        if len(self._stages) == 0:
            raise NoStagesError( "No stages have been added")
        for stage in self._stages:
            self._stage_race.add_stage(stage)
        return self._stage_race

    def road_stage(self, month, day, start, finish, distance):
        self._add_stage(RoadStage(datetime(self._year, month, day), self.stage_id, start, finish, distance))

    def team_time_trial(self, month, day, start, finish, distance):
        self._add_stage(TeamTimeTrial(datetime(self._year, month, day), self.stage_id, start, finish, distance))

    @property
    def stage_id(self):
        id = '{i}'
        return id.format(i = self._stage_number)

    def _add_stage(self, stage):
        self._stages.append(stage)
        self._stage_number += 1

class DauphineBuilder(StageRaceBuilder):
    def __init__(self,year,month,day):
        super().__init__(Dauphine(), datetime(year, month, day))

class ParisNiceBuilder(StageRaceBuilder):
    def __init__(self,year,month,day):
        super().__init__(ParisNice(), datetime(year, month, day))

class TourDeFranceBuilder(StageRaceBuilder):
    def __init__(self,year,month,day):
        super().__init__(TourDeFrance(), datetime(year, month, day))

class TourOfItalyBuilder(StageRaceBuilder):
    def __init__(self,year,month,day):
        super().__init__(TourOfItaly(), datetime(year, month, day))

class TourOfSpainBuilder(StageRaceBuilder):
    def __init__(self,year,month,day):
        super().__init__(TourOfSpain(), datetime(year, month, day))
