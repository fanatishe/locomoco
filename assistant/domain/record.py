from .fields import Name, Phone, Birthday, Email, Address, Note


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None
        self.email: Email | None = None
        self.address: Address | None = None
        self.notes: list[Note] = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)

        if phone_obj is None:
            raise ValueError("Phone not found")

        self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_obj = self.find_phone(old_phone)

        if phone_obj is None:
            raise ValueError("Phone not found")

        index = self.phones.index(phone_obj)
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_email(self, email: str) -> None:
        self.email = Email(email)

    def edit_email(self, email: str) -> None:
        self.email = Email(email)

    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def edit_address(self, address: str) -> None:
        self.address = Address(address)

    def add_note(self, text: str) -> None:
        self.notes.append(Note(text))

    def list_notes(self) -> str:
        if not self.notes:
            return "No notes for this contact."

        return "\n".join(
            f"{index}. {note}" for index, note in enumerate(self.notes, start=1)
        )

    def edit_note(self, index: int, text: str) -> None:
        if index < 1 or index > len(self.notes):
            raise IndexError("Note with this number does not exist")

        self.notes[index - 1] = Note(text)

    def delete_note(self, index: int) -> None:
        if index < 1 or index > len(self.notes):
            raise IndexError("Note with this number does not exist")

        self.notes.pop(index - 1)

    def delete_all_notes(self) -> None:
        self.notes.clear()

    def __str__(self):
        phones = "; ".join(str(phone) for phone in self.phones) or "-"
        birthday = str(self.birthday) if self.birthday else "-"
        email = str(self.email) if self.email else "-"
        address = str(self.address) if self.address else "-"
        notes_count = len(self.notes)

        return (
            f"Name: {self.name}, "
            f"phones: {phones}, "
            f"email: {email}, "
            f"address: {address}, "
            f"birthday: {birthday}, "
            f"notes: {notes_count}"
        )
