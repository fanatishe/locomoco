from assistant.contacts.address import Address
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.contacts.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.emails = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def set_address(self, address: str):
        self.address = Address(address)

    def add_email(self, email: str):
        self.emails.append(Email(email))

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"{self.name.value}: {phones}"
