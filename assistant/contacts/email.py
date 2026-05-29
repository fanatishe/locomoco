# FILE PATH: assistant/contacts/email.py
import re
from assistant.contacts.field import Field


class Email(Field):
    """Represents a contact's email address"""

    PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def __init__(self, value: str):
        cleaned = value.strip()
        if not re.match(self.PATTERN, cleaned):
            raise ValueError("Incorrect email format (e.g., example@domain.com).")
        super().__init__(cleaned)
