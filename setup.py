import subprocess
import pip
import sys
from os import environ
from os import getcwd

def start():
    print("Welcome to the FakeOS installation script")
    print("Checking if Art module is installed...")
    try:
        from art import text2art
        print("Art module is installed")
    except:
        temp = input("Art module is not installed, do you want me to install it? [Y/N] ")
        if temp == "Y" or temp == "y":
            pip.main(["install", "art"])
        elif temp == "N" or temp == "n":
            print("Ok, art module will not be installed")
        else:
            print("You haven't chosen a correct option, I will install module by default...")
            pip.main(["install", "art"])

    print("Checking if Dotenv module is installed...")
    try:
        from dotenv import load_dotenv
        print("Dotenv module is installed")
    except:
        temp = input("Dotenv module is not installed, do you want me to install it? [Y/N] ")
        if temp == "Y" or temp == "y":
            pip.main(["install", "python-dotenv"])
        elif temp == "N" or temp == "n":
            print("Ok, Dotenv module will not be installed")
        else:
            print("You haven't chosen a correct option, I will install module by default...")
            pip.main(["install", "python-dotenv"])

    if sys.platform != 'win32':
        temp = input("Do you want to add FakeOS to PATH? [Y/N] ")
        if temp == "Y" or "y":
            username = input("Please tell me your username: ")
            try:
                if "bash" in environ['SHELL']:
                    bashrc = open('/home/' + username + '/.bashrc', 'a')
                    bashrc.write("alias fakeos='python3 " + getcwd() + "/main.py'\nexport FAKEOSHOME=" + getcwd())
                    bashrc.close()
                if "zsh" in environ['SHELL']:
                    zshrc = open('/home/' + username + '/.zshrc', 'a')
                    zshrc.write("alias fakeos='python3 " + getcwd() + "/main.py'\nexport FAKEOSHOME=" + getcwd())
                    zshrc.close()
            except Exception as identifier:
                print("Sorry, this cannot be done for now:")
                print(identifier)
        elif temp == "N" or "n":
            print("This cannot be done for now")
    else:
        pass

    print("Nano, Vim, Neovim, Notepad, Gedit, Pluma")
    editor = input("Choose your favorite text editor (It should obviously be installed): ")
    if editor == 'Neovim' or 'neovim':
        editor = 'nvim' # Change name to executable of Neovim.
    elif editor == "Notepad":
        editor = "notepad.exe"
    data = open('./data.env', 'w')
    data.write("EDITOR = " + editor.lower())


if __name__ == "__main__":
    start()
