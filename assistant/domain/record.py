from .fields import Name, Phone, Birthday


class Record:
    def __init__(self, name: str):
        self.name: Name
        self.phones: list[Phone]
        self.birthday: Birthday | None

    def add_phone(self, phone: str) -> None:
        ...

    def remove_phone(self, phone: str) -> None:
        ...

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        ...

    def find_phone(self, phone: str) -> Phone | None:
        ...

    def add_birthday(self, birthday: str) -> None:
        ...

    def __str__(self):
        ...
