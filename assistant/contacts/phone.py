from assistant.contacts.field import Field
from assistant.utils.validators import validate_phone


class Phone(Field):
    def __init__(self, value):
        validate_phone(value)
        super().__init__(value)
