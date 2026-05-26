from datetime import date, timedelta
from re import sub

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __format__(self, format_spec):
        return format(self.value, format_spec)


class Name(Field):
    ...

class Phone(Field):
    FORMATTED_LEN = 19
    COUNTRY_CODE = "+38"
    NUM_LEN = 10
    NUM_PATTERN = r"[^0-9]+"

    def __init__(self, phone):
        if not self.validate(phone):
            raise ValueError("Incorrect phone format")
        
        formated_phone = self.format(phone)
        super().__init__(formated_phone)

    def _get_num (self):
        return sub(Phone.NUM_PATTERN,"", self.phone)
    
    def format(self):
        number = self._get_num()
        without_code = number[-10:]
        operator_code = without_code[0:3]

        part_1 = without_code[3:6]
        part_2 = without_code[6:8]
        part_3 = without_code[8:]

        formatted = f"{Phone.COUNTRY_CODE} ({operator_code}) {part_1}-{part_2}-{part_3}"
        return formatted

    def validate (self):
        return len(self._get_num()) < Phone.NUM_LEN

class Email(Field):
    def __init__(self, value):
        is_valid = self._validate_email(value)
        if not is_valid:
            raise ValueError("Incorrect email")
        super().__init__(value)

    def _validate_email(email: str) -> bool:
        pass

class Address(Field):
    def __init__(self, value):
        ...

class Note(Field):
    def __init__(self, value):
        ...


class Birthday(Field):
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, value):
        ...

    def __str__(self):
        ...


class ContactCongratulation(Birthday):
    def __init__(self, name, value):
        ...

    def __str__(self):
        ...
