from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __format__(self, format_spec):
        return format(str(self), format_spec)


class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value.strip())


class Phone(Field):
    def __init__(self, value):
        value = value.strip()
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must contain exactly 10 digits")
        super().__init__(value)


class Email(Field):
    def __init__(self, value):
        value = value.strip()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        super().__init__(value)


class Address(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Address cannot be empty")
        super().__init__(value.strip())


class Note(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Note cannot be empty")
        super().__init__(value.strip())


class Birthday(Field):
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, self.DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Birthday must be in format DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(self.DATE_FORMAT)


class ContactCongratulation(Birthday):
    def __init__(self, name, value):
        self.name = name
        super().__init__(value)

    def __str__(self):
        return f"{self.name}: {self.value.strftime(self.DATE_FORMAT)}"
