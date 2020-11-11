#!/usr/bin/env python3

import signal
from art import text2art
import apps

print(text2art("FakeOS"))
print("Welcome to FakeOS!")

def signal_handler(signal, frame):
    print("\nBye ;D!")
    quit()

def handle_command(data):
    method = data[0]
    del data[0]

    if method == "exit":
        sure = input("Do you really want to logout? [Y/N] ")
        if sure == "Y" or sure == "y":
            print("Bye ;D!")
            quit()
        elif sure == "N" or sure == "n":
            return
        else:
            print("You haven't chosen a correct option. Canceling logout...")
            return
    else:
        try:
            if data:
                eval("apps." + method+"(*data)")
            else:
                eval("apps." + method)()
        except:
            print("Couldn't handle that command D:")
            return

signal.signal(signal.SIGINT, signal_handler)

while True:
    command = input("FOS > ")
    handle_command(command.split())
