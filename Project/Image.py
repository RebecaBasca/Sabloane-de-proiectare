from Element import Element

class Image(Element):
    def __init__(self, link):
        self.link = link

    def add(self, item):
        pass;

    def remove(self, item):
        pass;

    def print(self):
        print("Image:",self.link)