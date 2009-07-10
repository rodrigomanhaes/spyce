class Bowling(object):
    _score = 0

    @property
    def score(self):
        return self._score

    def hit(self, number_of_pins):
        self._score += number_of_pins
