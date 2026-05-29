from assistant.contacts.address_book import Book
from assistant.utils.decorators import input_error


@input_error
def note_add(args, book: Book):
    if not args:
        return "Please provide content for the note."

    note_text = " ".join(args)
    note_id = book.notebook.add_note(note_text)
    return f"Note #{note_id} added successfully to your separate notebook!"


def note_change(*args):
    return "Command 'note_change' TO BE IMPLEMENTED"


def note_delete(*args):
    return "Command 'note_delete' TO BE IMPLEMENTED"


def note_search(*args):
    return "Command 'note_search' TO BE IMPLEMENTED"


def note_tag_add(*args):
    return "Command 'note_tag_add' TO BE IMPLEMENTED"


def note_tag_change(*args):
    return "Command 'note_tag_change' TO BE IMPLEMENTED"


def note_tag_delete(*args):
    return "Command 'note_tag_delete' TO BE IMPLEMENTED"


def note_tag_search(*args):
    return "Command 'note_tag_search' TO BE IMPLEMENTED"
