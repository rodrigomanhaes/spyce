# SUT: Context
import inspect
import sys

class description(object):
    def __init__(self, klass):
        self._name = klass.__name__
        self._sub_contexts = []

    def __enter__(self):
        frame = sys._getframe(1)
        frame.f_locals['context'] = self

        return self

    def __exit__(self, type, value, error):
        print self._name + ':'
        self._print_sub_contexts()
    
    def add_sub_context(self, sub_context):
        self._sub_contexts.append(sub_context)

    def _print_sub_contexts(self):
        for sub_context in self._sub_contexts:
            print ' - ' + sub_context.description
    

class example(object):
    def __init__(self, textual_description):
        self.description = textual_description
        self.frame = None

    def __enter__(self):
        self.frame = frame = sys._getframe(1)
        frame_locals, frame_globals = frame.f_locals, frame.f_globals
        self.context = frame_locals.get('context', None) or \
                       frame_globals.get('context', None)

        if self.context is None:
            raise Exception('Each example must have a description context!')
        
        self.context.add_sub_context(self)

        setup_method = frame.f_locals.get('setup', None)
        if setup_method:
#            src = "%s%s\n    %s%s;%s" % (
#                        ' '*8,
#                        inspect.getsource(setup_method), 
#                        ' '*8,
#                        "self_frame = sys._getframe()", 
#                        "frame.f_locals.update(self_frame.f_locals)")
            src = """
def setup():
    bowling = Bowling()
    self_frame = sys._getframe() 
    frame.f_locals.update(self_frame.f_locals)
"""
            tudo = locals()
            tudo.update(globals())
            tudo.update(frame.f_globals)
            exec src in tudo
            setup()

        return self
        
    def __exit__(self, type, value, error):
        teardown_method = self.frame.f_locals.get('tear_down', None)
        if teardown_method:
            teardown_method()
