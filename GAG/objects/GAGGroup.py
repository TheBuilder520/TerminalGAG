from ..GAGBasic import *
from ...utils import *

from numpy import array

class GAGGroup(GAGBasic):
    def __init__(self):
        super().__init__()
        self.width = screenWidth
        self.height = screenHeight
        self.plane = array(generatePlane(self.width, self.height, ""))
        self.objects:list[GAGBasic] = []
        self.__runningFunctions:list[GAGFunction] = []

    def update(self, elapsed):
        super().update(elapsed)
        self.plane = array(generatePlane(self.width, self.height, ""))

        for object in self.objects:
            object.update(elapsed)

            if object.visible:
                insertObject(object, object.draw(0, 0, object.width, object.height), self.plane)

        for function in self.__runningFunctions:
            function.update(elapsed)

            if not function.isRunning():
                self.__runningFunctions.remove(function)
                function.destroy()

    def add(self, object:GAGBasic):
        """Adds an object to the group."""
        object.create()
        self.objects.append(object)

    def call(self, function:GAGFunction):
        """Adds a function to the group."""
        function.create()
        self.__runningFunctions.append(function)

    def remove(self, object:GAGBasic):
        """Removes an object to the group."""
        self.objects.remove(object)
        object.destroy()

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)
        
        return self.plane[y1:y2, x1:x2]