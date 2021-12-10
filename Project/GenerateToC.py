from Visitor import Visitor
from TableOfContents import TableOfContents

class GenerateToC(Visitor):
    def __init__(self):
        self.obj = None

    def getToC(self):

        print("Table of contents:")
        print(TableOfContents(self.obj).getToc())