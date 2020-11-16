#!/usr/bin/env/ python3

# Apps module originally created by Sebastian-Byte, FabioPolancoE and FRostri
# Edited by Suaj

import os
import sys
import setup
import subprocess
from random import randint
from dotenv import load_dotenv


load_dotenv()

# Each command's description
all_commads = {
        "hello": "Prints \"Hello, World!\"",
        "numguess": "An awesome Guess-The-Number game",
        "ls": "Lists the files and directories inside of the home folder",
        "new": "Creates a new file by specifying its name",
        "show": "Prints the contents of a file",
        "pyshell": "Opens an embedded Python 3 shell",
        "pyrun": "Executes a Python 3 file",
        "interactive": "Opens an interactive Python 3 shell. Requires the\
\"ipython\" module",
        "edit": "Edit or create files, requires \"nano\" installed",
        "help": "Shows information about all available commands",
        "exit": "Stops the execution of FakeOS"
        }

# Definition of the commands
def hello():
    print("Hello, World!")

def numguess():
    number = randint(1, 10)
    while True:
        guess = int(input("I'm thinking of a number between 1 and 10, try\
to guess it...\n")
        if guess == number:
            print("Wow, you did it! :D")
            break
        else:
        print("Oops! that isn't the number I'm thinking of D:")

def ls():
    home = os.listdir("./home")
    if home:
        for i in home:
            print(i)
    elif not home or len(home) == 0:
        print("The home folder is empty.")

def new(filename):
    if sys.platform.startswith("win32"):
        os.system(f"type nul > ./home/{filename}")
    else:
        subprocess.call(["cat", f"./home/{filename}"])

def show(filename):
    with open(f"./home/{filename}", "r") as f:
        fcontent = f.readlines()
    for i in fcontent:
        print(i, end='')  # Each line already has the \n char at the end

def help(method=False):
    if method:
        print(all_commands[method])
    else:
        print("All available commands:\n")
        for i in all_commands.keys():
            print(f"{i}: {all_commands[i]}\n")

def pyrun(filename):
    os.system(f"python {filename}")  # Same command for all platforms

def pyshell():
    print("")
    os.system("python")
    print("")

def interactive():
    print("")
    os.system("ipython")
    print("")

def edit(filename):
    try:
        editor = os.getenv("EDITOR")
        if sys.platform.startswith("win32"):
            os.system(f"{editor} {filename}")
        else:
            subprocess.call([editor, filename])
    except:  # There should be an specific exception here
        if sys.platform.startswith("win32"):
            os.system(f"start notepad.exe {filename}")
        else:
            subprocess.call(["nano", f"./home/{filename}"])

def install():
    setup.start()

