from assistant.handlers.contact_handlers import add_contact, show_all, show_contact


COMMANDS = {
    "add": add_contact,
    "contact": show_contact,
    "all": show_all,
}
