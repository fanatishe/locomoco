from assistant.cli.commands import commands_list


def dispatch(command_parts: list[str]) -> tuple:
    commands_names = commands_list.keys()
    parts_to_check = []
    args = []
    command = ""
    for part in command_parts:
        parts_to_check.append(part)
        command_to_check = " ".join(parts_to_check)
        if command_to_check in commands_names:
            command = command_to_check
            args = command_parts[len(parts_to_check) :]

    if command and command in commands_list:
        if callable(commands_list[command]):
            return commands_list[command], args
        elif isinstance(commands_list[command], tuple):
            if len(args) >= commands_list[command][1]:
                return commands_list[command][0], args
            else:
                if "help " + command in commands_names:
                    return commands_list["help " + command][0], args

    # if not commands:
    #     commands = COMMANDS

    # if len(command_parts) == 0 and "/" in commands and callable(commands["/"]):
    #     return (commands["/"], [])
    # else:
    #     command = command_parts[0].lower()

    # if command in commands:
    #     if callable(commands[command]):
    #         return (commands[command], command_parts[1:])
    #     elif isinstance(commands[command], str):
    #         return (commands[command], [])
    #     elif isinstance(commands[command], dict):
    #         return dispatch(command_parts[1:], commands[command])

    return (lambda *_: "Invalid command.", [])
