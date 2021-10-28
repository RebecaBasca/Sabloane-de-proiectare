from Author import Author
from Section import Section
from Image import Image
from Paragraph import Paragraph
from Book import Book

if __name__ == "__main__":
    book = Book("Noapte buna copii!")
    author = Author("Radu Pavel Gheo")

    book.addAuthor(author)

    cap1 = Section("Capitolul 1")
    cap11 = Section("Capitolul 1.1")
    cap111 = Section("Capitolul 1.1.1")
    cap1111 = Section("Subchapter 1.1.1.1")
    book.add(Paragraph("Multumesc celor care..."))
    book.add(cap1)
    cap1.add(Paragraph("Moto capitol"))
    cap1.add(cap11)
    cap11.add(Paragraph("Text from chapter 1.1"))
    cap11.add(cap111)
    cap111.add(Paragraph("Text from subchapter 1.1.1"))
    cap111.add(cap1111)
    cap1111.add(Image("Image from subchapter 1.1.1.1"))


    book.print()