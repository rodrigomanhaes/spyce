from __future__ import with_statement
from bowling import Bowling
from spyce import description, example
from should_dsl import should_be

with description(Bowling):
    def setup():
        bowling = Bowling()

    with example("should score 0 for gutter game"):
        bowling.score |should_be| 0
        bowling.hit(1)

    with example("should score 13 if I get a spare with 6 and 7"):
        bowling.score |should_be| 0
        bowling.hit(6)
        bowling.hit(7)
        bowling.score |should_be| 13

    
