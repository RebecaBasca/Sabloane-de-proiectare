from elements import *

class Book:
    def __init__(self,title):
        self.title = title
        self.authors = []
        self.chapters = []
        self.tableOfContents = TableOfContents()


    def addAuthor(self,name):
        self.authors.append(name)

    def createChapter(self,title):
        newChapter = Chapter(title)
        self.chapters.append(newChapter)
        return len(self.chapters)-1

    def getChapter(self,id):
        return self.chapters[id]


    def print(self):
        print(f"Book: {self.title}")
        print("Authors:")
        if(not len(self.authors)):
            print("unknown")
        else:
            for author in self.authors:
                author.print()

        print("Content:")

        if (not len(self.chapters)):
            print("empty book")
            return

        for item in self.chapters:
            item.print()




if __name__ == "__main__":
    book = Book("Disco Titanic")
    author = Author("Radu Pavel")

    book.addAuthor(author)
    indexChapterOne = book.createChapter("Chapter One")

    chp1 = book.getChapter(indexChapterOne)

    indexSubchapterOneOne = chp1.createSubChapter("Subchapter 1.1")

    subChapterOneOne = chp1.getSubChapter(indexSubchapterOneOne)

    subChapterOneOne.createNewParagraph("Paragraph 1")
    subChapterOneOne.createNewParagraph("Paragraph 2")
    subChapterOneOne.createNewParagraph("Paragraph 3")
    subChapterOneOne.createNewImage("Image 1")
    subChapterOneOne.createNewParagraph("Paragraph 4")
    subChapterOneOne.createNewTable("Table 1")

    book.print()
