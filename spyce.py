# SUT: Context
import sys

class Spec(object):
    def __enter__(self):
        frame = sys._getframe(1)
        frame_locals, frame_globals = frame.f_locals, frame.f_globals
        self.context = frame_locals.get('context', None) or \
                       frame_globals.get('context', None)

        if self.context:
            self.context.add_sub_context(self)

        return self
        
    def __exit__(self, type, value, error):
        pass


class description(Spec):
    def __init__(self, klass):
        self._name = klass.__name__
        self._sub_contexts = []

    def __exit__(self, type, value, error):
        print self._name + ':'
        self._print_sub_contexts()
    
    def add_sub_context(self, sub_context):
        self._sub_contexts.append(sub_context)

    def _print_sub_contexts(self):
        for sub_context in self._sub_contexts:
            print ' - ' + sub_context.description
    
class example(Spec):
    def __init__(self, textual_description):
        self.description = textual_description
