from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def loan_period(self):
        return 5

    @classmethod
    def _from_dict(cls, data):
        return cls(data["title"],data["director"])
    def to_dict(self):
        return {"type": "DVD","title": self.title,"director": self.director,"status": self.status.name}