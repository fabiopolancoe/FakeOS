#!/usr/bin/python3

# Apps module coded by Sebastian-Byte, FabioPolancoE, FRostri and SuajCarrot

import os
import setup
import subprocess
from random import randint
from dotenv import load_dotenv



load_dotenv()

# Each command's description
commands_help = {
    "hello":
    "A simple command that prints 'Hello World!'",
    "numguess":
    "An awesome Guess-The-Number Game",
    "ls":
    "Lists all the files and directories inside the home folder",
    "new":
    "Creates a new file, use with 'new [filename]', i.e 'new hi.txt'",
    "show":
    "Prints the contents of a file",
    "help":
    "Shows information about a available commands",
    "exit":
    "Stops the execution of FakeOS",
    "pyshell":
    "Opens an embedded Python shell",
    "pyrun":
    "Executes a Python file, place the file inside the home folder and type 'pyrun [filename]', i.e. 'pyrun hello.py'",
    "interactive":
    "Opens an interactive Python shell, requires 'iPython' installed",
    "edit":
    "Edit or create files, type 'edit [filename]', i.e. 'edit note.txt', \
requires a text editor installed",
    "install":
    "Activates setup script",
    "clear":
    "Clears the console"
}


class main:
    def __init__(self):
        pass


    # Definition of the commands
    def hello():
        print("Hello, World!")


    def numguess():
        number = randint(1, 10)
        while True:
            guess = int(
                input("I'm thinking of a number between 1 and 10, try \
to guess it > "))
            if guess == number:
                print("Wow, you did it! :D")
                break
            else:
                print("Oops! that isn't the number I'm thinking of D:")


    def ls():
        home = f"{os.getcwd()}/home"
        if os.path.isdir(home):
            if len(os.listdir(home)) == 0:
                print("The home folder is empty.")
            else:
                for i in os.listdir(home):
                    print(i)
        else:
            print("Whoops, looks like the home folder doesn't exist!")


    def new(filename):
        if ".." in filename:
            print("You can't create files outside of the Home folder!")
        else:
            try:
                f = open(f"./home/{filename}", "x")
                f.close()
            except FileExistsError:
                print("That file already exists!")


    def show(filename):
        if ".." in filename:
            print("You can't view files outside of the Home folder!")
        else:
            with open(f"./home/{filename}", "r") as f:
                fcontent = f.readlines()
                for i in fcontent:
                    print(i, end='')  # Each line already has the \n char at the end


    def help_fkos(method=False):
        if method:
            print(commands_help[method])
        else:
            print("All available commands:\n")
            for i in commands_help.keys():
                print(f"{i}: {commands_help[i]}\n")


    def pyrun(filename):
        if ".." in filename:
            print("You can't run files outside of the Home folder!")
        else:
            subprocess.run(["python3", f"./home/{filename}"])


    def pyshell():
        print("")
        subprocess.run("python3")
        print("")


    def interactive():
        print("")
        subprocess.run("ipython3")
        print("")


    def edit(filename):
        if ".." in filename:
            print("You can't edit files outside of Home folder!")
        else:
            try:
                editor = os.getenv("EDITOR")
                subprocess.run([editor, f"./home/{filename}"])
            except OSError:
                subprocess.run(["nano", f"./home/{filename}"])


    def clear():
        subprocess.run(["tput", "reset"])


    def install():
        print("")
        setup.start()
        print("")
