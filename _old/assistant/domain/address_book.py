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
        ...

    def save(self) -> None:
        ...

    def add_record(self, record: Record) -> None:
        ...

    def find(self, name: str) -> Record | None:
        ...

    def delete(self, name: str) -> None:
        ...

    def get_upcoming_birthdays(
        self, from_date: date | None = None
    ) -> list[ContactCongratulation]:
        ...

    def show_upcoming_birthdays(self) -> None:
        ...

    def __str__(self):
        ...
