# This file handles everything state related.

import time
from .GAGBasic import *
from ..GAGFunction import *
from ..config import *
from ..utils import *
from .objects.GAGText import *
from time import sleep
import sys

# The heart of TerminalGAG

class GAGState:
    def __init__(self):
        self.running = True
        self.objects = []
       
        self.__runningFunctions:list[GAGFunction] = []
        if debug: print("State initialized")

    def __str__(self):
        """Returns the state name"""
        return self.__class__.__name__
    
    def create(self): # Called on start
        """Called when the state first runs"""
        if debug: print("State created")

    def update(self, elapsed): # Called on every frame
        """Called every frame after create is finished""" 

        if FPSLimit != 0: 
            time.sleep(1/FPSLimit - 0.001)
        
        for object in self.objects: 
            object.update(elapsed)

        for function in self.__runningFunctions:
            function.update(elapsed)

            if not function.isRunning():
                self.__runningFunctions.remove(function)
                function.destroy()

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