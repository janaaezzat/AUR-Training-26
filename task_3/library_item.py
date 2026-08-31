from abc import ABC, abstractmethod
from item_status import ItemStatus

class LibraryItem(ABC):
    _type_registry = {}
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        LibraryItem._type_registry[cls.__name__] = cls

    def __init__(self, title):
        self.title = title
        self._status = ItemStatus.AVAILABLE
    @property
    def status(self):
        return self._status
    @abstractmethod
    def loan_period(self):
        pass
    def checkout(self):
        if self._status == ItemStatus.LOST:
            raise ValueError("A lost item cannot be checked out.")
        if self._status == ItemStatus.CHECKED_OUT:
            raise ValueError("Item is already checked out.")
        self._status = ItemStatus.CHECKED_OUT
    def return_item(self):
        if self._status != ItemStatus.CHECKED_OUT:
            raise ValueError("Only checked-out items can be returned.")
        self._status = ItemStatus.AVAILABLE
    def mark_lost(self):
        if self._status == ItemStatus.LOST:
            raise ValueError("Item is already marked as lost.")
        self._status = ItemStatus.LOST
    def __lt__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.title.lower() < other.title.lower()
    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r}, status={self._status.name!r})"
    def __str__(self):
        status_text = self._status.name.replace("_", " ").title()
        return f"{self.title} ({self.__class__.__name__}) — {status_text}"
    @classmethod
    def from_dict(cls, data):
        item_type = data.get("type")
        if item_type not in cls._type_registry:
            cls._load_item_type(item_type)
        if item_type not in cls._type_registry:
            raise ValueError(f"Unknown item type: {item_type}")
        item_class = cls._type_registry[item_type]
        item = item_class._from_dict(data)
        status = data.get("status", "AVAILABLE")
        try:
            status = ItemStatus(status)
        except ValueError:
            raise ValueError(f"Invalid item status: {status}")
        if status == ItemStatus.CHECKED_OUT:
            item.checkout()
        elif status == ItemStatus.LOST:
            item.mark_lost()
        return item
    @staticmethod
    def _load_item_type(item_type):
        import importlib

        module_name = item_type.lower()
        try:
            importlib.import_module(module_name)
        except ModuleNotFoundError:
            pass
    @staticmethod
    def validate_isbn(isbn):
        """Validate an ISBN-13 checksum."""
        isbn = isbn.replace("-", "").replace(" ", "")
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        total = 0
        for i, digit in enumerate(isbn):
            digit = int(digit)
            if i % 2 == 0:
                total += digit
            else:
                total += digit * 3
        return total % 10 == 0
    @abstractmethod
    def to_dict(self):
        pass