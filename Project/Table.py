from Element import Element

class Table(Element):
    def __init__(self, content):
        self.link = content

    def add(self, item):
        pass;

    def remove(self, item):
        pass;

    def print(self):
        print("Table:",self.content)
