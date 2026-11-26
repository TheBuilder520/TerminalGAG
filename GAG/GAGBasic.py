# This is a basic object that has all the basic attributes apparent on all objects
from ..GAGFunction import *
from ..GAGInstance import GAGInstance as GAGI # Dont ask how importing this here imports it everywhere else
from ..utils import *

from numpy import array

class GAGBasic:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.visible = True
        self.cameras = [GAGI.cameras[0]]
        self.object = "" # Basically in ASCII art format
        self.__runningFunctions:list[GAGFunction] = []

    def __str__(self):
        """Returns the object name"""
        return self.object

    def create(self):
        """Called when the object is created"""
        pass

    def update(self, elapsed):
        """Called when the state is updated every frame"""
        for function in self.__runningFunctions:
            function.update(elapsed)

            if not function.isRunning():
                self.__runningFunctions.remove(function)
                function.destroy()

        for cam in self.cameras:
            cam.draw(self)

    def draw(self, x1, y1, x2, y2):
        return array(parseObject(self))[y1:y2, x1:x2]

    def destroy(self):
        pass

    def call(self, function:GAGFunction):
        """Adds an object to the state."""
        function.create()
        self.__runningFunctions.append(function)