from __future__ import with_statement
from bowling import Bowling
from spyce import description, example
from should_dsl import should_be

with description(Bowling):
    bowling = Bowling()

    with example("should score 0 for gutter game"):
        bowling.score |should_be| 0

