import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from assistant.contacts.book import Book
from assistant.handlers.contact_handlers import contact_add
from assistant.handlers.note_handlers import note_add
from assistant.storage.pickle_storage import save_data, load_data, STORAGE_DIR

# We use a custom filename so we don't overwrite your actual saved assistant data!
TEST_FILENAME = "test_data_dump.pkl"


def test_save_and_load():
    print("\n=== Storage Operations ===")

    # 1. Create a fresh Book and populate it
    original_book = Book()
    contact_add(["Alice", "0501234567"], original_book)
    note_add(["Test", "note", "for", "storage"], original_book)

    print("--- Original Data ---")
    print(f"Contacts Keys: {list(original_book.addressbook.data.keys())}")
    print(f"Notes Keys: {list(original_book.notebook.data.keys())}")

    # 2. Save data to the test file
    print(f"\nSaving to {TEST_FILENAME}...")
    save_data(original_book, TEST_FILENAME)

    # 3. Load data into a completely new Book instance to simulate a restart
    print("Loading data into a new Book instance...")
    restored_book = load_data(TEST_FILENAME)

    print("\n--- Restored Data ---")
    # Verify that the loaded data matches what we originally added
    print(f"Contacts Keys: {list(restored_book.addressbook.data.keys())}")
    print(f"Notes Keys: {list(restored_book.notebook.data.keys())}")

    # 4. Clean up the test file so we leave no trace behind
    test_file_path = STORAGE_DIR / TEST_FILENAME
    if test_file_path.exists():
        os.remove(test_file_path)
        print(f"\n[Success] Cleaned up test file: {test_file_path}")


if __name__ == "__main__":
    test_save_and_load()
