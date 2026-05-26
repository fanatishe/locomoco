from ..domain import AddressBook
from .decorators import unexpected_exit


@unexpected_exit
def run(book: AddressBook) -> None:
    ...
