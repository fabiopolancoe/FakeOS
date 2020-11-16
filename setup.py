#!/usr/bin/env python3

# Set Up module, originally created by FabioPolancoE and Sebastian-Byte
# Edited by Suaj

import pip  # To install missing modules, if the user allows us
import sys  # To check actual OS
from getpass import getuser  # To get the name of the PC user
from os import environ, getcwd


def install_module(module):
    '''Installs the given module if the user allows to do so.
    Returns True or False depending on the confirmation.'''
    while True:
        conf = input("The {module} module is not installed, do you want\
to install it? [Y/n]\n")
        if conf.lower() in ["y", "yes"]:
            print(f"Ok, installing the {module} module...")
            pip.main(["install", module])
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
    print("Cheking if the art module is installed...")
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

    if sys.platform != 'win32': # Check the OS.
        # Add FakeOS to PATH
        conf = input("Do you want to add FakeOS to PATH? [Y/n]: ")
        if conf.lower() in ["y", "yes"]:
            try:
                if "bash" in environ["SHELL"]:
                    fname = ".bashrc"
                elif "zsh" in environ["SHELL"]:
                    fname = ".zshrc"
                with open(f"/home/{getuser()}/{fname}", "a") as f:
                    f.writelines(f"alias fakeos='python3 {getcwd()}/main.py'\
\nexport FAKEOSHOME={getcwd()}")

            except Exception as identifier:
                print("Sorry, an exception occurred during the process.")
                print(f"Exception Details: {identifier}")

        elif conf.lower() in ["n", "no", "nope"]:
            print("Ok, FakeOS will not be added to PATH.")
    else:
        pass # Do not add to PATH if OS is Windows.

    # Let the user choose the editor
    print("\n[Nano|Vim|NeoVim|Gedit|Pluma]")
    editor = input("Choose your favorite text editor (It should be already installed): ")
    if editor.lower() == "neovim":
        editor = "nvim"
    with open("./data.env", "w") as data:
        data.write(f"EDITOR={editor}")

    print("\nThe SetUp has ended. Have fun! :D")


if __name__ == "__main__":
    start()
