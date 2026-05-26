from assistant.handlers.contact_handlers import add_contact, add_email, set_address, show_all


COMMANDS = {
    "add": add_contact,
    "add-email": add_email,
    "set-address": set_address,
    "all": show_all,
}
