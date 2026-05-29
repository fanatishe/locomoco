from collections import UserDict
from .record import Record


class AddressBook(UserDict[str, Record]):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)


class Notebook(UserDict):
    """Holds standalone text notes separate from contacts."""

    def __init__(self):
        super().__init__()
        self.current_id = 1

    def add_note(self, text: str) -> int:
        note_id = self.current_id
        self.data[note_id] = {"text": text, "tags": []}
        self.current_id += 1
        return note_id


class Book:
    """The root application state object unifying both sub-stores."""

    def __init__(self):
        self.addressbook = AddressBook()
        self.notebook = Notebook()
