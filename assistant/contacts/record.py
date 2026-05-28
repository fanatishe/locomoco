from assistant.contacts.address import Address
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.contacts.phone import Phone
from assistant.contacts.note import Note
from assistant.utils.formatters import format_address, format_emails, format_name, format_phones


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.emails = []
        self.note = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def set_address(self, address: str):
        self.address = Address(address)

    def set_note(self, note: str):
        self.note = Note(note)

    def add_email(self, email: str):
        self.emails.append(Email(email))

    def to_dict(self) -> dict:
        """Return all contact fields as a display-ready dict for formatters."""
        return {
            "Name": format_name(self.name),
            "Phones": format_phones(self.phones),
            "Address": format_address(self.address),
            "Emails": format_emails(self.emails),
            "Note": str(self.note) if self.note else "-",
        }

    def __str__(self):
        phones = "; ".join(str(p) for p in self.phones)
        return f"{self.name.value}: {phones}"
