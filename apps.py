#!/usr/bin/env/ python3

# Apps module originally created by Sebastian-Byte, FabioPolancoE and FRostri
# Edited by Suaj
# Ported to Windows by Sebastian-Byte

import os
import sys
import setup
from random import randint
from dotenv import load_dotenv


load_dotenv()

# Each command's description
all_commands = {"hello": "A simple command that prints 'Hello World!'",
                "numguess": "An awesome Guess-The-Number Game",
                "ls": "Lists all the files and directories inside the home folder",
                "new": "Creates a new file, use with 'new [filename]', i.e 'new hi.txt'",
                "show": "Prints the contents of a file",
                "help": "Shows information about a available commands",
                "exit": "Stops the execution of FakeOS",
                "pyshell": "Opens an embedded python3 shell",
                "pyrun": "Executes a python3 file, place the file inside the home folder and type 'pyrun [filename]', i.e. 'pyrun hello.py'",
                "interactive": "Opens an interactive python3 shell, requires 'ipython' installed",
                "edit": "Edit or create files, type 'edit [filename]', i.e. 'edit note.txt', requires a text editor installed",
                "install": "Activates setup script",
                "clear": "Clears the console"}

# Definition of the commands
def hello():
    print("Hello, World!")

def numguess():
    number = randint(1, 10)
    while True:
        guess = int(input("I'm thinking of a number between 1 and 10, try to guess it > "))
        if guess == number:
            print("Wow, you did it! :D")
            break
        else:
            print("Oops! that isn't the number I'm thinking of D:")

def ls():
    home = os.listdir(".\\home\\")
    if home:
        for i in home:
            print(i)
    elif not home or len(home) == 0:
        print("The home folder is empty.")

def new(filename):
    os.system(f"type nul > .\\home\\{filename}")

def show(filename):
    with open(f"./home/{filename}", "r") as f: # In Python using / is correct, not in os.system().
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
    os.system(f"python {filename}")

def pyshell():
    print("")
    os.system("python")
    print("")

def interactive():
    print("")
    os.system('ipython')
    print("")

def edit(filename):
    try:
        editor = os.getenv("EDITOR")
        os.system(f"{editor} .\\home\\{filename}")
    except OSError:
        os.system(f"start notepad .\\home\\{filename}")

def clear():
    os.system("cls")

def install():
    setup.start()
