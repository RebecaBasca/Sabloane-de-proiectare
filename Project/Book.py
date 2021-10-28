from Section import Section

class Book(Section):
    def __init__(self,title):
        Section.__init__(self,title)
        self.authors = []

    def add(self, item):
        self._children.append(item)

    def remove(self, item):
        self._children.remove(item)

    def addAuthor(self,name):
        self.authors.append(name)

    def print(self):
        print(f"Book: {self.title}")
        print("\nAuthor(s):")
        for author in self.authors:
            author.print()
        print()
        for child in self._children:
            child.print()
