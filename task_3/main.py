from book import Book
from database import Database
from dvd import DVD
from library import Library
from magazine import Magazine


def display_items(title, items):
    print(f"\n{title}")
    print("-" * len(title))

    for item in items:
        print(item)


def main():
    database = Database()
    library = Library(database.load())

    # Display all items
    display_items("All Library Items", library.items)

    # Display available items
    display_items("Available Items", library.list_available())

    # Find an item
    print("\nFinding 'Dune':")
    print(library.find_by_title("Dune"))

    # Demonstrate sorting
    print("\nItems Sorted Alphabetically:")
    display_items("Sorted Items", sorted(library.items))

    # Checkout an item
    print("\nChecking out Dune:")
    print(library.checkout("Dune"))

    print("\nReturning Dune:")
    print(library.return_item("Dune"))

    print("\nMarking Dune as lost:")
    dune = library.find_by_title("Dune")
    dune.mark_lost()
    print(dune)

    print("\nAdding a new book:")
    new_book = Book(
        "Clean Code",
        "Robert C. Martin",
        "9780132350884"
    )
    library.add_item(new_book)
    print(new_book)

    print("\nAdding a new DVD:")
    new_dvd = DVD(
        "The Dark Knight",
        "Christopher Nolan"
    )
    library.add_item(new_dvd)
    print(new_dvd)
    print("\nAdding a new magazine:")
    new_magazine = Magazine(
        "Science",
        "2026-09"
    )
    library.add_item(new_magazine)
    print(new_magazine)
  #  database.save(library.items)
    print("\nLibrary saved successfully.")
if __name__ == "__main__":
    main()