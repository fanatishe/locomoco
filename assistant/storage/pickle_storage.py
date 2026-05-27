from assistant.contacts.address_book import AddressBook
from pathlib import Path
import pickle


def save_data(book, filename_str: str = "addressbook.pkl") -> None:
    """
    Зберігає AddressBook у файл.
    """
    filename = Path(__file__).parent.parent / "data" / filename_str
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename_str: str = "addressbook.pkl") -> AddressBook:
    """
    Завантажує AddressBook з файлу.
    Якщо файлу немає — створює нову книгу.
    """
    try:
        filename = Path(__file__).parent.parent / "data" / filename_str
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
