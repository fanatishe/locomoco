from assistant.contacts.field import Field


class Email(Field):
    def __init__(self, value: str):
        super().__init__(value)
