#!/usr/bin/python3

# Set Up module, originally created by FabioPolancoE and Sebastian-Byte
# Edited by Suaj

import subprocess, pickle, sys, os
from getpass import getuser  # To get the name of the PC user

def install_module(module):
    '''Installs the given module if the user allows to do so.
    Returns True or False depending on the confirmation.'''
    while True:
        conf = input(f"The {module} module is not installed, do you want\
 to install it? [Y/n]: ")
        conf = conf.lower()
        if conf in ["y", "yes", "", " "]:
            print(f"Ok, installing the {module} module...")
            subprocess.run(["python", "-m", "pip", "install", module], shell=True)
            return True
        elif conf in ["n", "no", "nope"]:
            print(f"Ok, the {module} module will not be \
installed.")
            return False
        else:
            print("Please, select a valid option.")

def start_setup():
    '''The script inside of a function for easy calls'''
    print("Welcome to the FakeOS installation script")

    # Check if the art module is installed
    print("Checking if the art module is installed...")
    try:
        from art import text2art
    except ModuleNotFoundError:
        install_module("art")
    else:
        print("The art module is installed.")

  # Check if the python-colortext module is installed
    print("Checking if the python-colortext module is \
installed...")
    try:
        from ColorText import ColorText
    except ModuleNotFoundError:
        install_module("Python-ColorText")
    else:
        print("The python-colortext module is installed.")

    if not sys.platform.startswith("win32"):
        # Add FakeOS to PATH
        conf = input("Do you want to add FakeOS to PATH? [Y/n]: ")
        if conf.lower() in ["y", "yes"]:
            try:
                if "bash" in os.environ['SHELL']:
                    fname = ".bashrc"
                elif "zsh" in os.environ['SHELL']:
                    fname = ".zshrc"
                    with open(f"/home/{getuser()}/{fname}", "a") as f:
                        f.writelines(f"alias fakeos='python3 {os.getcwd()}/main.py'\
 \nexport FAKEOSHOME={os.getcwd()}")
            except Exception as identifier:
                print("Sorry, an exception occurred during the process.")
                print(f"Exception Details: {identifier}")

        elif conf.lower() in ["n", "no", "nope"]:
            print("Ok, FakeOS will not be added to PATH.")

    # Let the user choose the editor
    print("\n[Vim|Neovim|VSCode|Notepad]")
    editor = input("Choose your favorite text editor (It should be already installed): ")
    editor = editor.lower()
    if editor == "neovim":
        editor = "nvim"
    elif editor == "vscode":
        editor = "code"
    with open("./editor.pkl", "wb") as f:
        pickle.dump(editor, f)
    print("\nThe Setup has ended. Please close and reopen your terminal to apply all changes. Have fun! :D")

if __name__ == "__main__":
    start_setup()
