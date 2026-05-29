import os
import sys
import time


def clear_screen():
    # Clears the terminal for a clean system boot look
    os.system("cls" if os.name == "nt" else "clear")


def generate_jarvis_interface():
    if not sys.stdin.isatty():
        return
    clear_screen()
    # Simulate a quick systems check load sequence
    CYAN = "\033[96m"
    RESET = "\033[0m"
    WHITE_BOLD = "\033[1;97m"

    sys.stdout.write(f"{CYAN}Booting JARVIS mainframe ")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4)
    print(f" {RESET}")

    clear_screen()
    # Display the final interface

    # Cyan/Blue ANSI escape color codes for that holographic look
    CYAN = "\033[96m"
    RESET = "\033[0m"

    # Big Text "JARVIS" (ASCII Block Font)
    jarvis_ascii = f"""{CYAN}
      ██████╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
      ╚═██╔═╝██╔══██╗██╔══██╗██║   ██║██║██╔════╝
        ██║  ███████║██████╔╝██║   ██║██║███████╗
   ██╗  ██║  ██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
   ╚██████║  ██║  ██║██║  ██║ ╚████╔╝ ██║███████║
    ╚═════╝  ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝{RESET}

Welcome to the assistant
Use {WHITE_BOLD}tab{RESET} or {WHITE_BOLD}right arrow{RESET} for auto-complete
Enter {CYAN}help{RESET} command to see the list of all commands

"""
    print(jarvis_ascii)


def good_bye():
    if not sys.stdin.isatty():
        return
    print("Good bye!")
