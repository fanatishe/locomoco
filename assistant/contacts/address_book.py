from collections import UserDict
from .record import Record


class AddressBook(UserDict[str, Record]):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
