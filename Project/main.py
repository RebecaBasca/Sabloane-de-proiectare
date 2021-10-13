

class Book:
    book_content = []

    def __init__(self, title):
        self.title = title

    def createNewParagraph(self, paragraph):
        self.book_content.append(paragraph)

    def createNewImage(self, image):
        self.book_content.append(image)

    def createNewTable(self, table):
        self.book_content.append(table)

    def print(self):
        print("Book",self.title, ":")
        for items in self.book_content:
            print(items)



if __name__ == '__main__':
    book = Book("Disco Titanic")
    book.createNewParagraph("Paragraph 1")
    book.createNewParagraph("Paragraph 2")
    book.createNewParagraph("Paragraph 3")
    book.createNewImage("Image 1")
    book.createNewParagraph("Paragraph 4")
    book.createNewTable("Table 1")

    book.print()


