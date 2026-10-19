"""TerminalGAG is a graphics engine that can be used to display data or write games inside of a terminal. There are a lot of modules and objects to help you build whatever you dream of inside of python."""

try:
    import keyboard
    import mouse
    import pytweening
    import win32api
    import pygame

except:
    from os import system
    system("pip install mouse")
    system("pip install keyboard")
    system("pip install pytweening")
    system("pip install pywin32")
    system("pip install pygame-ce") # Use ce since it works for some reason

from TerminalGAG.GAGScreen import GAGScreen # packages are weird

from . import *
from .GAGSplash import *
from .utils import *
import sys

sys.stdout.write("\033[?25l")

# GAG is in front of names to avoid variable name clutter most of the time

if doSplash:
    switchStates(SplashScreen())