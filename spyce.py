# SUT: Context

class Spec(object):
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, error):
        pass


class description(Spec):
    def __init__(self, klass):
        self._name = klass.__name__

    def __exit__(self, type, value, error):
        print self._name + ':'
        self._print_sub_contexts()
    
    def _print_sub_contexts(self):
        print ' - should score 0 for gutter game'

    
class example(Spec):
    def __init__(self, textual_description):
        pass
