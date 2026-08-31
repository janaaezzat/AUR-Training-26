from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue

    def loan_period(self):
        return 14

    @classmethod
    def _from_dict(cls, data):
        return cls(data["title"],data["issue"])
    def to_dict(self):
        return {"type": "Magazine","title": self.title,"issue": self.issue,"status": self.status.name}