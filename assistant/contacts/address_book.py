from collections import UserDict
from datetime import datetime, timedelta

from assistant.utils.birthday_utils import birthday_in_year
from .record import Record


class AddressBook(UserDict[str, Record]):
    """
    Stores and manages contact records. Inherits from UserDict, meaning
    the actual contact data is stored in the `self.data` dictionary.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a new Record to the address book using the contact's name as the key.

        Args:
            record (Record): The completely formed contact record to store.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """
        Retrieves a Record by its exact name.

        Args:
            name (str): The name of the contact to find.

        Returns:
            Record | None: The matched Record object, or None if it doesn't exist.
        """
        return self.data.get(name)

    def get_upcoming_birthdays(self, days: int) -> list[Record]:
        """
        Calculates which contacts have a birthday coming up within a specified number of days.

        Args:
            days (int): The forward-looking time window in days.

        Returns:
            list[Record]: A list of records whose birthdays fall within the window.
        """
        upcoming = []
        today = datetime.now().date()
        target_date = today + timedelta(days=days)

        for record in self.data.values():
            if not record.birthday:
                continue

            # Extract day and month from the normalized string format DD.MM.YYYY
            b_day, b_month, _ = map(int, record.birthday.value.split("."))

            # Build this year's birthday; roll over to next year if already passed
            birthday_this_year = birthday_in_year(today.year, b_month, b_day)
            if birthday_this_year < today:
                birthday_this_year = birthday_in_year(today.year + 1, b_month, b_day)

            # Check if the adjusted birthday falls within the requested time frame
            if today <= birthday_this_year <= target_date:
                upcoming.append(record)

        return upcoming


class Notebook(UserDict):
    """
    Holds standalone text notes separate from contacts, utilizing an auto-incrementing ID.
    """

    def __init__(self):
        super().__init__()
        self.current_id = 1

    def add_note(self, text: str) -> int:
        """
        Creates a new note with a unique integer ID.

        Args:
            text (str): The body text of the note.

        Returns:
            int: The unique identifier assigned to the note.
        """
        note_id = self.current_id
        self.data[note_id] = {"text": text, "tags": []}
        self.current_id += 1
        return note_id


class Book:
    """
    The root application state object unifying both sub-stores (AddressBook and Notebook).
    This single object is what gets pickled and saved to the hard drive.
    """

    def __init__(self):
        self.addressbook = AddressBook()
        self.notebook = Notebook()
