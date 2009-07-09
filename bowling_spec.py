from bowling import Bowling
from spyce import description, it

with description(Bowling) as context:
    
    with example("should score 0 for gutter game") as another_context:
        another_context.foo |should_be| bar
    
    with example("2"):
        pass

