#!/usr/bin/python3

# Main module, originally coded by FabioPolancoE, Sebastian-Byte
# and FRostri.
# Edited by Suaj
# NOTE: Documentation will be improved later

import os
import sys
from apps import *
from getpass import getuser
from setup import start_setup

try:
  from art import text2art
except ModuleNotFoundError:
  pass
else:
  print(text2art("FakeOS"))

print("Welcome to FakeOS!")

# To avoid possible errors with other modules, the exit function is handled here

def exit():
  while True:
    op = input("Are you sure you want to exit? [Y/n]: ")
    op = op.lower()
    if op in ["y", "yes", "", " "]:
      sys.exit(0)
    elif op in ["n", "no", "nope"]:
      break
    else:
      print("Please, enter a valid option.")

all_commands = {
  "hello": hello,
  "numguess": numguess,
  "ls": ls,
  "new": new,
  "show": show,
  "help": help_fkos,
  "pyshell": pyshell,
  "pyrun": pyrun,
  "interactive": interactive,
  "edit": edit,
  "install": start_setup,
  "clear": clear,
  "exit": exit,
}

# Get input with a BASH style
while True:
  op = input(f"[{getuser()}@FakeOS]$ ")
  op = op.lower()

  # Call the function. Argument support will be added in short.
  try:
    all_commands[op]()
  except KeyError:
    print(f"Whoops! The command \"{op}\" does not exist.")
  except Exception as id:
    print(f"""An exception occurred during the process.
Exception details: {id}""")
