#!/usr/bin/env python3

# Main module, originally created by FabioPolancoE
# Edited by Suaj

Fabio si estás escribiendo en la terminal no veo nada, está todo bugeado
Solo veo que se mueve el cursor pero los caracteres son un desastre

import signal

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
            sure = input("Do you really want to log out? [Y/n]: ")
            if sure.lower() in ["y", "yes"]:
                print("Bye! ;D")
                quit()

            elif sure.lower() in ["n", "no", "nope"]:
                return False
            else:
                print("You did not choose a correct option.")
                return False
        else:
            import apps
            try:
                if data:
                    eval("apps." + method + "(*data)")
                    return True
                else:
                    eval("apps." + method)()
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

