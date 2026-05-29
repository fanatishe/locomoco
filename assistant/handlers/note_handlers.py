from assistant.contacts.address_book import Book
from assistant.cli.decorators import input_error
from assistant.utils.table_printer import format_notes_table


@input_error
def note_add(args: list[str], book: Book) -> str:
    """
    Creates a new text note and assigns it an auto-incrementing ID.

    Args:
        args (list[str]): The body text of the note, split into words.
        book (Book): The root application state containing the notebook.

    Returns:
        str: A success message including the newly generated note ID.

    Raises:
        ValueError: If no text is provided.
    """
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
            results.append(
                {"id": note_id, "text": note_info["text"], "tags": note_info["tags"]}
            )

    if not results and query:
        return f"No notes found matching: '{args[0]}'"

    return format_notes_table(results)


@input_error
def note_tag_add(args: list[str], book: Book) -> str:
    """
    Assigns a descriptive tag to an existing note.

    Args:
        args (list[str]): User input containing the note ID and the tag string.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the tag attachment, or an error if the tag exists.

    Raises:
        ValueError: If the note ID is missing/invalid, or the tag name is missing.
    """
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
def note_tag_search(args: list[str], book: Book) -> str:
    """
    Filters the notebook to find notes containing a specific tag (partial matches allowed).
    If no tag is provided, displays a list of all unique tags currently in use across the system.

    Args:
        args (list[str]): An optional list containing the tag search query.
        book (Book): The root application state.

    Returns:
        str: A formatted table of matching notes, or a bulleted list of all available tags.
    """
    # CASE 1: No arguments provided -> Show all unique tags
    if not args or not args[0].strip():
        if not book.notebook.data:
            return "No notes found."

        all_tags = set()
        for note_info in book.notebook.data.values():
            # .update() adds multiple items to a set, ignoring duplicates automatically
            all_tags.update(note_info.get("tags", []))

        if not all_tags:
            return "No tags have been created yet."

        # Format the unique tags into a clean bulleted list
        sorted_tags = sorted(list(all_tags))
        formatted_list = "\n".join(f"  • {tag}" for tag in sorted_tags)
        return f"\nAvailable tags:\n{formatted_list}\n"

    # CASE 2: Argument provided -> Search notes by partial tag match
    query_tag = args[0].lower()
    matched_notes = []

    for note_id, note_info in book.notebook.data.items():
        if any(query_tag in tag for tag in note_info.get("tags", [])):
            matched_notes.append(
                {"id": note_id, "text": note_info["text"], "tags": note_info["tags"]}
            )

    if not matched_notes:
        return f"No notes found with tag containing: '{args[0]}'"

    return format_notes_table(matched_notes)


@input_error
def note_tag_sort(args, book: Book) -> str:
    """
    Sorts all notes by their tags alphabetically.
    Notes without tags are placed at the bottom of the list.

    Args:
        args (list[str]): Command arguments (none expected for this command).
        book (Book): The root application state.

    Returns:
        str: A formatted string of sorted notes.
    """
    if not book.notebook.data:
        return "No notes found."

    notes_list = []
    for note_id, note_info in book.notebook.data.items():
        sorted_tags = sorted(note_info.get("tags", []))
        notes_list.append(
            {"id": note_id, "text": note_info["text"], "tags": sorted_tags}
        )

    # Sort by presence of tags first, then alphabetically by tags
    notes_list.sort(key=lambda x: (0 if x["tags"] else 1, ", ".join(x["tags"])))

    return format_notes_table(notes_list)
