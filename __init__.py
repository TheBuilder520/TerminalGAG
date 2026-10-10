"""TerminalGAG is a graphics engine that can be used to display data or write games inside of a terminal. There are a lot of modules and objects to help you build whatever you dream of inside of python."""

from TerminalGAG.GAGScreen import GAGScreen # packages are weird

from . import *
from .utils import *
import sys

try:
    import keyboard
    import pytweening
    import pyautogui
except:
    from os import system
    system("pip install keyboard")
    system("pip install pytweening")
    system("pip install pyautogui")

sys.stdout.write("\033[?25l")

# GAG is in front of names to avoid variable name clutter most of the time