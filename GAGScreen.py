from .config import *

import sys
import os

class GAGScreen:
    def __init__(self):
        
        self.screen = self.generateScreen() # The stuff you see
        self.lastFrame = self.generateScreen()

        # Break down of how the update screen works

        # checks each pixel to see if it is different from the last frame
        # If it is, update that one pixel to the frontend.

        # This will hopefully cut down on lag and not be resource intensive

        if debug: print("screen initialized")

    def __str__(self):
        """Returns the screen name"""
        return self.__class__.__name__
    
    def clearScreen(self):
        """Wipes the screen"""
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

        self.screen = self.generateScreen() # The stuff you see
        self.lastFrame = self.generateScreen()
    
    def create(self):
        """Ran when the object is first created"""
        if debug: 
            print("screen created")
        self.clearScreen()

    def update(self, elapsed):
        """Ran every frame"""
        # print(self.screen)
        # print(self.lastFrame)

        for y in range(screenHeight):
            for x in range(screenWidth):
                if self.screen[y][x] != self.lastFrame[y][x]:
                    self.lastFrame[y][x] = self.screen[y][x]
                    sys.stdout.write(f"\033[{y+1};{x+1}H{self.screen[y][x]}")

                    # I removed it... I understood what happened now.
                    # print() # DO NOT REMOVE THIS PRINT STATEMENT IF YOU REMOVE IT, WEIRD STUFF WILL HAPPEN AND YOU WILL WONDER WHAT IS WRONG FOR 2 HOURS! I CAN NOT DESCRIBE MY CONFUSION RIGHT NOW

                    # if debug: print("WOAH! SOMETHING CHANGED!") 

        sys.stdout.flush()

    def generateScreen(self):
        """Generates a blank screen"""
        screen = []
        for y in range(screenHeight):
            screen.append([])
            for x in range(screenWidth):
                screen[y].append(" ")
        return screen