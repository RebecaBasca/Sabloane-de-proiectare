
class DocumentManager():
    title = None

    @staticmethod
    def __new__(Book):
        if Book.title is None:
            Book.title = super(DocumentManager, Book).__new__(Book)
        return Book.title

