from assistant.contacts.address_book import AddressBook
from assistant.handlers.contact_handlers import add_contact, show_contact, show_all


def build_book():
    book = AddressBook()

    add_contact(["Alice", "1234567890"], book)
    add_contact(["Alice", "0987654321"], book)
    book.find("Alice").set_address("Kyiv, Khreshchatyk 1")
    book.find("Alice").add_email("alice@example.com")
    book.find("Alice").add_email("alice.work@company.com")

    add_contact(["Bob", "5555555555"], book)
    book.find("Bob").add_email("bob@gmail.com")

    add_contact(["Charlie", "1111111111"], book)

    return book


def test_show_contact():
    print("\n=== show_contact (Alice) ===")
    book = build_book()
    print(show_contact(["Alice"], book))


def test_show_contact_not_found():
    print("\n=== show_contact - not found ===")
    book = build_book()
    print(show_contact(["Unknown"], book))


def test_show_all():
    print("\n=== show_all (table) ===")
    book = build_book()
    print(show_all([], book))


def test_show_all_empty():
    print("\n=== show_all - empty book ===")
    book = AddressBook()
    print(show_all([], book))


def test_invalid_email():
    print("\n=== invalid email ===")
    book = build_book()
    try:
        book.find("Alice").add_email("not-an-email")
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    test_show_contact()
    test_show_contact_not_found()
    test_show_all()
    test_show_all_empty()
    test_invalid_email()
