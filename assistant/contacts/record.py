from assistant.contacts.address import Address
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.contacts.phone import Phone
from assistant.contacts.note import Note
from assistant.contacts.birthday import Birthday
from assistant.utils.formatters import (
    format_address,
    format_emails,
    format_name,
    format_phones,
)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.emails = []
        self.note = None
        self.birthday = None

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if any(p.value == new_phone.value for p in self.phones):
            raise ValueError(
                f"Phone number '{new_phone.value}' already exists for {self.name.value}."
            )
        self.phones.append(new_phone)

    def set_address(self, address: str):
        self.address = Address(address)

    def set_note(self, note: str):
        self.note = Note(note)

    def add_email(self, email: str):
        new_email = Email(email)
        if any(e.value.lower() == new_email.value.lower() for e in self.emails):
            raise ValueError(
                f"Email '{new_email.value}' already exists for {self.name.value}."
            )
        self.emails.append(new_email)

    def set_birthday(self, birthday_str: str):
        # Even if Birthday class is a basic Field container right now,
        # it will contain the clean 'DD.MM.YYYY' string.
        self.birthday = Birthday(birthday_str)

    def to_dict(self) -> dict:
        """Return all contact fields as a display-ready dict for formatters."""
        return {
            "Name": format_name(self.name),
            "Phones": format_phones(self.phones),
            "Address": format_address(self.address),
            "Emails": format_emails(self.emails),
            "Birthday": str(self.birthday) if self.birthday else "-",
        }

    def __str__(self):
        phones = "; ".join(str(p) for p in self.phones)
        return f"{self.name.value}: {phones}"
