from assistant.contacts.address import Address
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.contacts.phone import Phone
from assistant.contacts.birthday import Birthday
from assistant.utils.formatters import (
    format_address,
    format_emails,
    format_name,
    format_phones,
)


class Record:
    """
    Represents a single contact profile, holding their name, phones, emails,
    physical address, and birthday.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.emails = []
        self.note = None
        self.birthday = None

    def add_phone(self, phone: str) -> None:
        """
        Validates and adds a new phone number to the contact.

        Args:
            phone (str): The raw string phone number.

        Raises:
            ValueError: If the phone number is a duplicate or fails formatting rules.
        """
        new_phone = Phone(phone)
        if any(p.value == new_phone.value for p in self.phones):
            raise ValueError(
                f"Phone number '{new_phone.value}' already exists for {self.name.value}."
            )
        self.phones.append(new_phone)

    def set_address(self, address: str) -> None:
        """
        Validates and sets the physical address of the contact.

        Args:
            address (str): The full physical address string.
        """
        self.address = Address(address)

    def add_email(self, email: str) -> None:
        """
        Validates and adds a new email address to the contact.

        Args:
            email (str): The raw string email address.

        Raises:
            ValueError: If the email already exists or fails formatting rules.
        """
        new_email = Email(email)
        if any(e.value.lower() == new_email.value.lower() for e in self.emails):
            raise ValueError(
                f"Email '{new_email.value}' already exists for {self.name.value}."
            )
        self.emails.append(new_email)

    def set_birthday(self, birthday_str: str) -> None:
        """
        Validates and sets the birthday of the contact.

        Args:
            birthday_str (str): The string representation of the birthday (e.g., 'DD.MM.YYYY').
        """
        # Even if Birthday class is a basic Field container right now,
        # it will contain the clean 'DD.MM.YYYY' string.
        self.birthday = Birthday(birthday_str)

    def to_dict(self) -> dict:
        """
        Serializes all contact fields into a display-ready dictionary.

        Returns:
            dict: A dictionary mapping field names (e.g., 'Phones') to their
                  formatted string representations.
        """
        return {
            "Name": format_name(self.name),
            "Phones": format_phones(self.phones),
            "Address": format_address(self.address),
            "Emails": format_emails(self.emails),
            "Birthday": str(self.birthday) if self.birthday else "-",
        }

    def __str__(self) -> str:
        """
        Returns a concise string representation of the contact and their phone numbers.

        Returns:
            str: A formatted string containing the contact's name and phones.
        """
        phones = "; ".join(str(p) for p in self.phones)
        return f"{self.name.value}: {phones}"
