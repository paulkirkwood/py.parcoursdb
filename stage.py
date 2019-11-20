from datetime import datetime

class Stage(object):

   def __init__(self,date):
       self._date = date

   @property
   def date(self):
       return self._date

   @property
   def day_and_date(self):
       return format(self.date, '%-e %B')

class RacingStage(Stage):

    def __init__(self,date,id,start,finish,distance,cols = None):
        super().__init__(date)
        self._id = id
        self._start = start
        self._finish = finish
        self._distance = distance
        if cols is None:
            self._cols = {}
        else:
            self._cols = cols

    def __eq__(self, other):
        return self.date == other.date and self.id == other.id and self.start == other.start and self.finish == other.finish and self.distance == other.distance

    @property
    def id(self):
        return self._id

    @property
    def start(self):
        return self._start

    @property
    def finish(self):
        return self._finish

    @property
    def distance(self):
        return self._distance

    @property
    def cols(self):
        return self._cols

    @property
    def stage_kilometres(self):
        return '%.1f km' % (self.distance)

    def from_to(self,country):
        if self.start == self.finish:
            return self.start.qualified_location(country)
        else:
            return '%s to %s' % (self.start.qualified_location(country), self.finish.qualified_location(country))

    def route(self,country):
        return '%s,%s,%s,%s,%s' % (self.id, self.day_and_date, self.from_to(country), self.stage_kilometres, self.description)

    @property
    def is_summit_finish(self):
        if len(self.cols) == 0:
            return False
        else:
            summits = sorted(self.cols.keys(), reverse=True)
            return summits[0] == self.distance

class RoadStage(RacingStage):

    @property
    def description(self):
        return "Road stage"

    def __repr__(self):
        return 'RoadStage(%r, %r, %r, %r, %r)' % (self.date, self.id, self.start, self.finish, self.distance)

class Criterium(RoadStage):
    def __init__(self,date,id,start_finish,distance,cols = None):
        super().__init__(date, id, start_finish, start_finish, distance, cols)
  
class TeamTimeTrial(RacingStage):

    @property
    def description(self):
        return "Team time trial"

    def __repr__(self):
        return 'TeamTimeTrial(%r, %r, %r, %r, %r)' % (self.date, self.id, self.start, self.finish, self.distance)

class ThreeManTeamTimeTrial(TeamTimeTrial):

    @property
    def description(self):
        return "Three man team time trial"

    def __repr__(self):
        return 'ThreeTeamTimeTrial(%r, %r, %r, %r, %r)' % (self.date, self.id, self.start, self.finish, self.distance)

class IndividualTimeTrial(RacingStage):

    @property
    def description(self):
        return "Individual time trial"

    def __repr__(self):
        return 'IndividualTimeTrial(%r, %r, %r, %r, %r)' % (self.date, self.id, self.start, self.finish, self.distance)

class Prologue(RacingStage):
    def __init__(self,date,start,finish,distance):
        super().__init__(date, "P", start, finish, distance)

    @property
    def description(self):
        return "Individual time trial"

    def __repr__(self):
      return 'Prologue(%r, %r, %r, %r)' % (self.date, self.start, self.finish, self.distance)

class PrologueTeamTimeTrial(Prologue):

    @property
    def description(self):
        return "Team time trial"

    def __repr__(self):
      return 'PrologueTeamTimeTrial(%r, %r, %r, %r)' % (self.date, self.start, self.finish, self.distance)

class PrologueTwoManTeamTimeTrial(PrologueTeamTimeTrial):

    @property
    def description(self):
        return "Two man team time trial"

    def __repr__(self):
      return 'PrologueTwoManTeamTimeTrial(%r, %r, %r, %r)' % (self.date, self.start, self.finish, self.distance)

class RestDay(Stage):

    def __init__(self,date,location = None):
        super().__init__(date)
        self._location = location

    def __repr__(self):
        if location is None:
            return 'RestDay(%r)' % (self.date)
        else:
            return 'RestDay(%r, %r)' % (self.date, self.location)

    @property
    def location(self):
        return self._location

    @property
    def description(self):
        return "Rest day"

    def route(self,country):
        if self.location is None:
            return ',%s,%s' % (self.day_and_date, self.description)
        else:
            return ',%s,%s,%s' % (self.day_and_date, self.description, self.location.qualified_location(country))
