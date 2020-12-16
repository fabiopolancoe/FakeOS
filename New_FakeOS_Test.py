#!/usr/bin/python3

# FakeOS redesign test. Originally coded by:
# FabioPolancoE, Sebastian-Byte and FRostri.
# Redesign coded by SuajCarrot.

import os
import sys
import apps
import subprocess
from getpass import getuser

try:
    from art import text2art
except ModuleNotFoundError:
    pass
else:
    print(text2art("FakeOS"))

print("Welcome to FakeOS!")


# Available commands
all_commands = {
        "hello": apps.hello,
        "numguess": apps.numguess,
        "ls": apps.ls,
        "new": apps.new,
        "show": apps.show,
        "help": apps.help,
        "exit": apps.exit_fakeos,
        "pyshell": apps.pyshell,
        "pyrun": apps.pyrun,
        "interactive": apps.interactive,
        "edit": apps.edit,
        # "install": apps.install,
        "clear": apps.clear
        }

# Get the operation, with a BASH style
while True:
    operation = input(f"[{getuser()}@FakeOS]$ ")
    # arguments = operation.split(' ')
    # del arguments[0]  # The first element is the command itself
    try:
        all_commands[operation]()  # (i for i in arguments)  # Call the function
    except KeyError:
        print(f"Whoops! The command \"{operation}\" does not exist.")
    except Exception as id:
        print("An exception occurred during the process.")
        print(f"Exception details: {id}")
