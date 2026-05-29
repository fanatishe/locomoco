from assistant.cli.parser import parse_input
from assistant.storage.pickle_storage import load_data, save_data
from assistant.cli.cli_prompt import get_user_input
from assistant.utils.messages import generate_jarvis_interface
from assistant.utils.messages import good_bye
from assistant.cli.dispatcher import dispatch
from assistant.cli.decorators import unexpected_exit
from assistant.cli.exceptions import GoodByeException


@unexpected_exit
def run_cli():
    """Runs the main CLI loop (or takes data from pipe/file)"""
    generate_jarvis_interface()
    book = load_data()

    try:
        while True:
            user_input = get_user_input()

            command_parts = parse_input(user_input)
            handler, args = dispatch(command_parts)

            try:
                result = handler(args, book)
                print(result)
            except GoodByeException:
                good_bye()
                break

    finally:
        save_data(book)
