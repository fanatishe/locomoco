from datetime import date
from assistant.contacts.field import Field
from assistant.utils.birthday_utils import normalize_date


class Birthday(Field):
    """Represents a contact's birthday. Validates that the date is not in the future."""

    def __init__(self, value: str):
        normalized_value = self.validate_and_normalize(value)
        super().__init__(normalized_value)

    def validate_and_normalize(self, value: str) -> str:
        # normalize_date returns a datetime object.
        normalized_datetime = normalize_date(value)

        # We must extract the date() part before comparing it to date.today()
        if normalized_datetime.date() > date.today():
            raise ValueError("Birthday cannot be in the future.")

        return normalized_datetime.strftime("%d.%m.%Y")
