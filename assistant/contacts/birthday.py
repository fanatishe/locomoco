from .field import Field
from datetime import date
class Birthday(Field):
    DATE_FORMAT = "%d.%m.%Y"
    def __init__(self, value):
        try:
            value = date.strptime(value, Birthday.DATE_FORMAT)
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def _format_date(self, date: date):
        return date.strftime(Birthday.DATE_FORMAT)
    
    def __str__(self):
        return f"{self._format_date(self.value)}"
    
class ContactCongratulation(Birthday):
    def __init__(self, value, name):
        super().__init__(value)
        self.name = name

    def __str__(self):
        return f"On {self.value} congratulate {self.name} "