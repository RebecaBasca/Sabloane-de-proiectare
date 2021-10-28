from Element import Element

class Section(Element):
    def __init__(self,title):
        self.title = title
        self._children = []

    def add(self, item):
        self._children.append(item)

    def remove(self, component):
        self._children.remove(item)

    def print(self):
        print(self.title)
        for child in self._children:
            child.print()




