from Element import Element
from AlignStrategy import AlignStrategy
from AlignLeft import AlignLeft
from AlignRight import AlignRight

class Paragraph(Element):
    def __init__(self,content):
        self.content = content
        self.alignmentStrategy = AlignLeft()

    def add(self, item):
        pass;

    def remove(self, item):
        pass;

    def print(self):
        print("Paragraph:", self.alignmentStrategy.render(self.content))

    def setAlignStrategy(self, strategy):
        self.alignmentStrategy = strategy