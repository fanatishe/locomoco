from assistant.handlers.contact_handlers import add_contact
from assistant.handlers.contact_handlers import show_all


COMMANDS = {
    "add": add_contact,
    "all": show_all,
}
