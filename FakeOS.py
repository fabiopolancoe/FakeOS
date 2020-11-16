#!/usr/bin/env python3

import signal

# Print the name, if the text2art module is found.
try:
    from art import text2art
    print(text2art("FakeOS"))
except ModuleNotFoundError, NameError:
    pass

# The apps module is already included, but just in case...
try:
    import apps
except ModuleNotFoundError:
    print("The required module \"apps\" was not found, exiting...")
    quit()
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
            sure = input("Do you really want to log out? [Y/n]\n")
            if sure.lower() in ["y", "yes"]:
                print("Bye! ;D")
                quit()

            elif sure.lower() in ["n", "no", "nope"]:
                return False

            else:
                print("You did not choose a correct option.")
                return False

        else:
            try:
                if data:
                    eval("apps." + method + "(*data)")
                    return True
                else:
                    eval("apps." + method())
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

