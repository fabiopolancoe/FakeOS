#!/usr/bin/python3

# Main module, originally coded by FabioPolancoE, Sebastian-Byte,
# FRostri and SuajCarrot.

import os, sys, setup
from new_apps import *
from getpass import getuser

try:
    from art import text2art
except ModuleNotFoundError:
    pass
else:
    print(text2art("FakeOS"))

print("Welcome to FakeOS!")  # Welcome Message
print("Note: The \"help\" command is temporarily disabled.")

apps = apps()  # Initialization of the apps class

# To avoid possible errors with other modules, the exit
# function is defined here
def exit_fkos(*args):
    while True:
        op = input("Are you sure you want to exit? [Y/n]: ")
        op = op.lower()
        if op in ["y", "yes", " ", ""]:
            sys.exit(0)
        elif op in ["n", "no", "nope"]:
            break
        else:
            print("Please, enter a valid option.")


all_commands = {
    "hello": apps.hello,
    "numguess": apps.numguess,
    "ls": apps.ls,
    "new": apps.new,
    "show": apps.show,
    # Remember to create the new dictionary of help
    # "help": apps.help_fkos,
    "pyshell": apps.pyshell,
    "pyrun": apps.pyrun,
    "interactive": apps.interactive,
    "edit": apps.edit,
    "install": setup.start_setup,
    "cd": apps.cd,
    "clear": apps.clear,
    "mkdir": apps.mkdir,
    "remove": apps.remove,
    "exit": exit_fkos
}

# Get input with a BASH style
while True:
    op = input(f"[{getuser()}@FakeOS ~]$ ")
    op = op.lower()
    # Get the arguments
    arguments = op.split(" ")
    # The first element is the command itself
    command = arguments[0]
    del arguments[0]
    # This is for debugging purposes
    print("Arguments: ", end="")
    for i in arguments: 
        print(i, end=' ')
    print("\n")

    try:
        # Call the function with the given arguments
        if len(arguments) > 0:
            all_commands[command](*arguments)
        # Call the function without arguments
        else:
            all_commands[command]()
    # Error management
    except KeyError:
        print(f"Whoops! The command \"{op}\" does not exist.")
    except TypeError:
        print(f"Looks like you have missing arguments...")
    except Exception as id:
        print(f"""An exception occurred during the process.
Exception details: {id}""")
