
from Element import *

class Visitor(metaclass=abc.ABCMeta):
    def visit(self, obj):
        self.obj = obj;
