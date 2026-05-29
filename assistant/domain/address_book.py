

from collections import UserDict
from datetime import date

from .fields import ContactCongratulation
from .record import Record
from ..storage.base import StorageStrategy


class AddressBook(UserDict[str, Record]):
    def __init__(self, storage: StorageStrategy):
        super().__init__()
        self._storage = storage

    def load(self) -> None:
        self.data = self._storage.load()

    def save(self) -> None:
        self._storage.save(self.data)

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name not in self.data:
            raise KeyError("Contact not found")

        del self.data[name]

    def get_upcoming_birthdays(
            self, from_date: date | None = None
    ) -> list[ContactCongratulation]:
        return []

    def show_upcoming_birthdays(self) -> None:
        birthdays = self.get_upcoming_birthdays()

        if not birthdays:
            print("No upcoming birthdays.")
            return

        for birthday in birthdays:
            print(birthday)

    def __str__(self):
        if not self.data:
            return "Address book is empty."

        return "\n".join(str(record) for record in self.data.values())
