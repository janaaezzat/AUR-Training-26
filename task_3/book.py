from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title)

        if not LibraryItem.validate_isbn(isbn):
            raise ValueError("Invalid ISBN-13.")

        self.author = author
        self.isbn = isbn

    def loan_period(self):
        return 21

    @classmethod
    def _from_dict(cls, data):
        return cls(data["title"],data["author"],data["isbn"])
    def to_dict(self):
        return {"type": "Book","title": self.title,"author": self.author,"isbn": self.isbn,"status": self.status.name}