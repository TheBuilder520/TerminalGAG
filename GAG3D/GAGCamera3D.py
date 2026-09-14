from time import sleep

from .GAGBasic3D import *
from ..GAG2D.objects.GAGText import *
from ..config import * 
from ..utils import *

import sys
import os

class GAGCamera3D(GAGBasic3D):
    def __init__(self, screen, state):
        super().__init__()
        self.screen = screen
        self.state = state
        self.height = screenHeight
        self.width = screenWidth
        self.depth = renderingDepth
        self.spaceX = 0
        self.spaceY = 0
        self.spaceZ = 0
        self.objectLink = None
        self.linkOffsetX = 0
        self.linkOffsetY = 0
        self.linkOffsetZ = 0
        self.hud = []
        if debug: print(f"camera initialized {self.width}x{self.height}x{self.depth}")

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
        self.screen.screen = self.screen.generateScreen() 
        for z in range(self.depth, -1, -1):
            scrollDepthX = (depthFactorX*z - z)
            scrollDepthY = (depthFactorY*z - z)
            #self.screen.update(elapsed)
            for y in range(self.height):
                for x in range(self.width):
                    #scrollDepthX *= x
                    if self.state.space[int((self.spaceZ + z) % self.state.depth)][int(((self.spaceY + y)+scrollDepthY) % self.state.height)][int(((self.spaceX + x)+scrollDepthX) % self.state.width)] != " ":
                        self.screen.screen[y+self.y][x+self.x] = hexANSI(brightness(self.state.colorMap[int((self.spaceZ + z) % self.state.depth)][int(((self.spaceY + y)+scrollDepthY) % self.state.height)][int(((self.spaceX + x)+scrollDepthX) % self.state.width)], 1/(z+1))) + self.state.space[int((self.spaceZ + z) % self.state.depth)][int(((self.spaceY + y)+scrollDepthY) % self.state.height)][int(((self.spaceX + x)+scrollDepthX) % self.state.width)] 

        for object in self.hud: 
            object.update(elapsed)

            if object.visible:
                insertObject(object, parseObject(object), self.screen.screen)
                #if debug: print(parsedObject)


            #print(self.screen.screen)
        
        if FPSCounter:
            self.GAGfps.text = "FPS: " + str(round(1/elapsed)) 

            if round(1/elapsed) < 10:
                self.GAGfps.color = "#ff0000"
            elif round(1/elapsed) < FPSLimit/2:
                self.GAGfps.color = "#ffff00"
            else:
                self.GAGfps.color = "#00ff00"

        self.screen.update(elapsed)