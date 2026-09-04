from TerminalGAG.GAGScreen import GAGScreen # packages are weird

from . import *
from .GAGState import *
import sys

sys.stdout.write("\033[?25l")

# GAG is in front of names to avoid variable name clutter most of the time