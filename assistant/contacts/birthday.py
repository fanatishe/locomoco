from datetime import datetime
from assistant.contacts.field import Field


class Birthday(Field):
    """
    Birthday in the format DD.MM.YYYY
    """

    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date)
