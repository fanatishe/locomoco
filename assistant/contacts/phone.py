import re
from assistant.contacts.field import Field


class Phone(Field):
    """Represents a contact's phone. Has basic validation on add/edit"""

    COUNTRY_CODE = "38"
    NUM_LEN = 10
    NUM_PATTERN = r"[^0-9]+"

    @staticmethod
    def get_num(phone: str) -> str:
        """
        Strips all non-numeric characters from a given string.

        Args:
            phone (str): The raw string containing the phone number.

        Returns:
            str: A string containing strictly the numeric digits.
        """
        return re.sub(rf"{Phone.NUM_PATTERN}", "", phone)

    def __init__(self, phone: str):
        raw_digits = self.get_num(phone)

        # Handle cases where users include the country code (e.g., 380501234567)
        if len(raw_digits) == 12 and raw_digits.startswith(Phone.COUNTRY_CODE):
            raw_digits = raw_digits[2:]

        if len(raw_digits) != Phone.NUM_LEN:
            raise ValueError("Phone must contain exactly 10 digits (e.g., 0501234567).")

        super().__init__(raw_digits)
