from assistant.cli.commands import commands_list
from difflib import get_close_matches


def guess_command(user_input: str, available_commands: list[str]) -> str:
    """
    Analyzes unrecognized input and suggests the closest valid command using fuzzy matching.

    Args:
        user_input (str): The invalid command typed by the user.
        available_commands (list[str]): A list of all valid commands in the system.

    Returns:
        str: A string suggesting the closest match, or a generic invalid command message.
    """
    # Returns a list of the closest matches
    matches = get_close_matches(user_input, available_commands, n=1, cutoff=0.6)

    if matches:
        return f"Invalid command. Did you mean '{matches[0]}'?\n"
    return "Invalid command.\n"


def dispatch(command_parts: list[str]) -> tuple:
    """
    Routes the parsed user input to the appropriate handler function.

    Args:
        command_parts (list[str]): The user input split into a list of words.

    Returns:
        tuple: A tuple containing the handler function and a list of its arguments.
               If the minimum argument count is not met, returns the help handler for that command.
    """
    commands_names = list(commands_list.keys())
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
