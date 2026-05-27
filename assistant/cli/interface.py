from assistant.cli.parser import parse_input
from assistant.storage.pickle_storage import load_data, save_data
from assistant.cli.cli_prompt import get_user_input
from assistant.utils.welcome_message import generate_jarvis_interface
from assistant.cli.dispatcher import dispatch


def run_cli():
    generate_jarvis_interface()
    book = load_data()

    try:
        while True:
            user_input = get_user_input()

            command_parts = parse_input(user_input)
            handler, args = dispatch(command_parts)

            if handler in ["close", "exit"]:
                print("Good bye!")
                break

            result = handler(args, book)

            print(result)
    finally:
        save_data(book)
