# FILE PATH: assistant/contacts/birthday.py
from datetime import date
from assistant.contacts.field import Field
from assistant.utils.birthday_utils import normalize_date


class Birthday(Field):
    def __init__(self, value: str):
        normalized_value = self.validate_and_normalize(value)
        super().__init__(normalized_value)

    def validate_and_normalize(self, value: str) -> str:
        normalized_date = normalize_date(value)
        # Support both formats (YYYY-MM-DD and DD.MM.YYYY ) standardizing to DD.MM.YYYY internal storage
        if normalized_date > date.today():
            raise ValueError("Birthday cannot be in the future.")
        return normalized_date.strftime("%d.%m.%Y")
