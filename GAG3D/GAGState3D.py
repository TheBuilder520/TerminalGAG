# This file handles everything state related.

import time
from .GAGBasic3D import *
from ..GAGKeys import *
from .GAGCamera3D import *
from ..startUp import *
from ..config import *
from ..utils import *
from time import sleep
import sys

class GAGState3D:
    def __init__(self, width=spaceWidth, height=spaceHeight, depth=spaceDepth):
        self.running = True
        self.objects = []
        self.space = self.generateSpace(width, height, depth)
        self.colorMap = self.generateSpace(width, height, depth) # Stores all colors in hex value to be later processed for depth effect
        self.camera = GAGCamera3D(mainScreen, self)
        if debug: print("State initialized")

    def __str__(self):
        """Returns the state name"""
        return self.__class__.__name__
    
    def create(self): # Called on start
        """Called when the state first runs"""
        if debug: print("State created")
        self.camera.create()

        self.GAGKeyboard = GAGKeyboard()

    def update(self, elapsed): # Called on every frame
        """Called every frame after create is finished""" 
        
        self.GAGKeyboard.update(elapsed)

        if FPSLimit != 0: 
            time.sleep(1/FPSLimit - 0.001)

        self.space = self.generateSpace(self.width, self.height, self.depth) # create a fresh slate                      
        self.colorMap = self.generateSpace(self.width, self.height, self.depth) 

        for object in self.objects: 
            object.update(elapsed)

            if object.visible: 
                insert3DObject(object, self.space, self.colorMap)
                #if debug: print(parsedObject)

        if self.camera.objectLink != None:
            self.camera.planeX = self.camera.objectLink.x + self.camera.linkOffsetX
            self.camera.planeY = self.camera.objectLink.y + self.camera.linkOffsetY
            self.camera.planeZ = self.camera.objectLink.z + self.camera.linkOffsetZ

        self.camera.update(elapsed)

    def destroy(self):
        """Closes the state and called when the state closes"""
        global inState
        self.running = False
        inState = False

    def add(self, object:GAGBasic):
        """Adds an object to the state."""
        object.create()
        self.objects.append(object)

    def remove(self, object:GAGBasic):
        self.objects.remove(object)
        object.destroy()

    def generateSpace(self, width, height, depth): # You've heard of 2d arrays before, now may I introduce 3D ARRAYS
        """Generates the physical space objects can appear on"""
        self.width = width
        self.height = height
        self.depth = depth

        space = [] 
        for z in range(depth):
            space.append([])
            for y in range(height):
                space[z].append([])
                for x in range(width):
                    space[z][y].append(" ")
        return space

    