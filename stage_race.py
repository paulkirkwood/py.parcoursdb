import country
import re
from stage import RacingStage, RoadStage, TeamTimeTrial, IndividualTimeTrial, RestDay

class StageRace(object):

    def __init__(self,name,country):
        self._name = name
        self._country = country
        self._stages = []

    def __len__(self):
        return len(self.racing_stages)

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def stages(self):
        return self._stages

    def add_stage(self,stage):
        self.stages.append(stage)

    @property
    def racing_stages(self):
        """The non rest-day stages in the stage race"""
        return [stage for stage in self.stages if isinstance(stage, RacingStage)]

    @property
    def distance(self):
        """Total distance"""
        return sum(stage.distance for stage in self.racing_stages)

    @property
    def prologue(self):
        """Return the Prologue stage if it exists"""
        return next((stage for stage in self.racing_stages if stage.id == "P"), None)

    @property
    def prologue_kilometres(self):
        """Return the length of the Prologue if it exists"""
        return next((stage.distance for stage in self.racing_stages if stage.id == "P"), 0)

    @property
    def road_stages(self):
        """The road stages in the stage race"""
        return [stage for stage in self.stages if isinstance(stage, RoadStage)]

    @property
    def road_stage_kilometres(self):
        """Total road KMs"""
        return sum(stage.distance for stage in self.road_stages)

    @property
    def number_of_road_stages(self):
        """The number of road stages in the stage race"""
        return len(self.road_stages)

    @property
    def team_time_trials(self):
        """The team time trials in the stage race"""
        return [stage for stage in self.stages if isinstance(stage, TeamTimeTrial)]

    @property
    def team_time_trial_kilometres(self):
        """Total TTT KMs"""
        return sum(stage.distance for stage in self.team_time_trials)

    @property
    def number_of_team_time_trials(self):
        """The number of team time trials in the stage race"""
        return len(self.team_time_trials)

    @property
    def individual_time_trials(self):
        """The team time trials in the stage race"""
        return [stage for stage in self.stages if isinstance(stage, IndividualTimeTrial)]

    @property
    def individual_time_trial_kilometres(self):
        """Total ITT KMs"""
        return sum(stage.distance for stage in self.individual_time_trials)

    @property
    def number_of_individual_time_trials(self):
        """The number of individual time trials in the stage race"""
        return len(self.individual_time_trials)

    @property
    def rest_days(self):
        """The rest days in the stage race"""
        return [stage for stage in self.stages if isinstance(stage, RestDay)]

    @property
    def number_of_rest_days(self):
        """The number of rest days in the stage race"""
        return len(self.rest_days)

    @property
    def first_stage(self):
        if len(self.stages) == 0:
            raise NoStagesError("Cannot determine first stage when there are no stages")
        return self.stages[0]

    @property
    def last_stage(self):
        if len(self.stages) == 0:
            raise NoStagesError("Cannot determine last stage when there are no stages")
        return self.stages[-1]

    @property
    def start_date(self):
        return self.first_stage.date

    @property
    def end_date(self):
        return self.last_stage.date
    
    @property
    def depart(self):
        return self.first_stage.start

    @property
    def arrive(self):
        return self.last_stage.finish

    @property
    def route(self):
        return '\n'.join(stage.route(self.country) for stage in self.stages)

    @property
    def summit_finishes(self):
        stages = [stage for stage in self.racing_stages if stage.is_summit_finish]
        return len(stages)

    @property
    def stage_summary(self):

        #
        # How many road, team or individual time trials ?
        #
        stage_id_re = re.compile(r'(^\d+$)')
        non_split_stages = [stage for stage in self.racing_stages if stage_id_re.match(stage.id)]
        non_split = len(non_split_stages)

        #
        # How many split stages ?
        #
        split_stage_re = re.compile(r'(^\d+a$)')
        split_stages = [stage for stage in self.racing_stages if split_stage_re.match(stage.id)]
        split = len(split_stages)

        total = non_split + split

        summary = [ '%d stages' % (total) ]
        if self.prologue is not None:
            summary.append("+ Prologue")
        
        if split == 1:
            summary.append("including 1 split stage")
        elif split > 1:
            summary.append('including %d split stages' % (split))
         
        return ' '.join(summary)

class TourDeFrance(StageRace):
    def __init__(self):
        super().__init__("Tour de France", country.France()) 

class ParisNice(StageRace):
    def __init__(self):
        super().__init__("Paris-Nice", country.France()) 

class Dauphine(StageRace):
    def __init__(self):
        super().__init__("Critérium du Dauphiné", country.France()) 

    @property
    def name(self):
        if self.start_date.year < 2010:
            return "Critérium du Dauphiné Libéré"
        else:
            return super().name

class TourOfItaly(StageRace):
    def __init__(self):
        super().__init__("Giro d'Italia", country.Italy()) 

class TirrenoAdriatico(StageRace):
    def __init__(self):
        super().__init__("Tirreno Adriatico", country.Italy()) 

class TourOfSpain(StageRace):
    def __init__(self):
        super().__init__("TourOfSpain a España", country.Spain()) 
