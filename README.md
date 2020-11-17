# FakeOS
<p align="center">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/fabiopolancoe/fakeos.svg">
<img alt="GitHub" src="https://img.shields.io/github/license/fabiopolancoe/fakeos.svg">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/fabiopolancoe/fakeos.svg">

A simple terminal **simulator** written in Python3.

## Setup
- The only dependence of this project is [**DotEnv**](https://pypi.org/project/dotenv/) module.
- There are some optional dependencies:
  - [**Nano**](https://www.nano-editor.org/) Editor
  - [**IPython**](https://pypi.org/project/ipython/)
  - [**Art**](https://pypi.org/project/art/)
  - [**Pip**](https://pypi.org/project/pip/)
 
## Usage
We recommend to run `setup.py` script before using the program. But you can also run the program en then execute the `install` command.
To run the program, you can execute `python3 main.py` on Linux/MacOS or `python main.py` on Windows.
You will see the ASCII Art Text logo, a welcome message and the prompt, to get started, type _help_.

## Making apps
I decided to make it easier for users to create their own apps for FakeOS, just add a function to the _apps.py_ file with the code of you app.

## Files
There's a folder named home, where all the files of the "user" are saved by default, you can edit apps.py to use another folder.

Thanks to @KelviNosse for his feedback. And also thanks to @FRostri, @Sebastian-byte and @SuajCarrot for their collaboration
