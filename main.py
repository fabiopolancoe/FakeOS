#!/usr/bin/python3

# Main module, originally created by FabioPolancoE
# Edited by Suaj
# Ported to Windows by Sebastian-byte

import signal
import sys

# Print the name, if the text2art module is found.
try:
    from art import text2art
    print(text2art("FakeOS"))
except ModuleNotFoundError:
    pass

from getpass import getuser  # To get the current PC user.

print("Welcome to FakeOS!")  # Welcome message, printed always.


def signal_handler(signal, frame):
    print("\nBye ;D!")
    quit()


def handle_command(data):
    '''Handles the command the user entered. If the command is not
    processed for any reason, the function returns False.'''
    if data:
        method = data[0]
        del data[0]
        if method.lower() == "exit":
            sure = input("Do you really want to logout? [Y/n]: ")
            if sure.lower() in ["y", "yes"]:
                print("Bye! ;D")
                sys.exit()

            elif sure.lower() in ["n", "no", "nope"]:
                return False
            else:
                print("You did not choose a correct option.")
                return False
        else:
            import apps
            app = apps.func()
            try:
                if data:
                    eval("app." + method + "(*data)")
                    return True
                else:
                    eval("app." + method + "()")
                    return True
            except:
                print("Couldn't handle that command D:")
                return False
    else:
        return False


signal.signal(signal.SIGINT, signal_handler)

# User input
while True:
    command = input(f"[{getuser()}@FakeOS]$ ")
    handle_command(command.split())
