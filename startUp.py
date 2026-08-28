# This file is used to run some first time start up things that are required.

from .config import *
from .GAGScreen import *

if startingScreen:
    mainScreen = GAGScreen()