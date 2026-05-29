import pickle
from pathlib import Path
from assistant.contacts.address_book import Book

# Using Path.home() ensures the file is saved in the user's home directory
# (e.g., C:\Users\Username or /home/username) fulfilling the project requirement.
STORAGE_DIR = Path.home() / ".personal_assistant"
STORAGE_FILE = "assistant_data.pkl"


def save_data(book: Book, filename_str: str = STORAGE_FILE) -> None:
    """
    Serializes and saves the application state (Book) to the user's home directory.

    Args:
        book (Book): The root state object containing AddressBook and Notebook.
        filename_str (str): The name of the file to save data into.
    """
    if not STORAGE_DIR.exists():
        STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    file_path = STORAGE_DIR / filename_str
    with open(file_path, "wb") as f:
        pickle.dump(book, f)


def load_data(filename_str: str = STORAGE_FILE) -> Book:
    """
    Loads the application state (Book) from the user's home directory.
    If the file or directory does not exist, or the file is corrupted,
    it returns a fresh, empty Book instance.

    Args:
        filename_str (str): The name of the file to load data from.

    Returns:
        Book: The populated application state, or a new instance if loading fails.
    """
    file_path = STORAGE_DIR / filename_str

    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, pickle.UnpicklingError, EOFError):
        # Graceful fallback: return a fresh book if no history exists
        return Book()
