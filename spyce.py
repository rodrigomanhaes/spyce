# SUT: Context

from should_dsl import *

class Spec(object):
    def __enter__(self):
        print('setup')
        return self
        
    def __exit__(self, type, value, error):
        print('teardown')


class description(Spec):
    def __init__(self, klass):
        pass
    
class example(Spec):
    def __init__(self, textual_description):
        pass