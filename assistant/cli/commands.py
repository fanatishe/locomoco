from assistant.handlers.contact_handlers import (
    add_contact,
    add_email,
    set_address,
    show_all,
    show_contact,
    set_note,
)


COMMANDS = {
    "add": add_contact,
    "contact": show_contact,
    "add-email": add_email,
    "set-address": set_address,
    "set-note": set_note,
    "all": show_all,
}
