#!/usr/bin/python3

# Apps module originally created by Sebastian-Byte, FabioPolancoE and FRostri
# Edited by Suaj
# Ported to Windows by Sebastian-Byte

import os
import sys
import setup
import subprocess
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
                "pyshell": "Opens an embedded Python shell",
                "pyrun": "Executes a Python file, place the \
file inside the home folder and type 'pyrun [filename]', i.e. 'pyrun hello.py'",
                "interactive": "Opens an interactive python3 shell, requires 'iPython' installed",
                "edit": "Edit or create files, type 'edit [filename]', i.e. 'edit note.txt', \
requires a text editor installed",
                "delete": "Deletes a file, type 'delete [filename], i.e. 'delete file.txt'",
                "install": "Activates setup script",
                "clear": "Clears the console"}


class func:
    def __init__(self):
        pass

    # Definition of the commands
    def hello(self):
        print("Hello, World!")

    def numguess(self):
        number = randint(1, 10)
        while True:
            guess = int(
                input("I'm thinking of a number between 1 and 10, try to guess it > "))
            if guess == number:
                print("Wow, you did it! :D")
                break
            else:
                print("Oops! that isn't the number I'm thinking of D:")

    def ls(self):
        home = f"{os.getcwd()}\\home"
        if os.path.isdir(home):
            if len(os.listdir(home)) == 0:
                print("The home folder is empty.")
            else:
                for i in os.listdir(home):
                    print(i)
        else:
            print("Whoops, looks like the home folder doesn't exist!")

    def new(self, filename):
        if ".." in filename:
            print("You can't create files outside of the Home folder!")
        else:
            try:
                f = open(f"./home/{filename}", "x")
                f.close()
            except FileExistsError:
                print("That file already exists!")

    def show(self, filename):
        if ".." in filename:
            print("You can't view files outside of the Home folder!")
        else:
            # In Python using / is correct, not in the Console.
            with open(f"./home/{filename}", "r") as f:
                fcontent = f.readlines()
            for i in fcontent:
                print(i, end='')  # Each line already has the \n char at the end

    def help(self, method=False):
        if method:
            print(all_commands[method])
        else:
            print("All available commands:\n")
            for i in all_commands.keys():
                print(f"{i}: {all_commands[i]}\n")

    def pyrun(self, filename):
        if ".." in filename:
            print("You can't run files outside the Home folder!")
        else:
            print("")
            os.system(f"python .\\home\\{filename}")
            print("")

    def pyshell(self):
        print("")
        subprocess.run("python", shell=True)
        print("")

    def interactive(self):
        print("")
        subprocess.run("ipython", shell=True)
        print("")

    def edit(self, filename):
        if ".." in filename:
            print("You can't edit files outside of the Home folder!")
        else:
            try:
                editor = os.getenv("EDITOR")
                subprocess.run([editor, f".\\home\\{filename}"], shell=True)
            except OSError:
                subprocess.run([editor, f".\\home\\{filename}"], shell=True)

    def delete(self, filename):
        if ".." in filename:
            print("You can't delete files outside of the Home folder!")
        else:
            subprocess.run(["del", f".\\home\\{filename}"], shell=True)

    def clear(self):
        subprocess.run("cls", shell=True)

    def install(self):
        print("")
        setup.start()
        print("")
