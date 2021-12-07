import abc

class AlignStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod

    def render(self, paragraph):
        pass