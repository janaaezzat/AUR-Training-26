from library_item import LibraryItem
from item_status import ItemStatus

class Library:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added.")
        self.items.append(item)

    def checkout(self, title):
        item = self.find_by_title(title)
        if item is None:
            raise ValueError(f"No item found with title: {title}")
        item.checkout()
        return item

    def return_item(self, title):
        item = self.find_by_title(title)
        if item is None:
            raise ValueError(f"No item found with title: {title}")
        item.return_item()
        return item

    def find_by_title(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None

    def list_available(self):
        return [
            item for item in self.items
            if item.status == ItemStatus.AVAILABLE
            ]

    def remove_item(self, title):
        item = self.find_by_title(title)
        if item is None:
            raise ValueError(f"No item found with title: {title}")
        self.items.remove(item)
        return item