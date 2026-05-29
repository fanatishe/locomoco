from assistant.contacts.address_book import Book
from assistant.utils.decorators import input_error


@input_error
def note_add(args, book: Book):
    if not args:
        raise ValueError("Give me note text please")

    text = " ".join(args)
    note_id = book.notebook.add_note(text)
    return f"Note added with ID: {note_id}."


@input_error
def note_change(args, book: Book):
    try:
        note_id = int(args[0])
        text = " ".join(args[1:])
    except (ValueError, IndexError):
        raise ValueError("Give me note ID and new text please")

    if note_id not in book.notebook.data:
        return f"Note with ID {note_id} not found."

    if not text:
        raise ValueError("Note text cannot be empty")

    book.notebook.data[note_id]["text"] = text
    return f"Note {note_id} updated."


@input_error
def note_delete(args, book: Book):
    if not args:
        raise ValueError("Give me note ID please")

    try:
        note_id = int(args[0])
    except ValueError:
        raise ValueError("Note ID must be an integer")

    if note_id in book.notebook.data:
        del book.notebook.data[note_id]
        return f"Note {note_id} deleted."
    return f"Note with ID {note_id} not found."


@input_error
def note_search(args, book: Book):
    if not book.notebook.data:
        return "No notes found."

    query = args[0].strip().lower() if (args and args[0].strip()) else None
    results = []

    for note_id, note_info in book.notebook.data.items():
        if query is None or query in note_info["text"].lower():
            tags_str = ", ".join(note_info["tags"]) if note_info["tags"] else "no tags"
            results.append(f"ID {note_id} [{tags_str}]: {note_info['text']}")

    if not results and query:
        return f"No notes found matching: '{args[0]}'"

    return "\n".join(results)


@input_error
def note_tag_add(args, book: Book):
    try:
        note_id = int(args[0])
        tag = args[1].lower()
    except (ValueError, IndexError):
        raise ValueError("Give me note ID and tag name please")

    if note_id not in book.notebook.data:
        return f"Note with ID {note_id} not found."

    if tag not in book.notebook.data[note_id]["tags"]:
        book.notebook.data[note_id]["tags"].append(tag)
        return f"Tag '{tag}' added to note {note_id}."
    return f"Tag '{tag}' already exists on note {note_id}."


@input_error
def note_tag_change(args, book: Book):
    try:
        note_id = int(args[0])
        old_tag = args[1].lower()
        new_tag = args[2].lower()
    except (ValueError, IndexError):
        raise ValueError("Give me note ID, old tag, and new tag please")

    if note_id not in book.notebook.data:
        return f"Note with ID {note_id} not found."

    tags = book.notebook.data[note_id]["tags"]
    if old_tag in tags:
        if new_tag not in tags:
            tags[tags.index(old_tag)] = new_tag
            return f"Tag '{old_tag}' changed to '{new_tag}' on note {note_id}."
        else:
            tags.remove(old_tag)
            return f"Tag '{old_tag}' replaced by existing tag '{new_tag}' on note {note_id}."
    return f"Tag '{old_tag}' not found on note {note_id}."


@input_error
def note_tag_delete(args, book: Book):
    try:
        note_id = int(args[0])
        tag = args[1].lower()
    except (ValueError, IndexError):
        raise ValueError("Give me note ID and tag name please")

    if note_id not in book.notebook.data:
        return f"Note with ID {note_id} not found."

    if tag in book.notebook.data[note_id]["tags"]:
        book.notebook.data[note_id]["tags"].remove(tag)
        return f"Tag '{tag}' removed from note {note_id}."
    return f"Tag '{tag}' not found on note {note_id}."


@input_error
def note_tag_search(args, book: Book):
    if not args:
        raise ValueError("Give me a tag name to search for please")

    query_tag = args[0].lower()
    results = []

    for note_id, note_info in book.notebook.data.items():
        if query_tag in note_info["tags"]:
            tags_str = ", ".join(note_info["tags"])
            results.append(f"ID {note_id} [{tags_str}]: {note_info['text']}")

    if not results:
        return f"No notes found with tag: '{args[0]}'"
    return "\n".join(results)
