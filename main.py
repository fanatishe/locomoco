from assistant.cli import run
from assistant.domain import AddressBook
from assistant.storage import FileStorage
from assistant.utils import get_path


def main() -> None:
    file_path = get_path(__file__, "contacts.pkl")
    book = AddressBook(FileStorage(file_path))
    run(book)


if __name__ == "__main__":
    main()
