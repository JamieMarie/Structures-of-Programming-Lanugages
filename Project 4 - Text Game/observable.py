""" Code adapted from http://www.giantflyingsaucer.com/blog/?p=5117 """

class Observable(object):
 
        def __init__(self):    
                self.observers = []
 
        def register(self, observer):
                if not observer in self.observers:
                        self.observers.append(observer)
 
        def unregister(self, observer):
                if observer in self.observers:
                        self.observers.remove(observer)
 
        def unregister_all(self):
                self.observers = []
