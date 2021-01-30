#!/usr/bin/python3

# Apps module. Coded by FabioPolancoE, Sebastian-Byte,
# FRostri and SuajCarrot.

import os, sys, subprocess, shutil, pickle
from random import randint  # For the "numguess" game


class apps:
    def __init__(self):
        # TODO: Change this
        self.home = f"{os.getcwd()}/home"

    # Decorator funcion used to check if the user is trying to
    # do something outside of the home folder
    # It also handles exceptions
    # NOTE: More features can be added in the same decorator
    def home_folder_checker(function):
        def check_dotdot(self, *args):
            if len(args) > 0:
                for i in args:
                    if ".." in i and os.getcwd() == self.home or\
                    i.startswith("/"):
                        print("You can only manipulate things \
inside of the FakeOS's home folder!")
                    else:
                        try:
                            function(self, i)
                        except Exception as id:
                            print(f"""An exception occurred during \
the process.\nException details: {id}""")
            else:
                try:
                    function(self)
                except Exception as id:
                    print(f"""An exception occurred during \
the process.\nException details: {id}""")
        return check_dotdot

    def hello(self, *args):
        print("Hello, World!")

    def numguess(self, *args):
        self.num = randint(1, 10)
        self.last_try = 0  # Initialization to avoid errors
        while True:
            self.guess = input("I'm thinking of a number \
between 1 and 10, try to guess it > ")
            # Check if it's a string
            if self.guess.lower() in ["stop", "surrender"]:
                print(f"The number was {self.num} ;)")
                break
            elif self.guess.lower() in ["", " ", "\n"]:
                print("Ummm, where is your guess?")
            # If not, convert it to an int
            else:
                try:
                    self.guess = int(self.guess)
                except ValueError:
                    print("Whoops! That is not a number.")
            # Check if the user guessed the num
            if self.guess == self.last_try:
                print("I already told you that isn't the number \
I'm thinking of!")
            elif self.guess > 10 or self.guess < 1:
                print("Respect the range of the guess.")
            elif self.guess == self.num:
                print("Wow, you did it!")
                break
            else:
                print(f"Whoops! That isn't the number I'm \
thinking of.")
                self.last_try = self.guess

    # Home folder-related functions
    @home_folder_checker
    def ls(self, *args):
        if os.path.isdir(self.home):
            if len(os.listdir(self.home)) == 0:
                print("The home folder is empty.")
            else:
                print("Files and directories in the home folder: ")
                for i in os.listdir(self.home):
                    if os.path.isfile(f"{self.home}/{i}"):
                        print(f"{i} (File)")
                    elif os.path.isdir(f"{self.home}/{i}"):
                        self.acdir = f"{i}"
                        print(f"{i} (Directory)")
                    else:
                        print(f"{i} (???)")
        else:
            print("Whoops! looks like the home folder \
doesn't exist!")

    @home_folder_checker
    def new(self, fname, *args):
        self.fname = fname
        if os.path.isfile(f"{self.home}/{self.fname}"):
            print("Whoops, the file already exists.")
        else:
            try:
                open(f"{self.home}/{self.fname}", "w")
            except FileNotFoundError:
                print("Looks like you're trying to create a file \
inside of a directory that doesn't exist.")

    @home_folder_checker
    def show(self, fname, *args):
        self.fname = fname
        if os.path.isfile(f"{self.home}/{self.fname}"):
            with open(f"{self.home}/{self.fname}", "r") as f:
                self.fcontent = f.readlines()
            for i in self.fcontent:
                print(i, end='')
        else:
            print("That file doesn't exist.")

    @home_folder_checker
    def edit(self, fname, *args):
        self.fname = fname
        try:
            editor = pickle.load(open(f"{os.getcwd()}/editor.pkl", "rb"))
            subprocess.run([editor, f"{self.home}/{self.fname}"], shell=True)
        except OSError:
            try:
                subprocess.run(["nano", f"{self.home}/{self.fname}"], shell=True)
            except Exception as id:
                print(f"""An exception ocurred during the process.
Exception details: {id}""")

    @home_folder_checker
    def mkdir(self, dname, *args):
        self.dname = dname
        try:
            os.mkdir(f"{self.home}/{self.dname}")
        # Recursive
        except FileNotFoundError:
            os.makedirs(f"{self.home}/{self.dname}")
        except FileExistsError:
            print("That directory already exists!")

    @home_folder_checker
    def remove(self, name, *args):
        self.name = f"{self.home}/{name}"
        try:
            if os.path.isfile(self.name):
                os.remove(self.name)
            elif os.path.isdir(self.name):
                try:
                    os.rmdir(self.name)
                except OSError:
                    while True:
                        op = input("The directory you're trying to \
remove is not empty. Remove it anyways? [Y/n] ")
                        op = op.lower()
                        if op in ["y", "yes", " ", ""]:
                            shutil.rmtree(self.name)
                            break
                        elif op in ["n", "no", "nope"]:
                            print("Operation cancelled by user.")
                            break
                        else:
                            print("Please, enter a valid option.")
        except Exception as id:
            print(f"""An exception occurred during the process.
Exception details: {id}""")

    # TODO: Mejorar este comando.
    def help_fkos(self, *, command):
        self.command = command
        if self.command:
            print(self.commands_help[self.command])
        else:
            print("All available commands:\n")
            for i in self.commands_help.keys():
                print(f"{i}: {self.commands_help[i]}\n")

    def pyrun(self, fname, *args):
        self.fname = fname
        subprocess.run(["python", f"{self.home}/{self.fname}"], shell=True)

    def pyshell(self, *args):
        print("")
        subprocess.run("python", shell=True)
        print("")

    def interactive(self, *args):
        print("")
        subprocess.run("ipython", shell=True)
        print("")

    def clear(self, *args):
        subprocess.run("cls", shell=True)

    @home_folder_checker
    def cd(self, directory, *args):
        self.directory = directory
        os.chdir(f"{self.home}\\{self.directory}")

    # WIP: Execute python commands directly without
    # starting interpreter with 'shell'
    # def python(self, *args):
