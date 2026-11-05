# This file handles everything state related.

import time
from .GAGBasic import *
from ..GAGFunction import *
from ..GAGKeys import *
from .GAGCamera import *
from ..startUp import *
from ..config import *
from ..utils import *
from .objects.GAGText import *
from time import sleep
import sys

# The heart of TerminalGAG

class GAGState:
    def __init__(self, width=planeWidth, height=planeHeight):
        self.running = True
        self.objects = []
        self.fillChar = " "
        self.plane = self.generatePlane(width, height)
        self.camera = GAGCamera(mainScreen, self)
       
        self.__runningFunctions:list[GAGFunction] = []
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

        self.plane = self.generatePlane(self.width, self.height) # create a fresh slate                      
        
        for object in self.objects: 
            object.update(elapsed)

            if object.visible:
                parsedObject = parseObject(object)
                insertObject(object, parsedObject, self.plane)
                #if debug: print(parsedObject)

        for function in self.__runningFunctions:
            function.update(elapsed)

            if not function.isRunning():
                self.__runningFunctions.remove(function)
                function.destroy()

        if self.camera.objectLink != None:
            self.camera.planeX = self.camera.objectLink.x + self.camera.linkOffsetX
            self.camera.planeY = self.camera.objectLink.y + self.camera.linkOffsetY

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

    def call(self, function:GAGFunction):
        """Adds an object to the state."""
        function.create()
        self.__runningFunctions.append(function)

    def remove(self, object:GAGBasic):
        self.objects.remove(object)
        object.destroy()

    def generatePlane(self, width, height):
        """Generates the physical space objects can appear on"""
        self.width = width
        self.height = height

        plane = []
        for y in range(height):
            plane.append([])
            for x in range(width):
                plane[y].append(self.fillChar)
        return plane