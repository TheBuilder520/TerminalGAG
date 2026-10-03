from TerminalGAG.GAGScreen import GAGScreen # packages are weird

from . import *
from .utils import *
import sys

try:
    import keyboard
    import pytweening
except:
    from os import system
    system("pip install keyboard")
    system("pip install pytweening")

sys.stdout.write("\033[?25l")

# GAG is in front of names to avoid variable name clutter most of the time