class Field:
    def __init__(self, value):
        ...

    def __str__(self):
        ...

    def __format__(self, format_spec):
        ...


class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value):
        ...

class Email(Field):
    def __init__(self, value):
        ...

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
