from assistant.contacts.name import Name
from assistant.contacts.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)

        return f"{self.name.value}: {phones}"
