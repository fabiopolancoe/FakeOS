import os
import subprocess
from random import randint

all_commands = {"hello": "A simple command that prints 'Hello World!'", "numguess": "An awesome Guess-The-Number Game", "ls": "Lists all the files and directories inside the home folder", "new": "Creates a new file, use with 'new [filename]', i.e 'new hi.txt', do never use whitespace.", "show": "Prints the contents of a file", "help": "Shows information about a available commands", "exit": "Stops the execution of FakeOS", "pyshell": "Opens an embedded python3 shell", "pyrun": "Executes a python3 file, place the file inside the home folder and type 'pyrun [filename]', i.e. 'pyrun hello.py'", "interactive": "Opens an interactive python3 shell, requires 'ipython3' installed", "edit": "Edit or create files, type 'edit [filename]', i.e. 'edit note.txt', requires 'nano' installed"}

def hello():
    print("Hello World!")

def numguess():
    number = randint(1, 10)
    guess = int(input("I'm thinking a number from 1 to 10, try to guess it > "))
    
    if guess == number:
        print("¡Wow, you did it! :D")
    else:
        print("Bad luck, you failed D:")

def ls():
    home = os.listdir("./home")
    
    if home:
        for element in home:
            print(element+"\n")
    else:
        print("Home is empty, fill it with anything you want :D")

def new(filename):
    subprocess.call(["touch", "./home/" + filename])

def show(filename):
    subprocess.call(["cat", "./home/" + filename])

def help(*method):
    if method:
        print(all_commands.get(method[0]))
    else:
        print("Running 'help' will print data about all commands, if you want info about only one command, type 'help [command]', i.e. 'help hello'\n")
        for command in all_commands.keys():
            print(command+": "+all_commands.get(command)+"\n")

def pyrun(filename):
    subprocess.call(["python3", filename])

def pyshell():
    print("")
    subprocess.call("python3")
    print("")

def interactive():
    print("")
    subprocess.call("ipython3")
    print("")

def edit(filename):
    subprocess.call(["nano", "./home/"+filename])
