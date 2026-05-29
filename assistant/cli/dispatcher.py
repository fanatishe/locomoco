from assistant.cli.commands import commands_list
from difflib import get_close_matches


def guess_command(user_input, available_commands):
    # Returns a list of the closest matches
    matches = get_close_matches(user_input, available_commands, n=1, cutoff=0.6)

    if matches:
        return f"Invalid command. Did you mean '{matches[0]}'?\n"
    return "Invalid command.\n"


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

    return (lambda *_: guess_command(" ".join(command_parts), commands_names), [])
