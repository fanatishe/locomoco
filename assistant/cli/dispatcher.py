from assistant.cli.commands import COMMANDS


def dispatch(command_parts: list[str], commands=None) -> tuple:
    if not commands:
        commands = COMMANDS

    if len(command_parts) == 0 and "/" in commands and callable(commands["/"]):
        return (commands["/"], [])
    else:
        command = command_parts[0].lower()

    if command in commands:
        if callable(commands[command]):
            return (commands[command], command_parts[1:])
        elif isinstance(commands[command], str):
            return (commands[command], [])
        elif isinstance(commands[command], dict):
            return dispatch(command_parts[1:], commands[command])

    return (lambda *_: "Invalid command.", [])
