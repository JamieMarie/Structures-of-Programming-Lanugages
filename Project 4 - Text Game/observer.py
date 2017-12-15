""" Code adapted from http://www.giantflyingsaucer.com/blog/?p=5117 """

from abc import ABCMeta, abstractmethod

class Observer(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def update(self):
                pass
