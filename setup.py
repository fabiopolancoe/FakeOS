#!/usr/bin/python3

# Set Up module, originally created by FabioPolancoE and Sebastian-Byte
# Edited by Suaj
# Ported to Windows by Sebastian-byte

# import pip ## Acording to pip is recommended using "-m pip" because this module is deprecated.
import sys  # To check actual OS
from os import getcwd, environ, system
from getpass import getuser  # To get the name of the PC user


def install_module(module):
    '''Installs the given module if the user allows to do so.
    Returns True or False depending on the confirmation.'''
    while True:
        conf = input(f"The {module} module is not installed, do you want to install it? [Y/n]: ")
        if conf.lower() in ["y", "yes"]:
            print(f"Ok, installing the {module} module...")
            system(f"python -m pip install {module}")
            return True
        elif conf.lower() in ["n", "no", "nope"]:
            print(f"Ok, the {module} module will not be installed.")
            return False
        else:
            print("Please, select a valid option.")

def start():
    '''The script inside of a function for easy calls, if needed'''
    print("Welcome to the FakeOS installation script")

    # Check if the art module is installed
    print("Checking if the art module is installed...")
    try:
        from art import text2art
    except ModuleNotFoundError:
        install_module("art")
    else:
        print("The art module is installed.")

    # Check if the python-dotenv module is installed
    print("Checking if the python-dotenv module is installed...")
    try:
        import dotenv
    except ModuleNotFoundError:
        install_module("python-dotenv")
    else:
        print("The python-dotenv module is installed.")


    # Let the user choose the editor
    print("\n[Vim|Neovim|Notepad|VSCode]")
    editor = input("Choose your favorite text editor (It should be already installed): ")

    if editor.lower() == "neovim":
        editor = "nvim"
    if editor.lower() == "vscode":
        editor = "code"
    if editor.lower() == "notepad":
        editor = "notepad"

    with open("./.env", "w") as data:
        data.write(f"EDITOR={editor}")

    print("\nThe Setup has ended. Please close and reopen your terminal/console to apply all changes. Have fun! :D")


if __name__ == "__main__":
    start()
