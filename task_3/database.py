from library_item import LibraryItem

class Database:
    def __init__(self, filename="database.txt"):
        self.filename = filename

    def load(self):
        items = []
        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                data = {}

                for field in line.split("|"):
                    key, value = field.split("=", 1)
                    data[key] = value
                item = LibraryItem.from_dict(data)
                items.append(item)
        return items

    def save(self, items):
        with open(self.filename, "w", encoding="utf-8") as file:
            for item in items:
                data = item.to_dict()

                line = "|".join(
                    f"{key}={value}"
                    for key, value in data.items()
                )
                file.write(line + "\n")