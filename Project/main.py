from Author import Author
from Element import Element
from Section import Section
from Image import Image
from ImageProxy import ImageProxy
from Table import Table
from Paragraph import Paragraph
import time
from AlignStrategy import AlignStrategy
from AlignLeft import AlignLeft
from AlignRight import AlignRight
from DocumentManager import DocumentManager
from Book import Book


if __name__ == "__main__":

    myBook = Book("My Book")
    DocumentManager.__new__(myBook)
    me = Author("Myself")
    myBook.addAuthor(me)



    cap1 = Section("Chapter 1")
    p1 = Paragraph("Paragraph 1")
    p2 = Paragraph("Paragraph 2")
    p3 = Paragraph("Paragraph 3")
    p4 = Paragraph("Paragraph 4")

    cap1.add(p1)
    cap1.add(p2)
    cap1.add(p3)
    cap1.add(p4)

    print("-------Printing without alignment:")
    cap1.print()

    p1.setAlignStrategy(AlignRight())
    p2.setAlignStrategy(AlignLeft())
    p3.setAlignStrategy(AlignRight())
    p4.setAlignStrategy(AlignLeft())

    print("\n-------Printing with alignment:")
    cap1.print()


    print(myBook)

