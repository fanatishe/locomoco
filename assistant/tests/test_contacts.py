import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from assistant.contacts.address_book import Book
from assistant.handlers.contact_handlers import (
    contact_add,
    contact_search,
    show_all,
)


def build_book():
    book = Book()

    contact_add(["Alice", "1234567890"], book)
    contact_add(["Alice", "0987654321"], book)

    book.addressbook.find("Alice").set_address("Kyiv, Khreshchatyk 1")
    book.addressbook.find("Alice").add_email("alice@example.com")
    book.addressbook.find("Alice").add_email("alice.work@company.com")

    contact_add(["Bob", "5555555555"], book)
    book.addressbook.find("Bob").add_email("bob@gmail.com")

    contact_add(["Charlie", "1111111111"], book)

    return book


def test_show_contact():
    print("\n=== show_contact (Alice) ===")
    book = build_book()
    print(contact_search(["Alice"], book))


def test_show_contact_not_found():
    print("\n=== show_contact - not found ===")
    book = build_book()
    print(contact_search(["Unknown"], book))


def test_show_all():
    print("\n=== show_all (table) ===")
    book = build_book()
    print(show_all([], book))


def test_show_all_empty():
    print("\n=== show_all - empty book ===")
    book = Book()
    print(show_all([], book))


def test_invalid_email():
    print("\n=== invalid email ===")
    book = build_book()
    book.addressbook.find("Alice").add_email("not-an-email")


def test_search_contact():
    print("\n=== search contact ===")
    book = build_book()

    print(book.addressbook.find("Alice"))
    print(book.addressbook.find("1234567890"))


if __name__ == "__main__":
    try:
        test_show_contact()
        test_show_contact_not_found()
        test_show_all()
        test_show_all_empty()
        test_invalid_email()
        test_search_contact()
    except ValueError as e:
        print(f"Error caught: {e}")
