from Visitor import Visitor

class RenderContentVisitor(Visitor):
    def __init__(self):
        self.obj = None

    def renderContent(self):
        for elem in self.obj._children:
            elem.print()