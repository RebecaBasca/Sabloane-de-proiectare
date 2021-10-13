
class Author:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"\t{self.name}")

class Chapter:
    def __init__(self,title):
        self.title = title
        self.subchapters = []

    def createSubChapter(self,title):
        newSubChapter = SubChapter(title)
        self.subchapters.append(newSubChapter)
        return len(self.subchapters)-1

    def getSubChapter(self,id):
        return self.subchapters[id]

    def print(self):
        print(f"\tChapter: {self.title}")
        if (not len(self.subchapters)):
            print("\tempty chapter")
            return;

        for item in self.subchapters:
            item.print()

class SubChapter:
    def __init__(self, title):
        self.title = title
        self.content = []

    def createNewParagraph(self,text):
        newParagraph = Paragraph(text)
        self.content.append(newParagraph)

    def createNewImage(self,imageName):
        newImage = Image(imageName)
        self.content.append(newImage)

    def createNewTable(self,title):
        newTable = Table(title)
        self.content.append(newTable)

    def print(self):
        print(f"\tSubChapter: {self.title}")

        if(not len(self.content)):
            print("\tempty subchapter")
            return;

        for item in self.content:
            item.print()

class Image:
    def __init__(self, imageName):
        self.imageName = imageName

    def print(self):
        print(f"\tImage: {self.imageName}")

class Paragraph:
    def __init__(self, text):
        self.text = text

    def print(self):
        print(f"\tParagraph: {self.text}")

class Table:
    def __init__(self, title):
        self.title = title

    def print(self):
        print(f"\tTable: {self.title}")

class TableOfContents:
    def __init__(self):
        self.table = "table"
