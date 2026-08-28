from .GAGBasic import *
from .objects.GAGText import *
from .config import *
from .utils import *

import sys
import os

class GAGCamera(GAGBasic):
    def __init__(self, screen, state):
        super().__init__()
        self.screen = screen
        self.state = state
        self.height = screenHeight
        self.width = screenWidth
        self.planeX = 0
        self.planeY = 0
        self.objectLink = None
        self.linkOffsetX = 0
        self.linkOffsetY = 0
        self.hud = []
        if debug: print(f"camera initialized {self.width}x{self.height}")

    def __str__(self):
        """Returns the camera name"""
        return self.__class__.__name__
    
    def create(self):
        """Ran when the object is first created"""
        super().create()
        if debug: print("camera created")

        if FPSCounter:
            self.GAGfps = GAGText(0, 0, "")
            self.GAGfps.create()
            self.add(self.GAGfps)

        self.screen.create()

    def add(self, object:GAGBasic):
        """Adds an object to the state."""
        object.create()
        self.hud.append(object)
        
    def update(self, elapsed):
        """Ran every frame"""
        super().update(elapsed)
        for y in range(self.height):
            for x in range(self.width):
                   self.screen.screen[y+self.y][x+self.x] = self.state.plane[int((self.planeY + y) % self.state.height)][int((self.planeX + x) % self.state.width)] 

        for object in self.hud: 
            object.update(elapsed)

            if object.visible:
                parsedObject = parseObject(object)
                insertObject(object, parsedObject, self.screen.screen)
                #if debug: print(parsedObject)
        
        if FPSCounter:
            self.GAGfps.text = "FPS: " + str(round(1/elapsed)) 

            if round(1/elapsed) < 10:
                self.GAGfps.color = "#ff0000"
            elif round(1/elapsed) < FPSLimit/2:
                self.GAGfps.color = "#ffff00"
            else:
                self.GAGfps.color = "#00FF00"

        self.screen.update(elapsed)