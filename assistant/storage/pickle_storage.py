from assistant.contacts.address_book import Book
from pathlib import Path
import pickle
import os


def save_data(book: Book, filename_str: str = "assistant_data.pkl") -> None:
    """Saves the unified Book object into a single file."""
    filename = Path(__file__).parent.parent / "data" / filename_str
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename_str: str = "assistant_data.pkl") -> Book:
    """Loads Book from file. If file doesn't exist, initializes a fresh unified Book."""
    try:
        if not (Path(__file__).parent.parent / "data").exists():
            os.mkdir(Path(__file__).parent.parent / "data")
        filename = Path(__file__).parent.parent / "data" / filename_str
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, pickle.UnpicklingError, EOFError):
        return Book()
