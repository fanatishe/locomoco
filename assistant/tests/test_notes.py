import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from assistant.contacts.book import Book
from assistant.handlers.note_handlers import (
    note_add,
    note_change,
    note_delete,
    note_search,
    note_tag_add,
    note_tag_search,
    note_tag_sort,
)


def build_book():
    book = Book()
    print("--- Adding Notes ---")
    print(note_add(["Buy", "milk", "and", "bread"], book))
    print(note_add(["Call", "the", "doctor", "tomorrow"], book))
    return book


def test_note_operations():
    print("\n=== Note Operations ===")
    book = build_book()

    print("\n--- Change Note 1 ---")
    print(note_change(["1", "Buy", "milk,", "bread,", "and", "eggs"], book))

    print("\n--- Search Note 'bread' ---")
    # In CLI, args are lists of strings.
    print(note_search(["bread"], book))

    print("\n--- Add Tags ---")
    print(note_tag_add(["1", "groceries"], book))
    print(note_tag_add(["2", "urgent"], book))
    print(note_tag_add(["2", "health"], book))

    print("\n--- Search Tag 'urgent' ---")
    print(note_tag_search(["urgent"], book))

    print("\n--- Sort by Tag ---")
    print(note_tag_sort([], book))

    print("\n--- Delete Note 2 ---")
    print(note_delete(["2"], book))

    print("\n--- Verify Deletion (Show All) ---")
    # note_search with empty args returns all notes
    print(note_search([], book))


if __name__ == "__main__":
    test_note_operations()
