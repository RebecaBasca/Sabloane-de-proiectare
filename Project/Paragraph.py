from Element import Element

class Paragraph(Element):
    def __init__(self,content):
        self.content = content

    def add(self, item):
        pass;

    def remove(self, item):
        pass;

    def print(self):
        print("Paragraph:",self.content)