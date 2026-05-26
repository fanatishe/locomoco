from .field import Field
from re import match, IGNORECASE

class Email(Field):
    PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    def __init__(self, value):
        is_valid = self.validate(value)
        if not is_valid:
            raise ValueError("Incorrect email")
        super().__init__(value)

    def validate(self, email: str) -> bool:
        return match(Email.PATTERN, email, IGNORECASE)