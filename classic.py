class Classic(object):

    def __init__(self, date, name, start, finish, distance, bergs = None, cotes = None, gravel = None, pave = None):
        self._date = date
        self._name = name
        self._distance = distance
        self._start = start
        self._finish = finish

        #
        # Belgian cobbled classics
        #
        if bergs is None:
            self._bergs = []
        else:
            self._bergs = bergs

        #
        # Non-cobbled classics
        #
        if cotes is None:
            self._cotes = []
        else:
            self._cotes = cotes

        #
        # Strada Bianche, Paris-Tours 2018 onwards
        #
        if gravel is None:
            self._gravel = []
        else:
            self._gravel = gravel

        #
        # Paris-Roubaix and Tour of Flanders
        #
        if pave is None:
            self._pave = []
        else:
            self._pave = pave


    @property
    def date(self):
        return self._date

    @property
    def distance(self):
        return self._distance

    @property
    def name(self):
        return self._name

    @property
    def start(self):
        return self._start

    @property
    def finish(self):
        return self._finish

    @property
    def climbs(self):
        climbs = []
        for km, c in self._cotes:
            dist_to_finish = self.distance - km
            climbs.append('{:0.1f} km,{},{}m'.format(dist_to_finish, c.name, c.height))
        return '\n'.join(climbs)

class ParisRoubaix(Classic):

    @property
    def cobbles(self):
        cobbles = []
        for km, sector_id, p in self._pave:
            dist_to_finish = self.distance - km
            cobbles.append('{},{:0.1f} km,{},{:0.1f} km,{}'.format(sector_id, dist_to_finish, p.name, p.length, str(p.rating)))
        return '\n'.join(cobbles)

class TourOfFlanders(Classic):

    @property
    def climbs(self):
        climbs = []
        for km, berg_id, b in self._bergs:
            dist_to_finish = self.distance - km
            climbs.append('{},{:0.1f} km,{},{} km,{}'.format(berg_id, dist_to_finish, b.name, b.length, str(b.pavement)))
        return '\n'.join(climbs)

    @property
    def cobbles(self):
        cobbles = []
        for km, sector_id, p in self._pave:
            dist_to_finish = self.distance - km
            cobbles.append('{},{:0.1f} km,{},{} km'.format(sector_id, dist_to_finish, p.name, p.length))
        return '\n'.join(cobbles)

class ParisTours(Classic):

    @property
    def gravel(self):
        gravel = []
        for km, sector_id, g in self._gravel:
            dist_to_finish = self.distance - km
            gravel.append('{},{:0.1f} km,{},{} km'.format(sector_id, dist_to_finish, g.name, g.length))
        return '\n'.join(gravel)
